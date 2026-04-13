---
title: "Profile"
layout: single
permalink: /profile/
---

<style>
/* 공통 카드 */
.pf-card {
  border: 1px solid #e8e8e8;
  border-radius: 8px;
  padding: 16px 18px;
  background: #fff;
  margin-bottom: 1rem;
}
.pf-card:hover { border-color: #aaa; }

/* 섹션 헤더 */
.pf-section-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 2rem 0 1rem;
}
.pf-section-header h2 {
  font-size: 1rem;
  font-weight: 700;
  color: #444;
  margin: 0;
  border: none;
}
.pf-section-header::after {
  content: '';
  flex: 1;
  height: 1px;
  background: #e0e0e0;
}

/* Affiliation */
.pf-affil {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 18px;
  background: #f8f8f8;
  border-radius: 8px;
  border-left: 4px solid #555;
  margin-bottom: 0.5rem;
}
.pf-affil-name { font-size: 0.95rem; font-weight: 700; color: #222; }
.pf-affil-loc { font-size: 0.78rem; color: #888; margin-top: 2px; }

/* Research 카드 */
.pf-lab-card {
  border: 1px solid #e8e8e8;
  border-radius: 8px;
  padding: 16px 18px;
  background: #fff;
  margin-bottom: 1rem;
}
.pf-lab-card:hover { border-color: #aaa; }
.pf-lab-title { font-size: 0.95rem; font-weight: 700; color: #222; margin-bottom: 4px; }
.pf-lab-period { font-size: 0.72rem; font-weight: 600; color: #888; margin-bottom: 10px; }
.pf-chips { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 10px; }
.pf-chip {
  font-size: 0.7rem;
  padding: 3px 10px;
  border-radius: 20px;
  font-weight: 600;
  background: #f0f0f0;
  color: #555;
}
.pf-chip-blue   { background: #e8f0fe; color: #1a56c4; }
.pf-chip-green  { background: #e6f4ea; color: #1a7a3c; }
.pf-chip-purple { background: #f3e8ff; color: #6d28d9; }
.pf-sub-title { font-size: 0.68rem; font-weight: 700; color: #888; text-transform: uppercase; letter-spacing: .06em; margin: 8px 0 4px; }
.pf-ul { list-style: none; padding: 0; margin: 0; }
.pf-ul li { font-size: 0.82rem; color: #444; padding: 2px 0 2px 12px; position: relative; line-height: 1.5; }
.pf-ul li::before { content: '·'; position: absolute; left: 0; color: #bbb; }

/* 기업과제 */
.pf-corp-card {
  border: 1px solid #e4d4ff;
  border-radius: 8px;
  padding: 14px 16px;
  background: #faf7ff;
  margin-bottom: 1rem;
}
.pf-corp-card:hover { border-color: #a78bfa; }

/* 수상/활동 카드 */
.pf-award-card {
  border: 1px solid #e8e8e8;
  border-radius: 8px;
  padding: 14px 18px;
  background: #fff;
  margin-bottom: 1rem;
}
.pf-award-card:hover { border-color: #aaa; }
.pf-award-title { font-size: 0.92rem; font-weight: 700; color: #222; margin-bottom: 2px; }
.pf-award-period { font-size: 0.72rem; font-weight: 600; color: #888; margin-bottom: 8px; }
.pf-award-item { font-size: 0.82rem; color: #444; padding: 3px 0 3px 12px; position: relative; line-height: 1.5; border-left: 2px solid #e0e0e0; margin-left: 4px; padding-left: 10px; margin-bottom: 4px; }
.pf-award-gold { border-left-color: #e6a817 !important; }
.pf-award-silver { border-left-color: #9e9e9e !important; }
.pf-award-entry { border-left-color: #90caf9 !important; }
</style>

<!-- Affiliation -->
<div class="pf-section-header"><h2>Affiliation</h2></div>

<div class="pf-affil">
  <div>
    <div class="pf-affil-name">{{ site.author.bio }}</div>
    <div class="pf-affil-loc">{{ site.author.location }}</div>
  </div>
</div>

<!-- Research Experience -->
<div class="pf-section-header"><h2>Research Experience</h2></div>

<div class="pf-lab-card">
  <div class="pf-lab-title">MAIRLab (Machine Artificial Intelligence Robotics Lab), Kookmin University</div>
  <div class="pf-lab-period">Undergraduate Researcher · 2025 ~ present</div>

  <div class="pf-sub-title">Research Topics</div>
  <div class="pf-chips">
    <span class="pf-chip pf-chip-blue">3D Scene Graph</span>
    <span class="pf-chip pf-chip-blue">Embodied AI</span>
    <span class="pf-chip pf-chip-green">Sim-to-Real</span>
  </div>

  <div class="pf-sub-title">Skills & Tools</div>
  <div class="pf-chips">
    <span class="pf-chip">ROS2</span>
    <span class="pf-chip">Isaac Sim</span>
    <span class="pf-chip">Habitat Sim</span>
  </div>
</div>

<div class="pf-corp-card">
  <div class="pf-lab-title">시뮬레이터를 통한 데이터셋 생성 및 이미지 복구</div>
  <div class="pf-lab-period">기업과제 (산학협력) · 2026 ~ 2027</div>
  <div class="pf-chips">
    <span class="pf-chip pf-chip-purple">기업과제</span>
    <span class="pf-chip pf-chip-green">구현</span>
  </div>
  <ul class="pf-ul">
    <li>시뮬레이터 환경(Isaac Sim / Habitat Sim)을 활용한 데이터셋 자동 생성</li>
    <li>생성된 데이터를 기반으로 이미지 복구(Image Restoration) 연구</li>
  </ul>
</div>

<!-- Awards & Activities -->
<div class="pf-section-header"><h2>Awards & Activities</h2></div>

<div class="pf-award-card">
  <div class="pf-award-title">FOSCAR — 국민대학교 소프트웨어학부 자율주행 동아리</div>
  <div class="pf-award-period">2024 ~ 2026</div>
  <div class="pf-award-item pf-award-gold">2025 대학생 창작 모빌리티 경진대회 무인 모빌리티 부문 <strong>설계부문 우수상</strong> — 한국자동차모빌리티안전학회</div>
</div>

<div class="pf-award-card">
  <div class="pf-award-title">KOBOT — 국민대학교 소프트웨어학부 로보틱스 동아리</div>
  <div class="pf-award-period">2021 ~ 2022</div>
  <div class="pf-award-item pf-award-silver">2022 로보컵 코리아 오픈 로보컵사커 휴머노이드 부문 <strong>3등</strong> — 한국 로보컵 협회</div>
</div>

<div class="pf-award-card">
  <div class="pf-award-title">LARES — 안양 중·고등학교 로봇 팀</div>
  <div class="pf-award-period">2015 ~ 2020</div>
  <div class="pf-award-item pf-award-gold">2017 RoboCup World Championship · Nagoya Japan — RoboCupJunior Soccer Lightweight Secondary SuperTeam <strong>World Champion</strong></div>
  <div class="pf-award-item pf-award-gold">2016 Korea Robot Championship FTC 부문 <strong>Inspired Award (1등)</strong></div>
  <div class="pf-award-item pf-award-entry">2019 RoboCup Asia Pacific · Russia Moscow — Soccer Lightweight 부문 참가</div>
  <div class="pf-award-item pf-award-entry">2016 First Tech Challenge World Championship 한국대표 참가</div>
</div>
