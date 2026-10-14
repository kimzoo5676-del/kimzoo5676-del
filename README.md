![header](https://capsule-render.vercel.app/api?type=soft&color=660033&height=200&section=header&text=joowoo%27s%20github&fontSize=40&fontColor=ffffff&fontAlignY=38&animation=fadeIn&desc=Backend%20Developer&descSize=16&descAlignY=65)

<p align="center">
  <a href="https://kimzoo5676-del.github.io/">
    <img src="https://img.shields.io/badge/Portfolio-660033?style=for-the-badge&logo=githubpages&logoColor=white" alt="Portfolio"/>
  </a>
  <a href="https://velog.io/@zooouu/posts">
    <img src="https://img.shields.io/badge/Velog-20C997?style=for-the-badge&logo=velog&logoColor=white" alt="Velog"/>
  </a>
  <a href="mailto:kimzoo5676@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"/>
  </a>
</p>

---

## 📚 Education

| 기간 | 소속 |
|------|------|
| 2019.03 - 2025.08 | 한양대학교 ERICA 경제학부 |
| 2026.01 - | 삼성청년SW·AI아카데미 SSAFY 15기 |

---

## 🚀 Projects

### 📱 모디 (MODI) — 팀 목표 협업 앱 &nbsp;`2026.07 -`

<p>
  <a href="https://apps.apple.com/kr/app/id6801031228">
    <img src="https://img.shields.io/badge/App%20Store-0D96F6?style=for-the-badge&logo=appstore&logoColor=white" alt="App Store"/>
  </a>
  <a href="https://maramodi.cloud/">
    <img src="https://img.shields.io/badge/Website-660033?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Website"/>
  </a>
  <a href="https://github.com/intpsquad/modi">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  </a>
</p>

> 방을 만들어 팀이 **목표 기간 동안 할일·일정·자료를 공유하고 서로 독려**하는 iOS 협업 앱.
> **App Store 정식 출시 후 실사용자를 받으며 운영 중.**

**Role** · Backend / Infra / AI &nbsp;&nbsp;|&nbsp;&nbsp; `Spring Boot` `FastAPI` `PostgreSQL` `Redis` `Docker` `GitHub Actions` `Oracle Cloud`


- **인프라·배포** — Oracle Cloud(ARM)로 서버 이관, Blue/Green 무중단 배포와 자동 롤백 구성
- **AI 투두 추천 서버** — FastAPI + LangGraph 파이프라인(자료 선별 → 후보 생성 → 의미 중복 제거) 개발
- **iOS 릴리스** — TestFlight 배포와 App Store 심사 제출까지 담당


<br>

### 🌌 Zoolog — 공부 기록 그래프 블로그 &nbsp;`2026.10 -`

<p>
  <a href="https://zoolog.site/">
    <img src="https://img.shields.io/badge/Website-660033?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Website"/>
  </a>
  <a href="https://github.com/kimzoo5676-del/Zoolog">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  </a>
</p>

> 공부 글을 주제 3단계로 정리해 **별자리 그래프로 보여 주고, 글 쓴 날을 주제별 달력에 쌓아 가는** 개인 블로그.
> **기획 · 디자인 · 백엔드 · 프론트 · 인프라를 혼자 만들어 https://zoolog.site 에서 운영 중.**

**Role** · 1인 개발 (Infra / Backend / Frontend) &nbsp;&nbsp;|&nbsp;&nbsp; `Spring Boot` `PostgreSQL` `React` `TypeScript` `k3s` `Argo CD` `GitHub Actions` `Caddy` `AWS Lightsail`

- **GitOps 배포** — GitHub Actions(통합 테스트 → 이미지 빌드 → 매니페스트 태그 커밋) + Argo CD로 push만으로 k3s에 반영, `git revert`로 되돌리기
- **2GB 서버 운영 설계** — 컨테이너별 메모리 상한과 Argo CD core 설치로 서버 1대에 구성, 화면 서버 RollingUpdate로 배포 중 응답 실패 0회(1초 간격 측정)
- **아침 기사 메일 · 뉴스 스크랩** — Google 뉴스 RSS · 네이버 검색으로 후보를 모아 규칙 기반 선정, 못 보낸 날 재발송, 메일 링크로 코멘트를 달면 블로그 글로 게시(같은 기사 중복 방지)
- **그래프 홈** — 힘 기반 배치(force-directed)로 수백 개 글도 겹치지 않는 별자리 그래프, View Transition으로 화면 사이 제목이 이어지는 전환


<br>

### 🏦 여보 (여신보좌관) — 기업여신 AI 업무 보조 서비스 &nbsp;`2026.08 - 2026.09`

<p>
  <a href="https://github.com/kimzoo5676-del/loanreview/blob/main/docs/presentation/yeobo-presentation.pdf">
    <img src="https://img.shields.io/badge/Slides-660033?style=for-the-badge&logo=googleslides&logoColor=white" alt="Slides"/>
  </a>
  <a href="https://github.com/kimzoo5676-del/loanreview">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  </a>
</p>

> 은행 심사 담당자가 스타트업 법인의 서류 10종을 심사할 때 **서류 판독 → 서류 간 대조 → 위험 점검 → 등급·한도 → 심사의견서 초고**까지 보조하는 AI 서비스.
> **계산은 규칙이, 설명과 초고는 AI 가, 판단·확정은 담당자가.** SSAFY 2학기 프로젝트 · 5인 팀.

**Role** · Infra / Backend &nbsp;&nbsp;|&nbsp;&nbsp; `Spring Boot` `Spring Security` `PostgreSQL` `Docker Swarm` `Jenkins` `GitLab CI` `Prometheus` `Grafana` `AWS Lightsail`

- **무중단 배포·CI/CD** — Docker Swarm start-first 무중단 배포, Jenkins 자동 배포와 되돌리기, GitLab Runner CI 게이트(포맷·린트·테스트·빌드·시크릿 스캔)
- **관측** — Prometheus·Loki·Grafana 로 지표와 컨테이너 로그를 모아 운영 대시보드 구성
- **로그인·접근 제어** — SSAFY 통합인증 + DB 세션 + CSRF + TOTP 2차 인증, 담당자별 접근 제어와 감사부 열람
- **감사 로그** — SHA-256 해시 체인 · DB 권한 분리 · 트리거로 수정·삭제를 막고, 체인 검증 API 로 변조 위치를 찾음


<br>

### 💰 OURWISH — 사회초년생을 위한 예·적금 추천 서비스 &nbsp;`2026.05 - 2026.06`

<p>
  <a href="https://our-wish.site/">
    <img src="https://img.shields.io/badge/Website-660033?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Website"/>
  </a>
  <a href="https://github.com/Our-Wish/ourwish">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  </a>
</p>

> 생성형 AI와 금융 데이터를 활용해 사용자에게 맞는 예·적금 상품을 추천하는 로보 어드바이저 서비스.
> **SSAFY 1학기 관통 프로젝트 최우수상 (서울2반 1등).**

**Role** · Backend / AI &nbsp;&nbsp;|&nbsp;&nbsp; `Django` `DRF` `Vue.js` `SQLite` `AWS EC2`

- **REST API·DB 설계** — DRF로 REST API와 JWT 인증 구현, 회원·상품·가입·찜·커뮤니티 5개 도메인 ERD 모델링
- **추천 알고리즘** — 금융감독원(FSS) API로 예·적금 상품 766건 수집, 프로필 기반 필터링 + 세후 실수령액 계산·정렬로 추천 구현
- **LLM 연동 3종** — 우대조건을 8개 표준 태그로 배치 구조화 · 약관 쉬운 말 요약 · 상품 데이터로 근거를 한정한 스트리밍 챗봇. 우대조건은 미리 가공해 두어 추천은 DB 쿼리만으로 즉시 응답
- **배포** — GitHub Actions로 CI/CD를 구성하고 AWS EC2(Nginx·Gunicorn)에 배포 후 도메인 연결

---

## 🏆 Awards

| 날짜 | 수상 내역 |
|:---:|:---|
| `2026.07` | 삼성청년SW·AI아카데미 **SSAFY Race 대회 2위**<br>Microsoft AirSim 기반 주행 봇 타임어택 — SSAFY 트랙 레이싱 라인·장애물 회피 최적화 |
| `2026.06` | 삼성청년SW·AI아카데미 1학기 관통 프로젝트 **최우수상** (서울2반 1등)<br>**OURWISH** — 생성형 AI와 금융 데이터를 활용한 금융 상품 로보 어드바이저 서비스 |

---

## 🛠 Tech Stack

**Language**  
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Java](https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=openjdk&logoColor=white)

**Backend**  
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-A30000?style=for-the-badge&logo=django&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white)
![Spring Security](https://img.shields.io/badge/Spring%20Security-6DB33F?style=for-the-badge&logo=springsecurity&logoColor=white)
![Spring Data JPA](https://img.shields.io/badge/Spring%20Data%20JPA-6DB33F?style=for-the-badge&logo=spring&logoColor=white)
![Spring Session](https://img.shields.io/badge/Spring%20Session-6DB33F?style=for-the-badge&logo=spring&logoColor=white)

**AI**  
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logoColor=white)

**Frontend**  
![Vue.js](https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)

**Database & Storage**  
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-FF4438?style=for-the-badge&logo=redis&logoColor=white)
![MinIO](https://img.shields.io/badge/MinIO-C72E49?style=for-the-badge&logo=minio&logoColor=white)
![Flyway](https://img.shields.io/badge/Flyway-CC0200?style=for-the-badge&logo=flyway&logoColor=white)

**Infra & Cloud**  
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Docker Swarm](https://img.shields.io/badge/Docker%20Swarm-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![K3s](https://img.shields.io/badge/K3s-FFC61C?style=for-the-badge&logo=k3s&logoColor=black)
![Argo CD](https://img.shields.io/badge/Argo%20CD-EF7B4D?style=for-the-badge&logo=argo&logoColor=white)
![AWS EC2](https://img.shields.io/badge/AWS%20EC2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white)
![AWS Lightsail](https://img.shields.io/badge/AWS%20Lightsail-FF9900?style=for-the-badge&logoColor=white)
![Oracle Cloud](https://img.shields.io/badge/Oracle%20Cloud-F80000?style=for-the-badge&logo=oracle&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![GitLab CI](https://img.shields.io/badge/GitLab%20CI-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![Caddy](https://img.shields.io/badge/Caddy-1F88C0?style=for-the-badge&logo=caddy&logoColor=white)
![Tailscale](https://img.shields.io/badge/Tailscale-242424?style=for-the-badge&logo=tailscale&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-DD2C00?style=for-the-badge&logo=firebase&logoColor=white)

**Monitoring**  
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![Loki](https://img.shields.io/badge/Loki-F46800?style=for-the-badge&logo=grafana&logoColor=white)

**Tools**  
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![GitLab](https://img.shields.io/badge/GitLab-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white)
![Jira](https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=jira&logoColor=white)
