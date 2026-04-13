---
title: "연구실 활동 타임라인"
permalink: /lab-timeline/
layout: single
author_profile: true
toc: false
---

> 2025.07 ~ 2026.04 랩미팅 발표 기반 연구 활동 정리입니다.

<style>
.tl-wrap { position: relative; padding-left: 28px; margin-top: 2rem; }
.tl-wrap::before { content:''; position:absolute; left:8px; top:0; bottom:0; width:2px; background:#e0e0e0; }
.tl-item { position:relative; margin-bottom:1.6rem; }
.tl-dot { position:absolute; left:-24px; top:6px; width:12px; height:12px; border-radius:50%; border:2.5px solid; }
.tl-card { border:1px solid #e8e8e8; border-radius:8px; padding:14px 16px; background:#fff; }
.tl-card:hover { border-color:#aaa; }
.tl-date { font-size:0.72rem; font-weight:600; color:#888; letter-spacing:.04em; margin-bottom:3px; }
.tl-title { font-size:0.95rem; font-weight:700; margin-bottom:6px; color:#222; }
.tl-tags { display:flex; flex-wrap:wrap; gap:4px; margin-bottom:8px; }
.tl-tag { font-size:0.68rem; padding:2px 9px; border-radius:20px; font-weight:600; }
.tag-paper { background:#e8f0fe; color:#1a56c4; }
.tag-impl  { background:#e6f4ea; color:#1a7a3c; }
.tag-hw    { background:#fef3e2; color:#a05c00; }
.tag-exp   { background:#fce8e6; color:#b31412; }
.tag-corp  { background:#f3e8ff; color:#6d28d9; }
.tl-section { margin-bottom:8px; }
.tl-section-title { font-size:0.68rem; font-weight:700; color:#888; text-transform:uppercase; letter-spacing:.06em; margin-bottom:3px; }
.tl-ul { list-style:none; padding:0; margin:0; }
.tl-ul li { font-size:0.82rem; color:#444; padding:2px 0 2px 12px; position:relative; line-height:1.5; }
.tl-ul li::before { content:'·'; position:absolute; left:0; color:#bbb; }
.tl-note { font-size:0.82rem; color:#555; line-height:1.6; padding:8px 10px; background:#f8f8f8; border-radius:5px; border-left:3px solid #ddd; }
.tl-legend { display:flex; flex-wrap:wrap; gap:8px; margin-bottom:1.5rem; }
.tl-legend span { font-size:0.75rem; color:#666; display:flex; align-items:center; gap:5px; }
.tl-legend-dot { width:8px; height:8px; border-radius:50%; display:inline-block; }
details summary { cursor:pointer; font-size:0.8rem; color:#666; margin-top:6px; }
details summary:hover { color:#333; }
details[open] summary { color:#333; }
</style>

<div class="tl-legend">
  <span><span class="tl-legend-dot" style="background:#5c85d6"></span>논문 리뷰</span>
  <span><span class="tl-legend-dot" style="background:#2e9e5e"></span>구현 / 개발</span>
  <span><span class="tl-legend-dot" style="background:#c47c10"></span>하드웨어 / 환경</span>
  <span><span class="tl-legend-dot" style="background:#c0392b"></span>실험 / 분석</span>
  <span><span class="tl-legend-dot" style="background:#7c3aed"></span>기업과제</span>
</div>

<div class="tl-wrap">

<!-- 1 -->
<div class="tl-item">
  <div class="tl-dot" style="background:#8aabde;border-color:#5c85d6"></div>
  <div class="tl-card">
    <div class="tl-date">2025.07.08 전후</div>
    <div class="tl-title">RoboPoint 논문 리뷰 & ROS2 환경 구축</div>
    <div class="tl-tags">
      <span class="tl-tag tag-paper">논문</span>
      <span class="tl-tag tag-hw">하드웨어</span>
    </div>
    <details>
      <summary>자세히 보기</summary>
      <div style="margin-top:10px">
        <div class="tl-section">
          <div class="tl-section-title">다룬 논문</div>
          <ul class="tl-ul">
            <li>RoboPoint: A Vision-Language Model for Spatial Affordance Prediction for Robotics</li>
          </ul>
        </div>
        <div class="tl-section">
          <div class="tl-section-title">구현 / 작업</div>
          <ul class="tl-ul">
            <li>ROS2 환경 구축 (연구실 원격 실습용)</li>
            <li>YOLO 연동 테스트</li>
          </ul>
        </div>
        <div class="tl-note">RoboPoint 핵심: 언어 지시만으로 부정확한 위치 출력하는 VLM 한계를 point-based action space로 보완. 어포던스 예측 후 3D 좌표 변환. 완전 자동화 데이터 파이프라인으로 시뮬레이션 데이터만으로 실제 환경 일반화.</div>
      </div>
    </details>
  </div>
</div>

<!-- 2 -->
<div class="tl-item">
  <div class="tl-dot" style="background:#6dc49a;border-color:#2e9e5e"></div>
  <div class="tl-card">
    <div class="tl-date">2025.07.22</div>
    <div class="tl-title">RoboPoint 구현 & Agentic AI 탐색</div>
    <div class="tl-tags">
      <span class="tl-tag tag-impl">구현</span>
      <span class="tl-tag tag-paper">논문</span>
    </div>
    <details>
      <summary>자세히 보기</summary>
      <div style="margin-top:10px">
        <div class="tl-section">
          <div class="tl-section-title">구현 / 작업</div>
          <ul class="tl-ul">
            <li>RoboPoint demo 테스트</li>
            <li>NVIDIA Isaac Sim으로 데이터셋 생성 시도</li>
            <li>CrewAI 기반 Agentic AI 실험</li>
          </ul>
        </div>
        <div class="tl-note">AI Assistant(reactive) vs AI Agent(proactive) 개념 정리. Agent는 사용자 프롬프트 없이도 자율적으로 목표를 추구.</div>
      </div>
    </details>
  </div>
</div>

<!-- 3 -->
<div class="tl-item">
  <div class="tl-dot" style="background:#8aabde;border-color:#5c85d6"></div>
  <div class="tl-card">
    <div class="tl-date">2025.08.05</div>
    <div class="tl-title">Mobile Agent V2 논문 리뷰</div>
    <div class="tl-tags">
      <span class="tl-tag tag-paper">논문</span>
    </div>
    <details>
      <summary>자세히 보기</summary>
      <div style="margin-top:10px">
        <div class="tl-section">
          <div class="tl-section-title">다룬 논문</div>
          <ul class="tl-ul">
            <li>Mobile Agent V2 — 수평적 멀티에이전트 (Planning / Decision / Reflect 순환 구조)</li>
            <li>Agentic AI - Threats and Mitigations</li>
          </ul>
        </div>
        <div class="tl-note">모바일 조작에서 여러 앱을 오갈 때 생기는 focus content 손실 문제를 메모리 유닛으로 해결하는 구조 파악.</div>
      </div>
    </details>
  </div>
</div>

<!-- 4 -->
<div class="tl-item">
  <div class="tl-dot" style="background:#6dc49a;border-color:#2e9e5e"></div>
  <div class="tl-card">
    <div class="tl-date">2025.08 중후반</div>
    <div class="tl-title">AI Agent 구현 & Mobile Agent E 비교</div>
    <div class="tl-tags">
      <span class="tl-tag tag-impl">구현</span>
      <span class="tl-tag tag-paper">논문</span>
    </div>
    <details>
      <summary>자세히 보기</summary>
      <div style="margin-top:10px">
        <div class="tl-section">
          <div class="tl-section-title">다룬 논문</div>
          <ul class="tl-ul">
            <li>Mobile Agent E — 계층적(Hierarchical) 멀티에이전트 + Self Improving 5단계 사이클</li>
          </ul>
        </div>
        <div class="tl-section">
          <div class="tl-section-title">구현 / 작업</div>
          <ul class="tl-ul">
            <li>로봇용 AI Agent 파이프라인 설계: planning → vision(robopoint) → check → action → reflection</li>
            <li>Self Improving 5단계 분석: Experience → Reflection → Knowledge → Memory → Utilization</li>
          </ul>
        </div>
        <div class="tl-note">딜레이 문제, 메모리 관리, 하드웨어 안전성, 센서 데이터 관리 등 실제 로봇 시스템의 핵심 과제 도출.</div>
      </div>
    </details>
  </div>
</div>

<!-- 5 -->
<div class="tl-item">
  <div class="tl-dot" style="background:#6dc49a;border-color:#2e9e5e"></div>
  <div class="tl-card">
    <div class="tl-date">2025.09.19</div>
    <div class="tl-title">에이전트 시스템 구현 & VLMPC / GEPA / SAFER</div>
    <div class="tl-tags">
      <span class="tl-tag tag-impl">구현</span>
      <span class="tl-tag tag-paper">논문</span>
    </div>
    <details>
      <summary>자세히 보기</summary>
      <div style="margin-top:10px">
        <div class="tl-section">
          <div class="tl-section-title">다룬 논문</div>
          <ul class="tl-ul">
            <li>VLMPC: Vision-Language Model Predictive Control for Robotic Manipulation</li>
            <li>GEPA: Reflective Prompt Evolution (RL 대체 가능성)</li>
            <li>Safety Aware Task Planning via LLMs in Robotics (SAFER-CBF)</li>
          </ul>
        </div>
        <div class="tl-section">
          <div class="tl-section-title">구현 / 작업</div>
          <ul class="tl-ul">
            <li>Planning → Vision Prompt → Affordance → Check → Action 파이프라인 구현</li>
            <li>Isaac Sim + ZED 카메라 연동 테스트</li>
            <li>동아리 대회 이상탐지 모델(anomalib) 준비</li>
          </ul>
        </div>
        <div class="tl-note">VLMPC: VLM + MPC로 미래 행동 예측. Conditional Action Sampling — 7-dim vector → 가우시안 샘플링 → visual foresight로 최적 제어값 선택.</div>
      </div>
    </details>
  </div>
</div>

<!-- 6 -->
<div class="tl-item">
  <div class="tl-dot" style="background:#daa050;border-color:#c47c10"></div>
  <div class="tl-card">
    <div class="tl-date">2025.10.02</div>
    <div class="tl-title">Go2 로봇 와이파이 세팅 & 연구 방향 구체화</div>
    <div class="tl-tags">
      <span class="tl-tag tag-hw">하드웨어</span>
      <span class="tl-tag tag-paper">논문</span>
    </div>
    <details>
      <summary>자세히 보기</summary>
      <div style="margin-top:10px">
        <div class="tl-section">
          <div class="tl-section-title">다룬 논문</div>
          <ul class="tl-ul">
            <li>SICNav: Safe and Interactive Crowd Navigation using MPC and Bilevel Optimization</li>
          </ul>
        </div>
        <div class="tl-section">
          <div class="tl-section-title">구현 / 작업</div>
          <ul class="tl-ul">
            <li>Go2 와이파이 동글 세팅 (8일 소요 — RTL8811AU 드라이버로 해결)</li>
            <li>Jetson Orin 초기화 및 CUDA 포함 이미지 플래싱</li>
          </ul>
        </div>
        <div class="tl-note">연구 방향 구체화: 멀티 플랜 생성 → 순위 매기기 → 최선책 수행 중 변수 발생 시 차선책 전환. Reflect 에이전트가 에피소딕 메모리로 에이전트 간 통신 최소화 설계.</div>
      </div>
    </details>
  </div>
</div>

<!-- 7 -->
<div class="tl-item">
  <div class="tl-dot" style="background:#6dc49a;border-color:#2e9e5e"></div>
  <div class="tl-card">
    <div class="tl-date">2025.11.14</div>
    <div class="tl-title">ConceptGraph 구현 (씬그래프 생성)</div>
    <div class="tl-tags">
      <span class="tl-tag tag-impl">구현</span>
      <span class="tl-tag tag-hw">하드웨어</span>
    </div>
    <details>
      <summary>자세히 보기</summary>
      <div style="margin-top:10px">
        <div class="tl-section">
          <div class="tl-section-title">구현 / 작업</div>
          <ul class="tl-ul">
            <li>ZED 2i Stereo Camera 세팅 및 데이터셋 생성 (depth + RGB + pose traj.txt)</li>
            <li>Isaac Sim 데이터로 ConceptGraph 실행</li>
            <li>Pose 값 문제 디버깅 (/zed/zed_node/pose → world pose 변환)</li>
            <li>바운딩박스 중복 제거 코드 직접 추가 (IoU 기반 병합)</li>
          </ul>
        </div>
        <div class="tl-note">카메라 pose 변환 문제 직접 해결. 다음 목표: ConceptGraph mapping 최적화 + multi-agent 시스템에 scene graph 연결.</div>
      </div>
    </details>
  </div>
</div>

<!-- 8 -->
<div class="tl-item">
  <div class="tl-dot" style="background:#6dc49a;border-color:#2e9e5e"></div>
  <div class="tl-card">
    <div class="tl-date">2025.11.27</div>
    <div class="tl-title">씬그래프 수정 & Planner 연동</div>
    <div class="tl-tags">
      <span class="tl-tag tag-impl">구현</span>
    </div>
    <details>
      <summary>자세히 보기</summary>
      <div style="margin-top:10px">
        <div class="tl-section">
          <div class="tl-section-title">구현 / 작업</div>
          <ul class="tl-ul">
            <li>Scene graph = node(물체 정보) + edge(관계). Gemini API로 edge 자동 생성</li>
            <li>같은 물체를 여러 object로 인식하는 문제 → 바운딩박스 병합 로직 추가</li>
            <li>Planner에 씬그래프 인식 연동</li>
          </ul>
        </div>
      </div>
    </details>
  </div>
</div>

<!-- 9 -->
<div class="tl-item">
  <div class="tl-dot" style="background:#daa050;border-color:#c47c10"></div>
  <div class="tl-card">
    <div class="tl-date">2025.12.26</div>
    <div class="tl-title">B-1 로봇 세팅 & 논문 탐색</div>
    <div class="tl-tags">
      <span class="tl-tag tag-hw">하드웨어</span>
      <span class="tl-tag tag-paper">논문</span>
    </div>
    <details>
      <summary>자세히 보기</summary>
      <div style="margin-top:10px">
        <div class="tl-section">
          <div class="tl-section-title">다룬 논문</div>
          <ul class="tl-ul">
            <li>DrPlanner: LLM 기반 Motion Planner 자동 진단 & 코드 수정 제안</li>
            <li>LLM3: LLM 기반 Task & Motion Planning with Motion Failure Reasoning</li>
          </ul>
        </div>
        <div class="tl-section">
          <div class="tl-section-title">구현 / 작업</div>
          <ul class="tl-ul">
            <li>B-1 로봇 기본 세팅 80% 완료</li>
            <li>경로 생성은 가능하나 경로 추적 문제 확인</li>
          </ul>
        </div>
      </div>
    </details>
  </div>
</div>

<!-- 10 -->
<div class="tl-item">
  <div class="tl-dot" style="background:#6dc49a;border-color:#2e9e5e"></div>
  <div class="tl-card">
    <div class="tl-date">2026.01.08</div>
    <div class="tl-title">RoboPoint B-1 구현 & PoliFormer / SafeVLA</div>
    <div class="tl-tags">
      <span class="tl-tag tag-impl">구현</span>
      <span class="tl-tag tag-paper">논문</span>
    </div>
    <details>
      <summary>자세히 보기</summary>
      <div style="margin-top:10px">
        <div class="tl-section">
          <div class="tl-section-title">다룬 논문</div>
          <ul class="tl-ul">
            <li>PoliFormer: On-Policy RL + Transformer 기반 내비게이션 (CoRL 2024)</li>
            <li>SafeVLA: VLA 모델 안전 정렬 — Constrained Learning (NeurIPS 2025)</li>
          </ul>
        </div>
        <div class="tl-section">
          <div class="tl-section-title">구현 / 작업</div>
          <ul class="tl-ul">
            <li>RoboPoint를 B-1에 올려서 구현 시도</li>
            <li>RoboPoint API 로컬 실행 불가 → Gemini API + RoboPoint 데이터셋 결합 (RAG 활용)</li>
          </ul>
        </div>
        <div class="tl-note">VLM → VLA 전환은 token hijacking 방식(RT-2) — 잘 안 쓰이는 숫자 토큰을 action 토큰으로 덮어씀.</div>
      </div>
    </details>
  </div>
</div>

<!-- 11 -->
<div class="tl-item">
  <div class="tl-dot" style="background:#8aabde;border-color:#5c85d6"></div>
  <div class="tl-card">
    <div class="tl-date">2026.01.22</div>
    <div class="tl-title">논문 집중 탐독 (동적 메모리 & 멀티로봇)</div>
    <div class="tl-tags">
      <span class="tl-tag tag-paper">논문</span>
    </div>
    <details>
      <summary>자세히 보기</summary>
      <div style="margin-top:10px">
        <div class="tl-section">
          <div class="tl-section-title">다룬 논문</div>
          <ul class="tl-ul">
            <li>DynaMem: Voxel map 기반 동적 환경 메모리</li>
            <li>Belief Scene Graphs: 보이지 않는 물체 위치 확률적 추론 (heatmap)</li>
            <li>COHERENT: LLM 기반 이종 멀티로봇 협업 + Self Reflection</li>
            <li>DELTA: 분해형 장기 로봇 태스크 플래닝</li>
            <li>ConceptAgent: LLM Precondition Grounding + Tree Search</li>
          </ul>
        </div>
        <div class="tl-note">Belief Scene Graph는 이후 PRED 구현의 이론적 기반. DynaMem 한계: 실패율 높음, 복잡한 공간 관계 미지원.</div>
      </div>
    </details>
  </div>
</div>

<!-- 12 -->
<div class="tl-item">
  <div class="tl-dot" style="background:#6dc49a;border-color:#2e9e5e"></div>
  <div class="tl-card">
    <div class="tl-date">2026.02.05</div>
    <div class="tl-title">Isaac Sim 씬그래프 + LLM 로봇 제어 구현</div>
    <div class="tl-tags">
      <span class="tl-tag tag-impl">구현</span>
    </div>
    <details>
      <summary>자세히 보기</summary>
      <div style="margin-top:10px">
        <div class="tl-section">
          <div class="tl-section-title">구현 / 작업</div>
          <ul class="tl-ul">
            <li>ConceptGraph → 씬그래프 생성 → LLM 인식 → LLM 기반 로봇 제어 end-to-end 파이프라인 완성</li>
            <li>DELTA 구현 (GPT-4 → Gemini 변환), SayPlan 프롬프트 활용</li>
            <li>LLM + 3D Scene Graph 연동 및 long-term task 실행 성공</li>
          </ul>
        </div>
      </div>
    </details>
  </div>
</div>

<!-- 13 -->
<div class="tl-item">
  <div class="tl-dot" style="background:#e07060;border-color:#c0392b"></div>
  <div class="tl-card">
    <div class="tl-date">2026.02.19</div>
    <div class="tl-title">SayPlan 한계 분석 & 4가지 시나리오 직접 테스트</div>
    <div class="tl-tags">
      <span class="tl-tag tag-exp">실험</span>
      <span class="tl-tag tag-paper">논문</span>
    </div>
    <details>
      <summary>자세히 보기</summary>
      <div style="margin-top:10px">
        <div class="tl-section">
          <div class="tl-section-title">구현 / 작업</div>
          <ul class="tl-ul">
            <li>4가지 시나리오 직접 실험: 일반 복잡 task / 씬그래프 변화 / 씬에 없는 물체 / 동적 장애물</li>
            <li>nav2 기반 제어, Gemini 2.5 Flash Light 버전 사용</li>
          </ul>
        </div>
        <div class="tl-note">결과: 씬 변화 시 0/10, 씬에 없는 물체 5/10, 동적 장애물 6/10. 핵심 한계: Replanning과 Reflection 없음.</div>
      </div>
    </details>
  </div>
</div>

<!-- 14 -->
<div class="tl-item">
  <div class="tl-dot" style="background:#6dc49a;border-color:#2e9e5e"></div>
  <div class="tl-card">
    <div class="tl-date">2026.03.04</div>
    <div class="tl-title">REACT 씬그래프 업데이터 구현</div>
    <div class="tl-tags">
      <span class="tl-tag tag-impl">구현</span>
      <span class="tl-tag tag-paper">논문</span>
    </div>
    <details>
      <summary>자세히 보기</summary>
      <div style="margin-top:10px">
        <div class="tl-section">
          <div class="tl-section-title">다룬 논문</div>
          <ul class="tl-ul">
            <li>MM-3DSGU: Multi-Modal 3D Scene Graph Updater (CoRL 2024)</li>
            <li>REACT: Real-time Efficient Attribute Clustering & Transfer (IROS 2025)</li>
          </ul>
        </div>
        <div class="tl-section">
          <div class="tl-section-title">구현 / 작업</div>
          <ul class="tl-ul">
            <li>REACT 구현: SAM2 활용, 씬그래프 좌표를 이미지에 투영해 정확도 향상</li>
            <li>Qwen 2.5VL로 잘못 crop된 이미지 필터링</li>
            <li>테스트: 물체이동 10/10, 물체추가 8/10, 물체삭제 10/10</li>
          </ul>
        </div>
        <div class="tl-note">False positive 문제 발견 → Reflection 도입 필요성 확인.</div>
      </div>
    </details>
  </div>
</div>

<!-- 15 -->
<div class="tl-item">
  <div class="tl-dot" style="background:#e07060;border-color:#c0392b"></div>
  <div class="tl-card">
    <div class="tl-date">2026.03.17</div>
    <div class="tl-title">REACT + PRED 통합 구현 & SayPlan 3-way 비교</div>
    <div class="tl-tags">
      <span class="tl-tag tag-impl">구현</span>
      <span class="tl-tag tag-exp">실험</span>
      <span class="tl-tag tag-paper">논문</span>
    </div>
    <details>
      <summary>자세히 보기</summary>
      <div style="margin-top:10px">
        <div class="tl-section">
          <div class="tl-section-title">다룬 논문</div>
          <ul class="tl-ul">
            <li>ASHiTA: Automatic Scene-grounded Hierarchical Task Analysis (CVPR 2025)</li>
            <li>SAGE: Scene Graph-Aware Long-Horizon Manipulation (ICRA 2026 목표)</li>
            <li>MOMAGRAPH: VLM 기반 State-Aware Unified Scene Graph (ICLR 2026)</li>
            <li>COOPERA: Continual Open-Ended Human-Robot Assistance (NeurIPS 2025)</li>
          </ul>
        </div>
        <div class="tl-section">
          <div class="tl-section-title">구현 / 작업</div>
          <ul class="tl-ul">
            <li>REACT + PRED 통합 구현 (DTA, ASR 모듈 적용)</li>
            <li>씬그래프에 없는 물체 탐색 및 Replanning 구현</li>
          </ul>
        </div>
        <div class="tl-note">3-way 비교: SayPlan 씬 변화 0/10 → REACT 추가 10/10 → PRED+REACT 없는 물체 10/10. 남은 과제: 빈공간 관련 task 0/5.</div>
      </div>
    </details>
  </div>
</div>

<!-- 16 -->
<div class="tl-item">
  <div class="tl-dot" style="background:#6dc49a;border-color:#2e9e5e"></div>
  <div class="tl-card">
    <div class="tl-date">2026.03.31</div>
    <div class="tl-title">Freespace 구현 & Scene Graph 구조 확장</div>
    <div class="tl-tags">
      <span class="tl-tag tag-impl">구현</span>
    </div>
    <details>
      <summary>자세히 보기</summary>
      <div style="margin-top:10px">
        <div class="tl-section">
          <div class="tl-section-title">구현 / 작업</div>
          <ul class="tl-ul">
            <li>SceneGraph 구조 확장: obj + edge + free space + affordance</li>
            <li>오프라인 초기 freespace 계산 파이프라인 (포인트클라우드 Z축 분석)</li>
            <li>실시간 freespace 관리 (Depth → 3D pointcloud → YOLO → 2D grid map)</li>
            <li>Object Place 좌표 계산: Edge Safety / Object Safety / Efficiency 3기준</li>
            <li>Habitat Sim & Isaac Sim BEHAVIOR 환경 구축</li>
          </ul>
        </div>
        <div class="tl-note">성능: REACT 평균 50ms, freespace 추가 시 150ms. 빈공간 task 5/5, 씬에 없던 desk 등장 task 5/5. Habitat 넓은 씬에서 추가 검증 예정.</div>
      </div>
    </details>
  </div>
</div>

<!-- 17 -->
<div class="tl-item">
  <div class="tl-dot" style="background:#a78bfa;border-color:#7c3aed"></div>
  <div class="tl-card">
    <div class="tl-date">2026 ~ 2027</div>
    <div class="tl-title">시뮬레이터를 통한 데이터셋 생성 및 이미지 복구 기업과제 참여</div>
    <div class="tl-tags">
      <span class="tl-tag tag-corp">기업과제</span>
      <span class="tl-tag tag-impl">구현</span>
    </div>
    <details>
      <summary>자세히 보기</summary>
      <div style="margin-top:10px">
        <div class="tl-section">
          <div class="tl-section-title">과제 개요</div>
          <ul class="tl-ul">
            <li>시뮬레이터 환경(Isaac Sim / Habitat Sim)을 활용한 데이터셋 자동 생성</li>
            <li>생성된 데이터를 기반으로 이미지 복구(Image Restoration) 연구</li>
          </ul>
        </div>
        <!-- TODO: 기업 정보, 세부 내용 추가 -->
      </div>
    </details>
  </div>
</div>

</div>