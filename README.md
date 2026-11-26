![header](https://capsule-render.vercel.app/api?type=soft&color=660033&height=200&section=header&text=joowoo%27s%20github&fontSize=40&fontColor=ffffff&fontAlignY=38&animation=fadeIn&desc=Infra%20%C2%B7%20Backend&descSize=16&descAlignY=65)

<p align="center">
  <a href="https://kimzoo5676-del.github.io/">
    <img src="https://img.shields.io/badge/Portfolio-660033?style=for-the-badge&logo=githubpages&logoColor=white" alt="Portfolio"/>
  </a>
  <a href="https://github.com/kimzoo5676-del/kimzoo5676-del.github.io/raw/main/pdf/kimjoowoo-infra-portfolio.pdf">
    <img src="https://img.shields.io/badge/Cloud%20Engineer%20Portfolio%20PDF-800020?style=for-the-badge&logo=files&logoColor=white" alt="Cloud Engineer Portfolio PDF"/>
  </a>
  <a href="https://github.com/kimzoo5676-del/kimzoo5676-del.github.io/raw/main/pdf/kimjoowoo-sw-portfolio.pdf">
    <img src="https://img.shields.io/badge/SW%20Portfolio%20PDF-800020?style=for-the-badge&logo=files&logoColor=white" alt="SW Portfolio PDF"/>
  </a>
  <a href="https://velog.io/@zooouu/posts">
    <img src="https://img.shields.io/badge/Velog-20C997?style=for-the-badge&logo=velog&logoColor=white" alt="Velog"/>
  </a>
  <a href="https://zoolog.site/">
    <img src="https://img.shields.io/badge/Zoolog-660033?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Zoolog"/>
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

### 📰 NEW:LEARN — 기사 이슈 타임라인 · 기사 마인드맵 AI 플랫폼 &nbsp;`2026.10 - 2026.11`

<p>
  <a href="https://newlearn.io.kr">
    <img src="https://img.shields.io/badge/Website-660033?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Website"/>
  </a>
  <a href="https://newlearn-issue.vercel.app/home">
    <img src="https://img.shields.io/badge/Demo-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Demo"/>
  </a>
  <a href="https://github.com/a102-NEWLEARN/NEW-LEARN">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  </a>
</p>

> 뉴스를 AI로 구조화해 **사건과 이슈의 흐름**으로 보여 주는 서비스.
> SSAFY 2학기 프로젝트 · 6인 팀.

**Role** · Infra · BE &nbsp;&nbsp;|&nbsp;&nbsp; `Spring Boot` `PostgreSQL` `Redis` `Kubernetes(kubeadm)` `Argo CD` `GitLab CI` `Terraform` `Prometheus` `Grafana` `AWS`

- **클러스터 구성** — 서버 2대를 WireGuard로 연결해 kubeadm 클러스터 하나로 운영, EC2 · 보안 그룹 · 백업 S3 버킷은 Terraform으로 관리
- **GitOps 배포** — MR 검사 → 이미지 빌드(Kaniko) → 배포 태그 MR → Argo CD 동기화, 롤백은 `git revert`
- **분석 작업 파이프라인** — 기사 분석을 Redis Streams 작업 큐로 API 응답과 분리, 동일 사건 판정은 PostgreSQL advisory lock으로 직렬화
- **기사 수집 · 적재** — 15분 주기 CronJob으로 뉴스 API 수집(중복 주소 제외), 기존 기사 79,335건은 카나리 100건 후 전체 적재
- **조회 성능** — 공개 기사 부분 인덱스로 기사 목록 p50 242ms → 22ms, 부하 테스트 포화 처리량 초당 93건 → 123건
- **묶기 정확도 평가** — 정답 라벨이 없는 사건 · 이슈 묶음을 LLM 채점과 사람 검수 200건으로 평가(B³ F1 사건 0.854 · 이슈 0.926)

<br>

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

> 방을 만들어 팀이 **목표 기간 동안 할 일 · 일정 · 자료를 공유**하는 iOS 협업 앱.
> App Store 출시 후 운영 중.

**Role** · Infra · AI &nbsp;&nbsp;|&nbsp;&nbsp; `Spring Boot` `FastAPI` `PostgreSQL` `Redis` `Docker` `GitHub Actions` `Caddy` `Oracle Cloud`


- **CI/CD** — Oracle Cloud(ARM) 이관과 함께 GitHub Actions 워크플로로 재구성, 테스트를 통과한 코드만 배포
- **blue/green 배포** — 새 버전이 헬스체크를 통과한 뒤 Caddy로 트래픽 전환, 이전 버전 컨테이너는 롤백용으로 유지
- **백업 · 복구** — PostgreSQL과 파일 저장소(MinIO)를 매일 백업, 임시 컨테이너 복구로 테이블 20개 행 수 일치 확인
- **크롤링 파이프라인** — 링크 등록은 접수만 하고 크롤링 · 요약은 비동기 처리, 사이트별 크롤러와 재시도 정책, 등록 시점 주소 검증
- **AI 할 일 추천** — 방에 모인 자료로 할 일 후보를 만드는 FastAPI 서버, 평가 러너로 변경마다 측정해 LLM 1회 호출 구조로 정리
- **iOS 릴리스** — TestFlight 배포와 App Store 심사 제출


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

> 공부한 글을 **주제별 그래프와 달력**으로 정리하는 개인 기술 블로그.
> 2026.10부터 운영 중.

**Role** · Infra · Full-Stack &nbsp;&nbsp;|&nbsp;&nbsp; `Spring Boot` `PostgreSQL` `React` `TypeScript` `k3s` `Argo CD` `GitHub Actions` `Caddy` `AWS Lightsail`

- **GitOps 배포** — GitHub Actions(통합 테스트 → 이미지 빌드 → 매니페스트 태그 커밋)와 Argo CD로 k3s에 배포, 롤백은 `git revert`


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

> 은행 심사 담당자가 스타트업 법인의 서류 10종을 심사할 때 **서류 판독 → 서류 간 대조 → 위험 점검 → 등급 · 한도 → 심사의견서 초고**까지 보조하는 AI 서비스.
> SSAFY 2학기 프로젝트 · 5인 팀.

**Role** · Infra · BE &nbsp;&nbsp;|&nbsp;&nbsp; `Spring Boot` `Spring Security` `PostgreSQL` `Docker Swarm` `Jenkins` `GitLab CI` `Prometheus` `Grafana` `AWS Lightsail`

- **무중단 배포 · CI/CD** — Docker Swarm start-first 무중단 배포, Jenkins 자동 배포와 롤백, GitLab Runner CI 게이트(포맷 · 린트 · 테스트 · 빌드 · 시크릿 스캔)
- **관측** — Prometheus · Loki · Grafana로 지표와 컨테이너 로그를 수집해 운영 대시보드 구성
- **로그인 · 접근 제어** — SSAFY 통합인증, DB 세션, CSRF, TOTP 2차 인증, 담당자별 접근 제어와 감사부 열람
- **감사 로그** — SHA-256 해시 체인 · DB 권한 분리 · 트리거로 수정 · 삭제 차단, 체인 검증 API로 변조 위치 확인


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

**Role** · Infra · BE · AI &nbsp;&nbsp;|&nbsp;&nbsp; `Django` `DRF` `Vue.js` `SQLite` `GitHub Actions` `AWS EC2`

- **배포** — GitHub Actions로 CI/CD를 구성하고 AWS EC2(Nginx · Gunicorn)에 배포, 헬스체크 실패 시 직전 커밋으로 롤백
- **REST API · DB 설계** — DRF로 REST API와 JWT 인증 구현, 회원 · 상품 · 가입 · 찜 · 커뮤니티 5개 도메인 ERD 모델링
- **추천 파이프라인** — 금융감독원 API로 예·적금 상품 766건 수집, 우대조건을 태그 8개로 사전 구조화, 조건 필터링 후 세후 수령액 순 정렬
- **스트리밍 챗봇** — 상품 데이터로 답변 근거를 한정하고 SSE로 응답, 대화는 서버에 저장하지 않고 최근 5턴만 전달

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
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white)

**AI**  
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logoColor=white)

**Database & Storage**  
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-FF4438?style=for-the-badge&logo=redis&logoColor=white)
![MinIO](https://img.shields.io/badge/MinIO-C72E49?style=for-the-badge&logo=minio&logoColor=white)
![Flyway](https://img.shields.io/badge/Flyway-CC0200?style=for-the-badge&logo=flyway&logoColor=white)

**Infra & Cloud**  
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![K3s](https://img.shields.io/badge/K3s-FFC61C?style=for-the-badge&logo=k3s&logoColor=black)
![Terraform](https://img.shields.io/badge/Terraform-844FBA?style=for-the-badge&logo=terraform&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![Argo CD](https://img.shields.io/badge/Argo%20CD-EF7B4D?style=for-the-badge&logo=argo&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logoColor=white)
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

**Tools**  
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Jira](https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=jira&logoColor=white)
