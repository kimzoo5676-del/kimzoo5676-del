<p><img src="assets/header.png" width="920" alt="김주우 · Infra · Backend Engineer"/></p>

<p align="center">
  <a href="https://kimzoo5676-del.github.io/"><img src="assets/btn-site.png" width="248" alt="Portfolio Site kimzoo5676-del.github.io"/></a>
  <a href="https://github.com/kimzoo5676-del/kimzoo5676-del.github.io/raw/main/pdf/kimjoowoo-infra-portfolio.pdf"><img src="assets/btn-ce.png" width="248" alt="Cloud Engineer Portfolio PDF"/></a>
  <a href="https://github.com/kimzoo5676-del/kimzoo5676-del.github.io/raw/main/pdf/kimjoowoo-sw-portfolio.pdf"><img src="assets/btn-sw.png" width="248" alt="Software Engineer Portfolio PDF"/></a>
  <br/>
  <a href="https://zoolog.site/"><img src="assets/btn-zoolog.png" width="248" alt="Zoolog Tech Blog"/></a>
  <a href="https://velog.io/@zooouu/posts"><img src="assets/btn-velog.png" width="248" alt="Velog @zooouu"/></a>
  <a href="mailto:kimzoo5676@gmail.com"><img src="assets/btn-mail.png" width="248" alt="Email kimzoo5676@gmail.com"/></a>
</p>

<br/>

<img src="assets/sec-education.png" width="920" alt="Education"/>

<img src="assets/edu.png" width="920" alt="Education"/>

<br/>

<img src="assets/sec-projects.png" width="920" alt="Projects"/>

<img src="assets/proj-newlearn.png" width="920" alt="NEW:LEARN"/>

<p><a href="https://newlearn.io.kr"><img src="assets/link-website.png" width="146" alt="Website"/></a> <a href="https://newlearn-issue.vercel.app/home"><img src="assets/link-demo.png" width="146" alt="Demo"/></a> <a href="https://github.com/a102-NEWLEARN/NEW-LEARN"><img src="assets/link-github.png" width="146" alt="GitHub"/></a></p>

<img src="assets/stack-newlearn.png" width="736" alt="NEW:LEARN 기술 스택"/>

- **클러스터 구성** — 서버 2대를 WireGuard로 연결해 kubeadm 클러스터 하나로 운영, EC2 · 보안 그룹 · 백업 S3 버킷은 Terraform으로 관리
- **GitOps 배포** — MR 검사 → 이미지 빌드(Kaniko) → 배포 태그 MR → Argo CD 동기화, 롤백은 `git revert`
- **분석 작업 파이프라인** — 기사 분석을 Redis Streams 작업 큐로 API 응답과 분리, 동일 사건 판정은 PostgreSQL advisory lock으로 직렬화
- **기사 수집 · 적재** — 15분 주기 CronJob으로 뉴스 API 수집(중복 주소 제외), 기존 기사 79,335건은 카나리 100건 후 전체 적재
- **조회 성능** — 공개 기사 부분 인덱스로 기사 목록 p50 242ms → 22ms, 부하 테스트 포화 처리량 초당 93건 → 123건
- **묶기 정확도 평가** — 정답 라벨이 없는 사건 · 이슈 묶음을 LLM 채점과 사람 검수 200건으로 평가(B³ F1 사건 0.854 · 이슈 0.926)

<br/>

<img src="assets/proj-modi.png" width="920" alt="모디 (MODI)"/>

<p><a href="https://apps.apple.com/kr/app/id6801031228"><img src="assets/link-appstore.png" width="146" alt="App Store"/></a> <a href="https://maramodi.cloud/"><img src="assets/link-website.png" width="146" alt="Website"/></a> <a href="https://github.com/intpsquad/modi"><img src="assets/link-github.png" width="146" alt="GitHub"/></a></p>

<img src="assets/stack-modi.png" width="736" alt="모디 (MODI) 기술 스택"/>

- **CI/CD** — Oracle Cloud(ARM) 이관과 함께 GitHub Actions 워크플로로 재구성, 테스트를 통과한 코드만 배포
- **blue/green 배포** — 새 버전이 헬스체크를 통과한 뒤 Caddy로 트래픽 전환, 이전 버전 컨테이너는 롤백용으로 유지
- **백업 · 복구** — PostgreSQL과 파일 저장소(MinIO)를 매일 백업, 임시 컨테이너 복구로 테이블 20개 행 수 일치 확인
- **크롤링 파이프라인** — 사이트별 크롤러 분배, 실패를 재시도 대상 · 쿨다운 보류 · 확정 실패로 나눈 재시도와 Redis 쿨다운, 등록 시점 주소 검증
- **인스타그램 크롤러 장애** — 가설 6개를 하나씩 검증해 Java 클라이언트 접속 지문으로 원인을 확정, 호출 2곳만 HTTP/2 클라이언트로 교체
- **AI 할 일 추천** — 방에 모인 자료로 할 일 후보를 만드는 FastAPI 서버, 평가 러너로 변경마다 측정해 LLM 1회 호출 구조로 정리(앱 실측 평균 28.2초 → 11.8초, 각 3회)
- **iOS 릴리스** — TestFlight 배포와 App Store 심사 제출

<br/>

<img src="assets/proj-zoolog.png" width="920" alt="Zoolog"/>

<p><a href="https://zoolog.site/"><img src="assets/link-website.png" width="146" alt="Website"/></a> <a href="https://github.com/kimzoo5676-del/Zoolog"><img src="assets/link-github.png" width="146" alt="GitHub"/></a></p>

<img src="assets/stack-zoolog.png" width="638" alt="Zoolog 기술 스택"/>

- **GitOps 배포** — GitHub Actions(통합 테스트 → 이미지 빌드 → 매니페스트 태그 커밋)와 Argo CD로 k3s에 배포, 롤백은 `git revert`
- **로그인** — Google OIDC와 허용 이메일 하나로 본인만 글을 쓰게 하고, 서버 세션과 CSRF 보호 적용
- **글-이미지 연결 테이블** — 글 ID 컬럼 하나를 다대다 연결 테이블로 바꿔, 연결이 모두 끊긴 이미지만 유예 기간 뒤 정리
- **기사 메일 재발송** — 보낸 날 기록(UNIQUE)과 서버 시작 · 매시 정각 확인으로 서버가 꺼져 있던 날도 재발송

<br/>

<img src="assets/proj-yeobo.png" width="920" alt="여보 (여신보좌관)"/>

<p><a href="https://github.com/kimzoo5676-del/loanreview/blob/main/docs/presentation/yeobo-presentation.pdf"><img src="assets/link-slides.png" width="146" alt="Slides"/></a> <a href="https://github.com/kimzoo5676-del/loanreview"><img src="assets/link-github.png" width="146" alt="GitHub"/></a></p>

<img src="assets/stack-yeobo.png" width="638" alt="여보 (여신보좌관) 기술 스택"/>

- **무중단 배포 · CI/CD** — Docker Swarm start-first 무중단 배포, Jenkins 자동 배포와 롤백, GitLab Runner CI 게이트(포맷 · 린트 · 테스트 · 빌드 · 시크릿 스캔)
- **관측** — Prometheus · Loki · Grafana로 지표와 컨테이너 로그를 수집해 운영 대시보드 구성
- **로그인 · 접근 제어** — SSAFY 통합인증, DB 세션, CSRF, TOTP 2차 인증, 담당자별 접근 제어와 감사부 열람
- **감사 로그** — SHA-256 해시 체인 · DB 권한 분리 · 트리거로 수정 · 삭제 차단, 체인 검증 API로 변조 위치 확인
- **값 계약 테스트** — 프론트 테스트가 백엔드 enum 파일을 직접 읽어 값과 순서를 비교, 어긋나면 머지 전 CI에서 실패

<br/>

<img src="assets/proj-ourwish.png" width="920" alt="OURWISH"/>

<p><a href="https://our-wish.site/"><img src="assets/link-website.png" width="146" alt="Website"/></a> <a href="https://github.com/Our-Wish/ourwish"><img src="assets/link-github.png" width="146" alt="GitHub"/></a></p>

<img src="assets/stack-ourwish.png" width="638" alt="OURWISH 기술 스택"/>

- **배포** — GitHub Actions로 CI/CD를 구성하고 AWS EC2(Nginx · Gunicorn)에 배포, 헬스체크 실패 시 직전 커밋으로 롤백
- **REST API · DB 설계** — DRF로 REST API와 JWT 인증 구현, 회원 · 상품 · 가입 · 찜 · 커뮤니티 5개 도메인 ERD 모델링
- **추천 파이프라인** — 금융감독원 API로 예·적금 상품 766건 수집, 우대조건을 태그 8개로 사전 구조화, 조건 필터링 후 세후 수령액 순 정렬
- **스트리밍 챗봇** — 상품 데이터로 답변 근거를 한정하고 SSE로 응답, 대화는 서버에 저장하지 않고 최근 5턴만 전달

<br/>

<img src="assets/sec-awards.png" width="920" alt="Awards"/>

<img src="assets/awards.png" width="920" alt="Awards"/>

<br/>

<img src="assets/sec-stack.png" width="920" alt="Core Stack"/>

<img src="assets/core-stack.png" width="920" alt="Core Stack"/>
