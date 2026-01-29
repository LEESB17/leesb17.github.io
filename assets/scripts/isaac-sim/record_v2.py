from isaacsim import SimulationApp
import carb.settings

# 화면 확인용
simulation_app = SimulationApp({"headless": False})

import os
import json
import numpy as np
from PIL import Image
from datetime import datetime
import omni.ui as ui
import omni.replicator.core as rep

from omni.isaac.core import World
from omni.isaac.core.objects import VisualCuboid, VisualCylinder
from omni.isaac.core.utils.stage import open_stage
from omni.isaac.core.utils.prims import create_prim, get_prim_at_path
from pxr import Gf, UsdGeom

# ================= [설정] =================
USD_PATH = "/home/sungbin/isaac/sg/scene/kitchen/World0.usd"
SAVE_ROOT_DIR = "/home/sungbin/isaac/sg/captured_sessions"

ZED_CONFIGS = {
    "WIDE (2.1mm)": {"focal": 2.12, "h_aperture": 4.8, "v_aperture": 2.7},
    "NARROW (4.0mm)": {"focal": 4.0, "h_aperture": 4.8, "v_aperture": 2.7}
}

state = {
    "current_mode": "NARROW (4.0mm)",
    "is_recording": False,
    "current_session_dir": "",
    "frame_count": 0,
    "render_product": None,
    "annotators": {}
}

RESOLUTION = (1280, 720)
os.makedirs(SAVE_ROOT_DIR, exist_ok=True)
# ==========================================

def setup_render_settings():
    print(">>> 렌더링 설정 최적화 (TAA OFF, Motion Blur OFF)...")
    settings = carb.settings.get_settings()
    settings.set_int("/rtx/post/aa/op", 0)
    settings.set_bool("/rtx/post/motionblur/enabled", False)
    settings.set_int("/rtx/post/dlss/execMode", 0)

# [FIX] 정밀도 충돌 해결 함수
def set_transform_safe(prim_path, translate=None, rotate_xyz=None, scale=None):
    """
    USD 표준 순서(T-R-S) 적용 및 PrecisionDouble 강제 사용으로 에러 방지
    """
    prim = get_prim_at_path(prim_path)
    if not prim: return
    
    xform = UsdGeom.Xformable(prim)
    xform.ClearXformOpOrder() # 기존 순서 초기화
    
    # [핵심 수정] PrecisionDouble을 명시하여 VisualCuboid(Double)와의 충돌 방지
    if translate is not None:
        xform.AddTranslateOp(UsdGeom.XformOp.PrecisionDouble).Set(Gf.Vec3d(*translate))
    if rotate_xyz is not None:
        xform.AddRotateXYZOp(UsdGeom.XformOp.PrecisionDouble).Set(Gf.Vec3d(*rotate_xyz))
    if scale is not None:
        xform.AddScaleOp(UsdGeom.XformOp.PrecisionDouble).Set(Gf.Vec3d(*scale))

def main():
    print(f"시스템 초기화 중...")
    try: open_stage(USD_PATH)
    except: simulation_app.close(); return

    world = World(stage_units_in_meters=1.0, physics_dt=1.0/60.0, rendering_dt=1.0/60.0)
    try: create_prim("/World/Env/DomeLight", "DomeLight", attributes={"inputs:intensity": 1000.0})
    except: pass

    setup_render_settings()

    # -----------------------------------------------------------
    # [1] 카메라 리그(Rig) 완벽 조립
    # -----------------------------------------------------------
    rig_path = "/World/ZED_Rig"
    
    # 1. 리그 부모 (Xform)
    create_prim(rig_path, "Xform")
    set_transform_safe(rig_path, translate=(2.0, 2.0, 1.5))
    
    # 2. 시각적 바디 (빨간 상자)
    VisualCuboid(prim_path=f"{rig_path}/Body", color=np.array([0.8, 0.1, 0.1]))
    # 바디: 위치 0,0,0, 스케일만 적용
    set_transform_safe(f"{rig_path}/Body", scale=(0.1, 0.4, 0.1))
    
    # 3. 시각적 렌즈 (파란 원통)
    VisualCylinder(prim_path=f"{rig_path}/Lens", color=np.array([0.1, 0.1, 1.0]))
    # 렌즈: 바디 앞(Y=0.2) + 90도 회전(눕힘) + 스케일
    set_transform_safe(f"{rig_path}/Lens", 
                       translate=(0, 0.2, 0), 
                       rotate_xyz=(90, 0, 0), 
                       scale=(0.05, 0.05, 0.05))
    
    # 4. 실제 센서 (카메라)
    cam_prim_path = f"{rig_path}/Sensor"
    create_prim(cam_prim_path, "Camera")
    # 센서: 렌즈보다 더 앞(Y=0.22) + 90도 회전(정면 보기)
    set_transform_safe(cam_prim_path, 
                       translate=(0, 0.22, 0), 
                       rotate_xyz=(90, 0, 0))

    # -----------------------------------------------------------
    # [2] Replicator 연결
    # -----------------------------------------------------------
    render_product = rep.create.render_product(cam_prim_path, RESOLUTION)
    
    rgb_annot = rep.AnnotatorRegistry.get_annotator("rgb")
    depth_annot = rep.AnnotatorRegistry.get_annotator("distance_to_image_plane")
    params_annot = rep.AnnotatorRegistry.get_annotator("camera_params")

    rgb_annot.attach(render_product)
    depth_annot.attach(render_product)
    params_annot.attach(render_product)

    state["annotators"] = {"rgb": rgb_annot, "depth": depth_annot, "params": params_annot}

    def apply_zed_specs(mode_name):
        conf = ZED_CONFIGS[mode_name]
        # 속성 설정은 안전하게 Attribute API 사용
        prim = get_prim_at_path(cam_prim_path)
        if prim:
            prim.GetAttribute("focalLength").Set(conf["focal"])
            prim.GetAttribute("horizontalAperture").Set(conf["h_aperture"])
            prim.GetAttribute("verticalAperture").Set(conf["v_aperture"])
            prim.GetAttribute("clippingRange").Set(Gf.Vec2f(0.1, 100.0))

    world.reset()
    apply_zed_specs(state["current_mode"])

    # -----------------------------------------------------------
    # [3] 데이터 추출 함수
    # -----------------------------------------------------------
    def get_pose_from_params(params_data):
        view_matrix = params_data["cameraViewTransform"].reshape(4, 4)
        c2w_matrix = np.linalg.inv(view_matrix)
        
        pos = c2w_matrix[3, :3]
        rot_mat = c2w_matrix[:3, :3]
        
        gf_mat = Gf.Matrix3d(
            float(rot_mat[0,0]), float(rot_mat[0,1]), float(rot_mat[0,2]),
            float(rot_mat[1,0]), float(rot_mat[1,1]), float(rot_mat[1,2]),
            float(rot_mat[2,0]), float(rot_mat[2,1]), float(rot_mat[2,2])
        )
        q = gf_mat.ExtractRotation().GetQuaternion()
        quat_wxyz = [q.GetReal(), q.GetImaginary()[0], q.GetImaginary()[1], q.GetImaginary()[2]]
        
        return pos, quat_wxyz

    def save_frame():
        f_idx = f"{state['frame_count']:05d}"
        session_dir = state["current_session_dir"]
        
        rgb = state["annotators"]["rgb"].get_data()
        depth = state["annotators"]["depth"].get_data()
        params = state["annotators"]["params"].get_data()

        if rgb is not None and params is not None:
            Image.fromarray(rgb[:, :, :3]).save(os.path.join(session_dir, "rgb", f"rgb_{f_idx}.png"))
            np.save(os.path.join(session_dir, "depth_raw", f"depth_{f_idx}.npy"), depth)
            
            d_vis = np.clip(depth, 0, 10.0) / 10.0
            Image.fromarray((d_vis * 255).astype(np.uint8)).save(os.path.join(session_dir, "depth_viz", f"depth_{f_idx}.png"))

            pos, rot = get_pose_from_params(params)
            
            pose_info = {
                "frame": state["frame_count"],
                "timestamp": datetime.now().isoformat(),
                "position": pos.tolist(),
                "quaternion_wxyz": rot
            }
            with open(os.path.join(session_dir, "poses", f"pose_{f_idx}.json"), "w") as f:
                json.dump(pose_info, f, indent=2)

            state["frame_count"] += 1

    # -----------------------------------------------------------
    # [4] UI 설정
    # -----------------------------------------------------------
    def on_start_rec():
        if not state["is_recording"]:
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            session_path = os.path.join(SAVE_ROOT_DIR, f"session_{ts}")
            state["current_session_dir"] = session_path
            state["frame_count"] = 0
            for s in ["rgb", "depth_raw", "depth_viz", "poses"]:
                os.makedirs(os.path.join(session_path, s), exist_ok=True)
            state["is_recording"] = True
            btn_start.enabled = False; btn_stop.enabled = True
            print(f">>> REC START: {session_path}")

    def on_stop_rec():
        if state["is_recording"]:
            state["is_recording"] = False
            conf = ZED_CONFIGS[state["current_mode"]]
            info = {
                "device": "ZED 2i", "lens": state["current_mode"],
                "intrinsics": {"focal": conf["focal"], "res": list(RESOLUTION)},
                "total_frames": state["frame_count"]
            }
            with open(os.path.join(state["current_session_dir"], "camera_info.json"), "w") as f:
                json.dump(info, f, indent=4)
            btn_start.enabled = True; btn_stop.enabled = False
            print(">>> REC STOPPED")

    window = ui.Window("Final Precision Recorder", width=400, height=280)
    with window.frame:
        with ui.VStack(spacing=15):
            ui.Label("Final Precision Recorder", style={"font_size": 18, "color": 0xFF00FF00})
            ui.Label("No Errors | Correct View | Clean Data", style={"color": 0xFF888888, "font_size": 12})
            
            with ui.HStack(height=30):
                ui.Label("Mode:", width=60)
                combo = ui.ComboBox(1, *list(ZED_CONFIGS.keys()))
                combo.model.add_item_changed_fn(lambda m, i: apply_zed_specs(list(ZED_CONFIGS.keys())[combo.model.get_item_value().as_int]))
            
            with ui.HStack(spacing=10):
                btn_start = ui.Button("START", height=60, clicked_fn=on_start_rec)
                btn_stop = ui.Button("STOP", height=60, clicked_fn=on_stop_rec, enabled=False)
            status_label = ui.Label("Idle", style={"color": 0xFF888888})

    while simulation_app.is_running():
        world.step(render=True)
        if state["is_recording"]:
            save_frame()
            status_label.text = f"REC: {state['frame_count']}"
            status_label.style = {"color": 0xFF0000FF}
        else:
            status_label.text = "Idle"

    simulation_app.close()

if __name__ == "__main__":
    main()