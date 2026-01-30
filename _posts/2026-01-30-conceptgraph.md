---
title: "Isaac Sim으로 데이터 수집 및 ConceptGraphs를 사용하여 3DSG 만들기"
categories:
  - isaacsim
tags:
  - Isaac Sim
  - Robotics
  - Data Generation
  - Scenegraph
  - 3DSG
---

Isaac Sim을 활용해 데이터셋을 구축하고, 이를 **ConceptGraphs**에 적용하여 3D Scene Graph(3DSG)를 생성하는 과정을 정리해 보겠습니다.

---

## 1. ConceptGraphs란 무엇인가?

**ConceptGraphs**는 로봇이 복잡한 3D 환경을 단순히 기하학적 구조(점구름, 메쉬)로만 보는 것이 아니라, **의미론적(Semantic)**으로 이해할 수 있도록 돕는 오픈 월드 3D Scene Graph 생성 프레임워크입니다.

전통적인 지도가 단순히 "여기에 벽이 있다"라고 말한다면, ConceptGraphs는 **"여기에 '검은색 사무용 의자'가 있고, 그 위에는 '노트북'이 놓여 있다"**는 객체 간의 관계성 데이터를 함께 제공합니다.

### 핵심 아키텍처 (Key Components)

1. **Multi-view Perception**: 여러 각도에서 촬영된 RGB-D 이미지를 입력 데이터로 사용합니다.
2. **2D Segmentation & Tagging**: SAM(Segment Anything Model)과 같은 모델을 활용하여 이미지 내 객체들을 정밀하게 분할합니다.
3. **Open-Vocabulary Feature**: CLIP 등의 모델을 이용해 각 객체의 시각적 특징을 벡터화합니다. 이를 통해 "빨간색 소파", "철제 선반" 등 학습 데이터에 없는 자연어 명칭으로도 객체를 검색할 수 있습니다.
4. **3D Incremental Mapping**: 각 프레임에서 추출된 2D 객체 정보를 3D 공간상에 투영하고 누적하여, 통합된 **객체 중심(Object-centric) 지도**를 생성합니다.
5. **LLM/VLM Integration**: 생성된 객체(Node)들의 정보를 Gemini나 GPT-4와 같은 대형 모델에 전달합니다. LLM은 각 객체의 위치와 클래스 정보를 바탕으로 "노트북-위-책상", "의자-옆-테이블"과 같은 공간적/의미적 관계를 추론하여 이를 **Edge(간선)** 형태로 연결합니다.

*추후 ConceptGraphs 논문에 대한 상세한 정리도 포스팅할 예정입니다.*

---

[Concept-Graphs GitHub 저장소](https://github.com/concept-graphs/concept-graphs/tree/ali_dev_new)

ConceptGraphs를 실행하기 위해서는 RGB-D 이미지와 더불어 카메라의 **Pose(위치 및 자세) 값**, 그리고 **카메라 정보(FOV, 중심점 등)**가 반드시 필요합니다.

이러한 데이터를 구하는 방법은 크게 어렵지 않습니다. 제가 작성한 [이전 글](https://leesb17.github.io/isaacsim/isaac-sim-data-precision/)을 참고하시면 상세한 가이드를 확인하실 수 있습니다.

이번 글에서는 이전 포스팅에서 다처 다루지 못했던, 데이터 생성 과정에서의 주요 **시행착오**들을 간단히 정리해 보려 합니다.

---

## 2. 주요 시행착오: Pose 데이터 관련 문제

{% include figure image_path="/assets/images/Screenshot from 2026-01-30 17-26-47.png" alt="Test Scene" caption="테스트를 진행한 Isaac Sim Scene" class="full" %}

### ❌ 문제 1: 월드 좌표계 고정 실패 (Relative Motion 문제)

Isaac Sim에서 추출한 Pose 값을 별도의 변환 없이 ConceptGraphs에 적용했을 때, 카메라의 움직임에 맞춰 월드 좌표계 전체가 함께 움직이는 현상이 발생했습니다.

- **증상**: 카메라가 전진하면 월드(지도)도 같이 전진하여, 결과적으로 로봇은 정지해 있고 배경이 움직이는 것처럼 처리되었습니다.
- **영향**: 3D Scene Graph 구축 시 동일한 객체임에도 불구하고 좌표가 중첩되지 않았습니다. 결과적으로 서로 다른 위치에 있는 별개의 물체로 인식되어 그래프가 비정상적으로 생성되었습니다.
- **원인 및 해결**: Isaac Sim의 월드 좌표계와 ConceptGraphs가 요구하는 카메라 좌표계(OpenCV 스타일) 사이의 변환 행렬이 일치하지 않아 발생한 문제였습니다. `convert_v2.py`에서 **Isaac Sim(Z-up) → OpenCV(Y-down, Z-forward)** 변환 로직을 정교화하여 해결할 수 있었습니다.

{% include figure image_path="/assets/images/Screenshot from 2026-01-30 17-26-56.png" alt="좌표계 변환 오류" caption="좌표계 변환이 이루어지지 않아 왜곡된 결과" class="full" %}

---

### ❌ 문제 2: 포인트클라우드 왜곡 (Object Smearing)

좌표계 변환을 마친 후에도 3D 포인트클라우드 상에서 물체가 실제보다 늘어지거나 '뚱뚱하게' 표현되는 왜곡 현상이 나타났습니다.

- **증상**: 고정된 사물의 형태가 뚜렷하지 않고 주행 방향을 따라 잔상이 남는 듯한 왜곡이 발생했습니다.
- **원인**: 실제 카메라가 렌더링되는 시점의 Pose와 파일로 저장되는 Pose 값 사이에 미세한 **시간차(Latency)** 또는 **정밀도 오차**가 누적되었기 때문입니다.
- **해결**: 이전 포스팅에서 언급한 것처럼, Isaac Sim의 물리 스텝과 렌더링 스텝을 동기화하고, Replicator의 **Annotator**를 통해 해당 프레임에 정확히 매칭되는 Pose 값을 추출함으로써 오차를 최소화했습니다. 시뮬레이터 상의 아주 작은 수치 차이가 3D 재구성(Reconstruction) 시에는 거대한 기하학적 왜곡으로 이어진다는 점을 배울 수 있었습니다.

{% include figure image_path="/assets/images/Screenshot from 2026-01-30 17-19-10.png" alt="물체 왜곡 현상" caption="오차 누적으로 인해 물체가 번져 보이는 결과" class="full" %}

---

## 3. 결과 및 Isaac Sim의 강점

{% include figure image_path="/assets/images/Screenshot from 2026-01-30 17-20-47.png" alt="최종 결과" caption="시행착오를 거쳐 해결한 최종 3D Reconstruction 결과" class="full" %}

최종 결과를 보시면 아시겠지만, 문제를 하나씩 해결할수록 3D 포인트클라우드가 실제 테스트 씬과 거의 유사하게 구축되는 것을 확인할 수 있습니다. 

이러한 과정 속에서 저는 **Isaac Sim의 진가**를 실감했습니다. 여러 논문을 접해보면 다양한 시뮬레이터가 활용되지만, 현실과의 괴리가 느껴지는 경우가 종종 있습니다. 반면, Isaac Sim은 실제 물리 환경과 가장 유사한 이미지를 제공해 줍니다.

제가 Isaac Sim을 선택한 가장 큰 이유이기도 한데, 로봇 연구에서 **Sim-to-Real(시뮬레이션에서 현실로의 전이)**은 매우 어려운 과제입니다. Isaac Sim을 능숙하게 다루는 것은 쉽지 않지만, 현실 환경과의 격차를 줄이는 데 있어 현존하는 시뮬레이터 중 가장 강력한 도구라고 생각합니다.