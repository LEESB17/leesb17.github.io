---
title: "Isaac Sim 데이터 수집 정밀도 향상 가이드: record.py vs record_v2.py"
categories:
  - isaacsim
tags:
  - Isaac Sim
  - Robotics
  - Data Generation
---

Isaac Sim에서 데이터를 수집할 때 "이미지와 포즈가 미세하게 어긋나는 문제"를 해결한 과정과 `record_v2.py`의 개선 사항을 정리합니다. 정밀한 **Scene Graph** 구성이나 **3D Reconstruction** 학습용 데이터를 구축한다면 v2 방식이 필수적입니다.

## 1. 카메라 포즈 계산 방식의 정밀도 향상
가장 큰 차이점은 카메라의 위치(Position)와 회전(Quaternion) 값을 가져오는 방식입니다.

* **v1 (직접 추출):** `camera.get_world_pose()`를 사용합니다. 시뮬레이션 엔진 값을 그대로 가져오지만, 렌더링 시점과 데이터 획득 시점 사이에 미세한 타임스텝(dt) 차이가 발생할 수 있습니다.
* **v2 (행렬 역산):** Replicator의 `camera_params` 주석가(Annotator)를 통해 `cameraViewTransform` 행렬을 가져와 `np.linalg.inv()`로 역산합니다. 렌더링된 해당 프레임의 실제 행렬을 사용하므로 수학적으로 완벽하게 일치합니다.

## 2. 변환 속성의 정밀도 강제 (PrecisionDouble)
USD 데이터 구조에서 발생할 수 있는 소수점 오차를 차단했습니다.

* **v2의 `set_transform_safe` 함수:** `UsdGeom.XformOp.PrecisionDouble`을 명시적으로 사용합니다.
* **이유:** `VisualCuboid` 같은 객체는 기본적으로 Double 정밀도를 사용하는데, 일반적인 속성 설정 시 Float으로 형변환되며 생기는 미세한 반올림 오차를 방지하기 위함입니다.

## 3. 렌더링 최적화 및 동기화 (TAA/Motion Blur 제거)
데이터의 선명도를 떨어뜨리는 렌더링 아티팩트를 제거했습니다.

1.  **TAA (Temporal Anti-Aliasing) OFF:** 이전 프레임 정보를 섞는 잔상을 제거하여 이동 중에도 선명한 외곽선을 얻습니다.
2.  **Motion Blur OFF:** 픽셀 단위의 정확도를 위해 빠른 움직임 시 발생하는 번짐 효과를 제거했습니다.

## 4. Replicator API 기반 동기화
`record_v2.py`는 Isaac Sim의 고수준 데이터 수집 도구인 **Omni Replicator**를 사용합니다. Replicator의 Gate 시스템을 통해 물리 엔진의 스텝, 렌더링, 데이터 저장이 완전히 동기화되어 타임 래그(Time Lag) 문제를 해결했습니다.

---

### 요약: 왜 record_v2가 더 정확한가요?

| 구분 | record.py (v1) | record_v2.py (v2) |
| :--- | :--- | :--- |
| **포즈 데이터** | 엔진 API 값을 신뢰 | 실제 렌더링 행렬 역산 (100% 동기화) |
| **수치 정밀도** | 자동 형변환 (Float 가능성) | `PrecisionDouble` 오차 차단 |
| **이미지 품질** | TAA/잔상 포함 가능성 | 렌더링 아티팩트 제거 |
| **프레임 동기화** | 수동 획득 (타임 래그 발생) | Replicator 기반 동기화 |

---

## 관련 코드
전체 코드는 아래 링크에서 확인할 수 있습니다.
* [코드 확인: record_v2.py](/assets/scripts/isaac-sim/record_v2.py)
