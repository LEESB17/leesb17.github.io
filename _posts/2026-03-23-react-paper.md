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
1. **문제 정의:** 자율 주행 로봇 등에서 3D Scene Graph (3DSG)가 메모리 효율과 풍부한 특징 표현으로 기존 그리드 맵의 대안으로 떠오르고 있으나, 대부분 정적(static) 환경에만 국한되어 사용되는 한계가 있었습니다. 로봇이 환경을 다시 방문했을 때 환경이 변해있으면 이전 3DSG의 노드에 내장된 풍부한 특징(VLM 등)들을 재사용하기 어렵습니다.

2. **해결 방법:** REACT라는 실시간 인스턴스 클러스터링 및 매칭 프레임워크를 제안합니다. 이 프레임워크는 동일한 객체 인스턴스들을 클러스터링하여 속성을 공유하고, triplet loss로 학습된 임베딩 모델을 통해 시각적으로 유사한 객체를 인식하여 장기적인 반정적(semi-static) 환경에서도 객체의 변화(이동, 추가, 삭제)를 실시간으로 감지하고 3DSG를 업데이트합니다.

3. **기여점:** 
   - Triplet loss로 학습된 효율적인 임베딩 모델을 활용해 시각적 유사성을 기반으로 객체를 구분하는 새로운 접근 방식을 제안했습니다. 
   - 속성(이미지, 3D 표현, 임베딩)을 공유하여 저장 공간과 연산량을 줄이는 인스턴스 클러스터링 기법을 도입했습니다. 
   - 로봇이 환경을 재방문할 때 실시간으로 누락되거나 새로운 객체를 감지하면서 3DSG의 노드를 효율적으로 재배치(relocalize)할 수 있게 하였습니다.

4. **한계점:** 
   - 분할(segmentation) 모델의 노이즈나 부정확한 깊이 데이터로 인해 단일 객체가 여러 노드로 분할되거나 인접한 객체가 병합되는 등 Scene Graph 구성 자체의 오류에 영향을 받습니다. 
   - 시각적 차이 임계값(visual difference threshold) 설정 시 파라미터 튜닝이 필요하며, 로봇의 첫 방문 시 임베딩 모델의 임시 학습(사전 훈련)이 요구됩니다.

---

#### [ 핵심 프로세스 ] 
{% include figure image_path="/assets/images/react/fig1.png" alt="REACT Pipeline" caption="Figure 1: REACT 파이프라인 개요" class="full" %}

1. **Attribute Clustering (속성 클러스터링)**
시각적으로 유사한 객체들(예: 같은 종류의 의자들)을 하나의 인스턴스 클러스터(Instance Cluster)로 묶습니다. 
- 이 클러스터링을 통해 동일한 객체 노드 간에 이미지, 포인트 클라우드, 시각적 임베딩과 같은 속성을 공유할 수 있어 연산 및 저장 공간의 부담을 줄일 수 있습니다.

2. **Triplet Network 기반 Embedding 학습 및 비교**
{% include figure image_path="/assets/images/react/fig2.png" alt="Online Matching Process" caption="Figure 2: 온라인 환경에서의 노드 임베딩 매칭 프로세스" class="full" %}

- **학습:** 초기 매핑 세션 이후, EfficientNet을 백본으로 하는 임베딩 모델을 Triplet Loss를 이용해 훈련시킵니다. 이를 통해 같은 종류 객체의 임베딩 거리는 가깝게, 다른 객체는 멀게 만듭니다.
- **적용:** 로봇이 다시 환경을 방문할 때 새로 생성된 객체 노드들의 임베딩 중앙값을 추출하여 이전 3DSG의 클러스터 임베딩과 유클리디안 거리를 비교(Visual difference)하여 유사도를 측정합니다.

3. **Instance Matching & Map Update (인스턴스 매칭 및 맵 업데이트)**
- 시각적 유사성을 바탕으로 클러스터들을 매칭한 후, 각 인스턴스들의 총 이동 거리를 최소화하는 방향으로 선형 할당 문제(Linear Sum Assignment)를 풀어 구체적인 개별 객체 매칭을 수행합니다.
- 매칭 결과를 토대로 위치만 바뀐 물체(Matched)의 위치를 갱신하고, 사라진 물체(Absent)는 그래프에서 제거하며, 새로 나타난 물체(New)는 추가하여 3DSG를 실시간으로 유지 및 보수합니다.

---

#### [ 결과 ]
{% include figure image_path="/assets/images/react/table1.png" alt="Dataset Description" caption="Table 1: 실험에 사용된 씬(Scene) 데이터셋 및 객체 구성" class="full" %}

{% include figure image_path="/assets/images/react/table2.png" alt="Change Detection Accuracy" caption="Table 2: 속성 클러스터링 적용 여부에 따른 변화 감지 정확도(F1-score) 비교" class="full" %}

{% include figure image_path="/assets/images/react/fig5.png" alt="Runtime of embedding model" caption="Figure 5: 프레임 당 인스턴스 마스크 수에 따른 임베딩 모델의 런타임 평가" class="full" %}

**결과 요약**
- **매칭 성능 (Change Detection Accuracy):** REACT는 속성 클러스터링을 적용하지 않은 그리디(Greedy) 방식의 베이스라인보다 더 일관되고 높은 성능(F1-score)을 기록했습니다. 특히 똑같이 생긴 유사한 객체가 밀집되어 있는 복잡한 공간(예: StudyHall)에서 클러스터링을 통한 매칭 오류(False Positive) 방지 효과가 돋보였습니다.
- **연산 속도 (Online Runtime):** 제안된 임베딩 비교 및 위치 기록 최적화 과정은 가벼운 연산으로 이루어져 있어, 온라인 구동 시에도 매핑 및 3DSG 생성 속도(약 3~4Hz)와 보조를 맞춰 실시간(Real-time)으로 3DSG를 업데이트하는 데 충분한 효율성을 보여주었습니다.
- **비교군 우위:** 기존 널리 쓰이는 특징 매칭 기법인 SuperGlue와 비교했을 때, REACT의 임베딩 모델은 객체를 식별하는 정확도(F1-score 0.98 vs 0.71)와 처리 속도면에서 모두 뛰어난 우위를 점했습니다.
