---
title: "[논문리뷰] REACT: Real-time Efficient Attribute Clustering and Transfer for Updatable 3D Scene Graph"
categories:
  - Paper
tags:
  - Robotics
  - SceneGraph
  - 3DSG
math: true
---

## REACT: Real-time Efficient Attribute Clustering and Transfer for Updatable 3D Scene Graph

#### [ 논문 간단 요약 ]
1. **문제 정의:** 자율 주행 로봇 등이 활용하는 3D Scene Graph (3DSG)는 메모리 효율이 좋고 의미론적(Semantic) 특징을 포함하여 최근 각광받고 있습니다. 하지만 대부분 정적(Static) 환경을 가정하고 구축되어, 환경이 변했을 때(물체가 이동하거나 추가/삭제됨) 이전 3DSG 노드에 내장된 풍부한 정보(VLM 임베딩 등)를 재사용하지 못하고 처음부터 다시 계산해야 하는 한계가 존재합니다.

2. **해결 방법:** 이를 해결하기 위해 로봇이 재방문한 환경에서 빠르고 효율적으로 변화를 감지하고 3DSG를 갱신할 수 있는 **REACT(Real-time Efficient Attribute Clustering and Transfer)** 프레임워크를 제안합니다. 외형이 같은 인스턴스(객체)들을 클러스터링하여 속성을 공유하고, Triplet Network 기반의 임베딩 모델로 시각적 유사성을 평가해 객체 간 매칭을 실시간으로 수행합니다.

3. **기여점:** 
   - **효율적인 인스턴스 인식:** Triplet loss로 학습된 경량화된 임베딩 모델(EfficientNet 기반)을 활용하여, 시각적으로 유사한 객체들을 빠르고 정확하게 구분하는 방법을 제시했습니다.
   - **속성 클러스터링 도입:** 외형이 동일한 객체들(예: 같은 디자인의 의자들)을 묶어 이미지, 3D 구조, 임베딩을 하나로 공유함으로써 메모리와 연산량을 크게 감축시켰습니다.
   - **실시간 유지보수:** 새롭게 추가된 물체(New), 사라진 물체(Absent), 이동한 물체(Matched)를 실시간으로 분류하여 3DSG의 노드들을 효율적으로 업데이트하고 재배치(relocalize)할 수 있습니다.

4. **한계점:** 
   - **전처리 의존성:** 2D Instance Segmentation 모델의 노이즈나 부정확한 센서의 깊이 맵으로 인해 단일 객체가 분할되거나 인접한 두 객체가 병합되는 등 Scene Graph 초기 생성 오류에 취약합니다.
   - **사전 훈련 필요성:** 시각적 차이를 판단하는 임계값(visual difference threshold, $\gamma$) 파라미터 튜닝이 필요하며, 특정 씬에 대해 로봇이 처음 방문했을 때 수집한 이미지로 임베딩 모델을 별도로 학습시켜야 하는 제약이 있습니다.

---

#### [ 핵심 프로세스 ] 
{% include figure image_path="/assets/images/react/fig1.png" alt="REACT Pipeline" caption="Figure 1: REACT 파이프라인 개요" class="full" %}

1. **Attribute Clustering (속성 클러스터링)**
환경에는 완전히 동일하게 생긴 객체들(예: 회의실의 의자들)이 다수 존재합니다. 이들을 개별적으로 비교하는 대신, 시각적으로 유사한 객체들을 모아 하나의 인스턴스 클러스터(Instance Cluster)로 묶습니다.
- **세부 프로세스:**
  - 객체의 위치나 가려짐(occlusion)에 관계없이 통합된 특징을 얻기 위해 각 뷰(view)의 시각적 임베딩을 평균화(Average)합니다.
  - 클러스터 내의 객체들은 Semantic class, 다각도의 RGB 이미지 라이브러리, 3D 형태 정보 및 특징 임베딩을 모두 공유합니다.

2. **Triplet Network 기반 Embedding 학습 및 비교**
{% include figure image_path="/assets/images/react/fig2.png" alt="Online Matching Process" caption="Figure 2: 온라인 환경에서의 노드 임베딩 매칭 프로세스" class="full" %}

- **세부 프로세스:**
  - **모델 구조 & 학습:** FaceNet의 파이프라인을 차용하여 EfficientNet을 백본으로 사용합니다. 로봇의 첫 매핑 세션 후 확보한 이미지를 바탕으로 Triplet Loss $L = \sum (\|f_a - f_p\|^2_2 - \|f_a - f_n\|^2_2 + \alpha)$ 를 최적화하여 30 Epoch 동안 학습합니다. 이는 앵커(Anchor) 대비 동일 객체(Positive)의 유클리디안 거리를 좁히고 다른 객체(Negative)의 거리를 벌리는 과정입니다.
  - **Online Embedding Query:** 온라인 주행 중 로봇이 새로운 객체 노드를 형성하면 쿼리 가능한 임베딩 라이브러리(Embedding Library, $E$)에서 시각적 임베딩을 추출해 중앙값을 가져옵니다.
  - **클러스터 매칭:** 추출된 임베딩 $f_k$와 이전 3DSG 클러스터의 임베딩 $f_l$ 사이의 거리 $V(C_k, C_l) = \|f_k - f_l\|^2_2$ 가 임계값 $\gamma$ 이하인지를 판별하여 시각적 유사도 매칭을 수행합니다.

3. **Instance Matching & Map Update (인스턴스 매칭 및 맵 최적화)**
시각적으로 클러스터 간의 매칭이 이루어졌다면, 각 클러스터에 속한 개별 객체들이 정확히 어디로 이동했는지를 유추해야 합니다.
- **세부 프로세스:**
  - **거리 최소화:** 반정적(semi-static) 객체는 위치가 크게 변하지 않는다는 점에 착안하여, 모든 매칭된 인스턴스들의 총 물리적 이동 거리 합이 최소화되도록 Jonker-Volgenant 알고리즘(Linear Sum Assignment 문제)을 이용해 최적화 수식을 풉니다.
  - **3DSG Update:** 최종 산출된 결과에 따라 이동한 객체는 위치를 갱신(Matched)하고, 과거에 있던 객체 중 현재 없는 것은 삭제(Absent), 새롭게 발견된 것은 추가(New)하여 Scene Graph 노드 관계를 업데이트합니다.

---

#### [ 결과 ]
{% include figure image_path="/assets/images/react/table1.png" alt="Dataset Description" caption="Table 1: 실험에 사용된 씬(Scene) 데이터셋 및 객체 구성" class="full" %}

{% include figure image_path="/assets/images/react/table2.png" alt="Change Detection Accuracy" caption="Table 2: 속성 클러스터링 적용 여부에 따른 변화 감지 정확도(F1-score) 비교" class="full" %}

{% include figure image_path="/assets/images/react/fig5.png" alt="Runtime of embedding model" caption="Figure 5: 프레임 당 인스턴스 마스크 수에 따른 임베딩 모델의 런타임 평가" class="full" %}

**결과 요약 (주요 수치 및 모듈별 영향)**

- **Table 2 결과 요약 (매칭 성능 및 클러스터링 효과):** 
  - **성능 지표:** 클러스터링을 적용한 REACT는 비교군(w/o clustering, 그리디 매칭) 대비 모든 환경에서 동일하거나 우월한 F1-score(Matched 1.0, New 1.0, Absent 1.0)를 기록했습니다.
  - **대규모 환경 입증:** 동일한 형태의 의자와 테이블이 매우 밀집된 StudyHall(의자 약 33개, 테이블 11개)의 경우 클러스터링이 없으면 오매칭(False Positive)으로 인해 정확도가 $F1_M$ 0.98, $F1_A$ 0.86으로 크게 하락합니다.
  - **이동 거리 최적화:** 최적의 매칭을 수행한 REACT는 전체 객체 이동 거리($P_{D}$)가 6.56m로 나타난 반면, 클러스터링을 배제한 베이스라인은 45.26m로 측정되어 불필요하게 물체가 멀리 '점프'한 것으로 잘못 인식하는 문제를 방지함을 확인했습니다.

- **Table 3 결과 요약 (학습된 임베딩 모델 비교군 우위):**
  - 기존 널리 쓰이는 특징 매칭 알고리즘인 SuperGlue(배경 마스크 적용)와 비교했을 때, REACT의 임베딩 모델은 Precision 0.97, Recall 0.98로 F1-score 0.98을 달성했습니다 (SuperGlue는 0.71).
  - 연산 속도 측면에서도 REACT는 평균 FPS 86.99로 압도적인 성능을 내며 실시간성에 유리함을 보였습니다.

- **Figure 5 결과 요약 (온라인 구동 속도):**
  - 제안된 임베딩 모델(EfficientNet-B2 기반)은 이미지 프레임 당 여러 개의 마스크가 존재할 때 마스크당 약 11ms를 소요합니다.
  - 임베딩 매칭 및 위치 최적화는 대부분 CPU 기반 가벼운 연산이므로, 로봇이 맵을 탐색할 때의 3DSG 생성 평균 속도인 3~4Hz 프레임레이트를 충분히 소화해내며 병목현상 없이 실시간 갱신(Online Runtime)이 가능함을 입증했습니다.
