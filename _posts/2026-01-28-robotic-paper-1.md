---
title: "[논문리뷰] Interaction-Driven Updates: 3D Scene Graph Maintenance During Robot Task Execution"
categories:
  - Paper
tags:
  - ICRA2025
  - Robotics
  - SceneGraph
math: true
---

## Interaction-Driven Updates: 3D Scene Graph Maintenance During Robot Task Execution

#### [ 논문 간단 요약 ]
1. **문제 정의:** 기존 로봇 시스템은 작업 수행 시 미리 구축된 정적인 (Static) 장면 정보에만 의존하는 경향이 있습니다. 이로 인해 작업 도중 물체의 위치가 바뀌거나 환경이 변하는 동적인 (Dynamic) 상황이 발생하면 로봇이 이에 적절히 대응하지 못하고 작업에 실패하는 문제가 발생 합니다.

2. **해결 방법:** 로봇이 환경과 직접 상호작용하며 정보를 갱신하는 상호작용 기반 (Interaction-driven) 업데이트 방식을 제안 합니다. 이를 위해 최적의 시야를 확보하는 관측 지점 선택 모듈 과 실시간으로 변화를 감지하여 3D 장면 그래프를 갱신하는 동적 장면 유지 관리 모듈 을 결합하여 시스템을 구축 하였습니다.

3. **기여점:** 첫째, 효율적인 환경 인식을 위해 각 객체를 바라보는 최적의 위치 (Observation Point) 를 선정하는 알고리즘을 제시 하였습니다. 둘째, LLM 과 3D 장면 그래프를 연동하여 실시간으로 변화하는 환경 정보를 지속적으로 유지 및 보수 할 수 있는 프레임워크를 개발하여 로봇의 작업 성공률을 높였습니다.

4. **한계점:** 논문의 실험 환경을 넘어선 매우 복잡하거나 극도로 혼잡한 (Highly cluttered) 환경에서의 실시간 연산 효율성에 대한 추가 검증이 필요할 수 있습니다. 또한, 상호작용 과정에서 발생하는 물리적 제약이나 예기치 못한 센서 노이즈 가 데이터 갱신 정확도에 미치는 영향에 대해 더욱 심도 있는 연구가 요구 됩니다.


#### [ 핵심 프로세스 ] 
{% include figure image_path="/assets/images/robotic-paper-screenshot.png" alt="로보틱스 페이퍼 스크린샷" caption="figure2" class="full" %}

1. **Observation Points Selection Module (좌측 파란색 박스)**
특정 작업 지침을 생성하기 전에, 각 자산 주변에 여러 관측 지점이 생성됩니다. 각 자산에 대한 최적의 관측 지점은 다양한 점에서 이미지 정보를 분석하여 결정됩니다.

세부 프로세스
- **Candidate Generation:** 자산 주변에 충돌이 없는 안전한 관측 후보 지점들을 생성합니다.

- **BLIP-2 & Cosine Similarity:** 각 지점에서 찍은 RGB 이미지 와 3DSG의 텍스트 정보를 BLIP-2 모델에 입력합니다.

- **Value Generate Module:** 이미지와 텍스트 사이의 코사인 유사도 를 계산하여, 자산이 가장 명확하게 식별되는 지점을 Best Observation Point 로 최종 선택합니다.

2. **LLM Planner & Action Sequences (상단 검은색 박스)**
로봇은 LLM 분석을 통해 구체적이고 실행 가능한 동작 시퀀스를 얻으며, 우리의 장면 정보 업데이트 프로세스는 동작 서브태스크의 일부입니다.

세부 프로세스
- 사용자의 명령(Prompt)을 받으면, LLM은 {goto: observation point}와 {collect: scene info} 같은 세부 단계를 실행 계획(Action Sequences)에 포함시킵니다.

3. **Dynamic Scene Maintenance Module (우측/하단 노란색 박스)**
물체 변화가 감지되면, 관측 지점에서 얻은 이미지 정보가 자산 위의 모든 물체에 대한 최신 정보를 업데이트하는 데 사용됩니다. 이 정보는 이후 3DSG에 통합됩니다.

세부 프로세스
- **Change Detection Module:** 이전 시점의 이미지($Image_{t-1}$)와 현재 이미지($Image_t$)를 비교하여 변화를 감지합니다.

- **Add/Reduce:** 물체가 새로 생겼는지(Add) 혹은 사라졌는지(Reduce)를 시각적으로 파악합니다.

- **Update 3DSG:** 변화된 내용을 바탕으로 3D Scene Graph 의 노드와 연결 관계를 즉시 갱신합니다.

#### [ 결과 ]
{% include figure image_path="Screenshot from 2026-01-30 13-19-27.png" alt="로보틱스 페이퍼 스크린샷" caption="table I" class="full" %}

{% include figure image_path="Screenshot from 2026-01-30 13-19-17.png" alt="로보틱스 페이퍼 스크린샷" caption="table III" class="full" %}

**Table 1 결과 요약 (주요 수치)**
- **성능 지표:** NRA (노드 인식 정확도) 평균 88.48%, ERA (엣지 인식 정확도) 평균 86.34%, WJS (가중 자카드 유사도) 평균 95.04% 를 기록했습니다. 

- **환경 적응성:** 실제 방(room 1, 2, 3)과 시뮬레이션 환경(floorplan) 모두에서 WJS 가 94% 이상을 유지하며 매우 높은 일관성을 보였습니다. 

- **한계 발견:** 열쇠, 숟가락, 펜과 같은 작은 물체들은 카메라 해상도의 한계로 인해 일부 환각(NHP) 현상이 발생하기도 했습니다.

**Table 3 결과 요약 (모듈별 영향)**
- **Ours (전체 시스템):** NRA 88.48%, WJS 95.04% 로 최고의 성능을 보입니다. 

- **w/o Dynamic Scene Maintenance (동적 유지 모듈 제거):** NRA 가 68.93% 로 급격히 떨어집니다. 이는 단순히 사진을 찍는 것보다 VLM을 통한 4단계 업데이트 과정이 정보의 정확성을 높이는 데 핵심적임을 보여줍니다. 

- **w/o Observation Point Selection (관측 지점 선택 제거):** 최적의 위치를 찾지 않고 랜덤한 지점에서 관측할 경우 NRA 가 74.62% 로 하락합니다. 이는 물체를 잘 볼 수 있는 '각도'를 선정하는 것이 인식 성능에 큰 영향을 미친다는 증거입니다.

