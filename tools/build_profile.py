"""프로필 README와 이미지(헤더 · 버튼 · 칸 제목 · 카드 · 기술 아이콘)를 한 데이터에서 만든다.

모든 이미지는 같은 모양(밝은 카드 · 회색 테두리 · 파란 강조 · Pretendard / JetBrains Mono)이고,
GitHub 다크 모드에서도 글자가 묻히지 않도록 바탕을 밝게 칠한다.
사용: python3 tools/build_profile.py   (Chrome 필요. 글꼴은 FONTS 폴더의 정적 TTF)
"""
import os, sys, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = os.path.join(ROOT, 'tools')
A = os.path.join(ROOT, 'assets')
TMP = os.path.join(ROOT, 'drafts', 'build')
FONTS = os.environ.get('FONTS', os.path.expanduser('~/Library/Mobile Documents/iCloud~md~obsidian/Documents/my-vault/04_지원/마스터 포트폴리오 SW/assets/fonts'))
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
os.makedirs(A, exist_ok=True)
os.makedirs(TMP, exist_ok=True)

FF = ''.join('@font-face{font-family:"%s";src:url("file://%s/%s-%s.ttf");font-weight:%d}\n' % (fam, FONTS, fn, w, n)
             for fam, fn in (('Pretendard', 'Pretendard'), ('JetBrains Mono', 'JetBrainsMono'))
             for w, n in (('Regular', 400), ('Medium', 500), ('SemiBold', 600), ('Bold', 700), ('ExtraBold', 800)))
BASE = FF + '''*{box-sizing:border-box}html,body{margin:0;background:transparent}
body{font-family:Pretendard,sans-serif;color:#1e1f22}
.mono{font-family:"JetBrains Mono",Pretendard,monospace}
.card{background:#fbfbfc;border:1.5px solid #dfe2e8;border-radius:16px}
.dots{display:flex;gap:10px}.dots i{width:12px;height:12px;border-radius:50%}
.dots i:nth-child(1){background:#ff5f57}.dots i:nth-child(2){background:#febc2e}.dots i:nth-child(3){background:#28c840}
'''
SVG = {
    'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/>',
    'pdf': '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h4"/>',
    'blog': '<path d="M4 20h4L19 9a2.8 2.8 0 0 0-4-4L4 16z"/><path d="M13.5 6.5l4 4"/>',
    'velog': '<path d="M5 6h3.2l2.6 9.2L16.5 6H19l-7.2 12h-2.3z"/>',
    'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6.5l8.5 6.5 8.5-6.5"/>',
    'play': '<circle cx="12" cy="12" r="9"/><path d="M10 8.5l5.5 3.5-5.5 3.5z"/>',
    'slides': '<rect x="3" y="4" width="18" height="13" rx="2"/><path d="M12 17v3M8 20h8M7 9h6M7 12h9"/>',
}


def shot(name, html, w, h, pad=None):
    # pad='both': 넓은 카드(캔버스 CW), pad='left': 버튼 · 기술 줄(왼쪽 선만 맞춤)
    if pad == 'both':
        html, w = '<div style="padding:0 %dpx">%s</div>' % (PAD, html), w + 2 * PAD
    elif pad == 'left':
        html, w = '<div style="padding-left:%dpx">%s</div>' % (PAD, html), w + PAD
    src = os.path.join(TMP, name + '.html')
    open(src, 'w', encoding='utf-8').write('<!doctype html><meta charset="utf-8"><style>%s</style>%s' % (BASE, html))
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--allow-file-access-from-files',
                    '--default-background-color=00000000', '--force-device-scale-factor=2', '--window-size=%d,%d' % (w, h),
                    '--screenshot=' + os.path.join(A, name + '.png'), 'file://' + src], stderr=subprocess.DEVNULL, check=True)


def ic(name):
    return 'file://' + os.path.join(T, 'icons', name)


def logo(name):
    return 'file://' + os.path.join(T, 'logos', name)


# ───────── 데이터 ─────────
LEAD = '모두가 같은 목표를 볼 수 있도록 소통하고,<br>배운 것을 나누며 함께 성장하는 엔지니어입니다.'
PDF = 'https://github.com/kimzoo5676-del/kimzoo5676-del.github.io/raw/main/pdf/'
TOP = [
    [('site', 'globe', 'Portfolio Site', 'kimzoo5676-del.github.io', 'https://kimzoo5676-del.github.io/'),
     ('ce', 'pdf', 'Cloud Engineer', 'Portfolio PDF', PDF + 'kimjoowoo-infra-portfolio.pdf'),
     ('sw', 'pdf', 'Software Engineer', 'Portfolio PDF', PDF + 'kimjoowoo-sw-portfolio.pdf')],
    [('zoolog', 'blog', 'Zoolog', 'Tech Blog', 'https://zoolog.site/'),
     ('velog', 'velog', 'Velog', '@zooouu', 'https://velog.io/@zooouu/posts'),
     ('mail', 'mail', 'Email', 'kimzoo5676@gmail.com', 'mailto:kimzoo5676@gmail.com')],
]
EDU = [('2026.01 – 2026.12', '삼성청년SW·AI아카데미 15기', '12월 수료 예정'),
       ('2019.03 – 2025.08', '한양대학교 ERICA 경제학부', '졸업')]
AWARDS = [('2026.11', '2학기 자율 프로젝트 우수상 (3위)', 'NEW:LEARN'),
          ('2026.07', '싸피레이스 2026 SUMMER 2위', 'AirSim 기반 주행 봇 타임어택 · 팀 길이NullNull하네'),
          ('2026.06', '1학기 관통 프로젝트 최우수상 (서울2반 1등)', 'OURWISH')]
LINK = {'website': ('globe', 'Website'), 'demo': ('play', 'Demo'), 'github': ('github.svg', 'GitHub'),
        'appstore': ('apple.svg', 'App Store'), 'slides': ('slides', 'Slides')}
S = lambda f, l: (f, l)
PROJECTS = [
    dict(key='newlearn', logo='newlearn.png', name='NEW:LEARN', sub='뉴스를 AI로 구조화해 사건과 이슈의 흐름으로 보여 주는 서비스',
         period='2026.10 – 2026.11', chips=['SSAFY 2학기 · 6인', 'Infra · BE'],
         links=[('demo', 'https://newlearn-issue.vercel.app/home'), ('github', 'https://github.com/a102-NEWLEARN/NEW-LEARN')],
         stack=[S('java.svg', 'Java'), S('spring.svg', 'Spring Boot'), S('postgresql.svg', 'PostgreSQL'), S('redis.svg', 'Redis'), S('kubernetes.svg', 'Kubernetes'), S('argocd.svg', 'Argo CD'), S('terraform.svg', 'Terraform')],
         bullets=[
             '**클러스터 구성** — 서버 2대를 WireGuard로 연결해 kubeadm 클러스터 하나로 운영, EC2 · 보안 그룹 · 백업 S3 버킷은 Terraform으로 관리',
             '**GitOps 배포** — MR 검사 → 이미지 빌드(Kaniko) → 배포 태그 MR → Argo CD 동기화, 롤백은 `git revert`',
             '**분석 작업 파이프라인** — 기사 분석을 Redis Streams 작업 큐로 API 응답과 분리, 동일 사건 판정은 PostgreSQL advisory lock으로 직렬화',
             '**기사 수집 · 적재** — 15분 주기 CronJob으로 뉴스 API 수집(중복 주소 제외), 기존 기사 79,335건은 카나리 100건 후 전체 적재',
             '**조회 성능** — 공개 기사 부분 인덱스로 기사 목록 p50 242ms → 22ms, 부하 테스트 포화 처리량 초당 93건 → 123건',
             '**묶기 정확도 평가** — 정답 라벨이 없는 사건 · 이슈 묶음을 LLM 채점과 사람 검수 200건으로 평가(B³ F1 사건 0.854 · 이슈 0.926)']),
    dict(key='modi', logo='modi.png', name='모디 (MODI)', sub='방을 만들어 팀이 목표 기간 동안 할 일 · 일정 · 자료를 공유하는 iOS 협업 앱',
         period='2026.07 – 운영 중', chips=['App Store 출시 · 6인', 'Infra · BE · AI'],
         links=[('appstore', 'https://apps.apple.com/kr/app/id6801031228'), ('website', 'https://maramodi.cloud/'), ('github', 'https://github.com/intpsquad/modi')],
         stack=[S('spring.svg', 'Spring Boot'), S('fastapi.svg', 'FastAPI'), S('postgresql.svg', 'PostgreSQL'), S('redis.svg', 'Redis'), S('docker.svg', 'Docker'), S('githubactions.svg', 'GitHub Actions'), S('oracle.svg', 'Oracle Cloud')],
         bullets=[
             '**CI/CD** — Oracle Cloud(ARM) 이관과 함께 GitHub Actions 워크플로로 재구성, 테스트를 통과한 코드만 배포',
             '**blue/green 배포** — 새 버전이 헬스체크를 통과한 뒤 Caddy로 트래픽 전환, 이전 버전 컨테이너는 롤백용으로 유지',
             '**백업 · 복구** — PostgreSQL과 파일 저장소(MinIO)를 매일 백업, 임시 컨테이너 복구로 테이블 20개 행 수 일치 확인',
             '**크롤링 파이프라인** — 사이트별 크롤러 분배, 실패를 재시도 대상 · 쿨다운 보류 · 확정 실패로 나눈 재시도와 Redis 쿨다운, 등록 시점 주소 검증',
             '**인스타그램 크롤러 장애** — 가설 6개를 하나씩 검증해 Java 클라이언트 접속 지문으로 원인을 확정, 호출 2곳만 HTTP/2 클라이언트로 교체',
             '**AI 할 일 추천** — 방에 모인 자료로 할 일 후보를 만드는 FastAPI 서버, 평가 러너로 변경마다 측정해 LLM 1회 호출 구조로 정리(앱 실측 평균 28.2초 → 11.8초, 각 3회)',
             '**iOS 릴리스** — TestFlight 배포와 App Store 심사 제출']),
    dict(key='zoolog', logo='zoolog.svg', name='Zoolog', sub='공부한 글을 주제별 그래프와 달력으로 정리하는 개인 기술 블로그',
         period='2026.10 – 운영 중', chips=['개인 프로젝트 · 1인', 'Infra · Full-Stack'],
         links=[('website', 'https://zoolog.site/'), ('github', 'https://github.com/kimzoo5676-del/Zoolog')],
         stack=[S('spring.svg', 'Spring Boot'), S('react.svg', 'React'), S('typescript.svg', 'TypeScript'), S('postgresql.svg', 'PostgreSQL'), S('k3s.svg', 'k3s'), S('argocd.svg', 'Argo CD')],
         bullets=[
             '**GitOps 배포** — GitHub Actions(통합 테스트 → 이미지 빌드 → 매니페스트 태그 커밋)와 Argo CD로 k3s에 배포, 롤백은 `git revert`',
             '**로그인** — Google OIDC와 허용 이메일 하나로 본인만 글을 쓰게 하고, 서버 세션과 CSRF 보호 적용',
             '**글-이미지 연결 테이블** — 글 ID 컬럼 하나를 다대다 연결 테이블로 바꿔, 연결이 모두 끊긴 이미지만 유예 기간 뒤 정리',
             '**기사 메일 재발송** — 보낸 날 기록(UNIQUE)과 서버 시작 · 매시 정각 확인으로 서버가 꺼져 있던 날도 재발송']),
    dict(key='yeobo', logo='yeosin.svg', name='여보 (여신보좌관)', sub='스타트업 법인 서류 판독부터 심사의견서 초고까지 은행 여신 심사를 보조하는 AI 서비스',
         period='2026.08 – 2026.09', chips=['SSAFY 2학기 · 5인', 'Infra · BE'],
         links=[('slides', 'https://github.com/kimzoo5676-del/loanreview/blob/main/docs/presentation/yeobo-presentation.pdf'), ('github', 'https://github.com/kimzoo5676-del/loanreview')],
         stack=[S('spring.svg', 'Spring Boot'), S('postgresql.svg', 'PostgreSQL'), S('fastapi.svg', 'FastAPI'), S('docker.svg', 'Docker Swarm'), S('jenkins.svg', 'Jenkins'), S('prometheus.svg', 'Prometheus')],
         bullets=[
             '**무중단 배포 · CI/CD** — Docker Swarm start-first 무중단 배포, Jenkins 자동 배포와 롤백, GitLab Runner CI 게이트(포맷 · 린트 · 테스트 · 빌드 · 시크릿 스캔)',
             '**관측** — Prometheus · Loki · Grafana로 지표와 컨테이너 로그를 수집해 운영 대시보드 구성',
             '**로그인 · 접근 제어** — SSAFY 통합인증, DB 세션, CSRF, TOTP 2차 인증, 담당자별 접근 제어와 감사부 열람',
             '**감사 로그** — SHA-256 해시 체인 · DB 권한 분리 · 트리거로 수정 · 삭제 차단, 체인 검증 API로 변조 위치 확인',
             '**값 계약 테스트** — 프론트 테스트가 백엔드 enum 파일을 직접 읽어 값과 순서를 비교, 어긋나면 머지 전 CI에서 실패']),
    dict(key='ourwish', logo='ourwish.png', name='OURWISH', sub='생성형 AI와 금융 데이터로 사용자에게 맞는 예·적금 상품을 추천하는 서비스',
         period='2026.05 – 2026.06', chips=['SSAFY 1학기 · 2인 · 최우수상', 'Infra · BE · AI'],
         links=[('website', 'https://our-wish.site/'), ('github', 'https://github.com/Our-Wish/ourwish')],
         stack=[S('django.svg', 'Django'), S('drf.svg', 'DRF'), S('vue.svg', 'Vue.js'), S('sqlite.svg', 'SQLite'), S('githubactions.svg', 'GitHub Actions'), S('aws.svg', 'AWS EC2')],
         bullets=[
             '**배포** — GitHub Actions로 CI/CD를 구성하고 AWS EC2(Nginx · Gunicorn)에 배포, 헬스체크 실패 시 직전 커밋으로 롤백',
             '**REST API · DB 설계** — DRF로 REST API와 JWT 인증 구현, 회원 · 상품 · 가입 · 찜 · 커뮤니티 5개 도메인 ERD 모델링',
             '**추천 파이프라인** — 금융감독원 API로 예·적금 상품 766건 수집, 우대조건을 태그 8개로 사전 구조화, 조건 필터링 후 세후 수령액 순 정렬',
             '**스트리밍 챗봇** — 상품 데이터로 답변 근거를 한정하고 SSE로 응답, 대화는 서버에 저장하지 않고 최근 5턴만 전달']),
]
CORE = [('Language', [S('java.svg', 'Java'), S('python.svg', 'Python'), S('typescript.svg', 'TypeScript')]),
        ('Backend', [S('spring.svg', 'Spring Boot'), S('fastapi.svg', 'FastAPI'), S('django.svg', 'Django')]),
        ('Data', [S('postgresql.svg', 'PostgreSQL'), S('redis.svg', 'Redis'), S('flyway.svg', 'Flyway')]),
        ('Infra', [S('docker.svg', 'Docker'), S('kubernetes.svg', 'Kubernetes'), S('aws.svg', 'AWS'), S('terraform.svg', 'Terraform'), S('argocd.svg', 'Argo CD'), S('prometheus.svg', 'Prometheus'), S('githubactions.svg', 'GitHub Actions')])]
SECTIONS = {'education': ('Education', '~/kimjoowoo/education'), 'projects': ('Projects', '~/kimjoowoo/projects'),
            'awards': ('Awards', '~/kimjoowoo/awards'), 'stack': ('Core Stack', '~/kimjoowoo/stack')}

W = 900  # 카드 폭(px)
PAD = 10  # 헤더 카드의 투명 여백과 같은 비율. 캔버스 폭 CW = W + 2*PAD
CW = W + 2 * PAD


# ───────── 이미지 ─────────
def header():
    logos = ''.join('<img src="%s"%s>' % (logo(f), '') for f in ('newlearn.png', 'modi.png', 'yeosin.svg', 'ourwish.png', 'zoolog.svg'))
    css = '''<style>.win{position:absolute;inset:14px;border-radius:18px;background:#fbfbfc;border:1.5px solid #dfe2e8;overflow:hidden}
.bar{height:46px;display:flex;align-items:center;gap:16px;padding:0 20px;background:#f2f3f6;border-bottom:1px solid #e3e6eb}
.bar span{font-size:14px;color:#6c707e}.in{padding:20px 44px}.cmd{font-size:17px;color:#6c707e}.cmd b{color:#3574f0;font-weight:700}
.nm{font-size:52px;font-weight:800;letter-spacing:-.03em;margin:4px 0 0}.nm small{font-size:26px;font-weight:600;color:#6c707e;margin-left:14px;letter-spacing:0}
.rl{font-size:24px;font-weight:700;margin-top:6px}.rl span{background:linear-gradient(transparent 60%,#d4e3fd 60%);padding:0 6px}
.ld{font-size:20px;line-height:1.6;color:#2b2d30;margin-top:4px}
.lg{position:absolute;right:48px;top:118px;display:flex;gap:14px}.lg img{width:58px;height:58px;border-radius:14px;border:1px solid #e3e6eb;object-fit:cover;background:#fff}.lg img.pad{padding:8px;object-fit:contain}</style>'''
    html = css + ('<div class="win"><div class="bar"><div class="dots"><i></i><i></i><i></i></div><span class="mono">~/kimjoowoo — zsh</span></div>'
                  '<div class="in"><div class="cmd mono"><b>$</b> whoami</div><div class="nm">김주우<small class="mono">Joowoo Kim</small></div>'
                  '<div class="rl"><span>Infra · Backend Engineer</span></div><div class="cmd mono" style="margin-top:14px"><b>$</b> cat motto.txt</div>'
                  '<div class="ld">%s</div></div><div class="lg">%s</div></div>') % (LEAD, logos)
    shot('header', html, 1280, 340)


BTN_CSS = '''<style>.b{display:flex;align-items:center;gap:12px;padding:0 16px;border-radius:12px;background:#fbfbfc;border:1.5px solid #dfe2e8}
.b svg{width:24px;height:24px;flex:none;fill:none;stroke:#3574f0;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.b img{width:22px;height:22px;flex:none}
.t{font-size:15px;font-weight:700;line-height:1.15}.s{font:500 11.5px/1.3 "JetBrains Mono",monospace;color:#6c707e}</style>'''


def icon_html(i):
    return '<img src="%s">' % ic(i) if i.endswith('.svg') else '<svg viewBox="0 0 24 24">%s</svg>' % SVG[i]


def top_buttons():
    for row in TOP:
        for k, i, t, s, _ in row:
            shot('btn-' + k, BTN_CSS + '<div class="b" style="width:248px;height:56px">%s<div><div class="t">%s</div><div class="s">%s</div></div></div>' % (icon_html(i), t, s), 248, 56)


def link_buttons():
    for k, (i, label) in LINK.items():
        shot('link-' + k, BTN_CSS + '<div class="b" style="width:136px;height:42px;gap:10px;padding:0 14px"><span style="display:flex">%s</span><div class="t" style="font-size:14px">%s</div></div>' % (icon_html(i).replace('width:24px', ''), label), 136, 42, 'left')


def section(k):
    title, path = SECTIONS[k]
    html = ('<style>.s{width:%dpx;height:52px;display:flex;align-items:center;gap:16px;padding:0 18px;background:#f2f3f6;border:1.5px solid #dfe2e8;border-radius:12px}'
            '.s b{font-size:20px;font-weight:800;letter-spacing:-.01em}.s span{margin-left:auto;font-size:13px;color:#6c707e}</style>'
            '<div class="s"><div class="dots"><i></i><i></i><i></i></div><b>%s</b><span class="mono">%s</span></div>') % (W, title, path)
    shot('sec-' + k, html, W, 52, 'both')


def rows_card(name, rows):
    h = 24 + len(rows) * 62
    html = ('<style>.c{width:%dpx;padding:10px 26px}.r{display:grid;grid-template-columns:190px 1fr;align-items:center;height:62px;border-top:1px solid #eceef2}'
            '.r:first-child{border-top:0}.d{font:600 14px "JetBrains Mono",monospace;color:#3574f0}.m{font-size:16px;font-weight:700}.x{font-size:13.5px;color:#6c707e;margin-top:3px}</style>'
            '<div class="card c">%s</div>') % (W, ''.join('<div class="r"><div class="d">%s</div><div><div class="m">%s</div><div class="x">%s</div></div></div>' % r for r in rows))
    shot(name, html, W, h, 'both')


def project_card(p):
    chips = ''.join('<span class="ch mono">%s</span>' % c for c in p['chips'])
    html = ('<style>.c{width:%dpx;height:112px;display:flex;align-items:center;gap:20px;padding:0 24px}'
            '.c img{width:64px;height:64px;border-radius:16px;border:1px solid #e3e6eb;background:#fff;object-fit:cover;flex:none}.c img.pad{padding:10px;object-fit:contain}'
            '.n{font-size:23px;font-weight:800;letter-spacing:-.02em}.sub{font-size:15px;color:#3d3f45;margin-top:4px}'
            '.cs{display:flex;gap:8px;margin-top:9px}.ch{font-size:12px;font-weight:600;color:#4a4d55;padding:4px 9px;border:1px solid #dfe2e8;border-radius:7px;background:#fff}'
            '.p{margin-left:auto;align-self:flex-start;margin-top:22px;font:600 13px "JetBrains Mono",monospace;color:#3574f0;white-space:nowrap}</style>'
            '<div class="card c"><img src="%s"%s><div><div class="n">%s</div><div class="sub">%s</div><div class="cs">%s</div></div><div class="p">%s</div></div>'
            ) % (W, logo(p['logo']), ' class="pad"' if p.get('pad') else '', p['name'], p['sub'], chips, p['period'])
    shot('proj-' + p['key'], html, W, 112, 'both')


TILE_CSS = '''<style>.row{display:flex;gap:10px;padding:2px}.it{width:88px;text-align:center;font:600 12px/1.25 Pretendard,sans-serif;color:#3d3f45}
.it i{display:flex;align-items:center;justify-content:center;width:56px;height:56px;margin:0 auto 7px;border-radius:14px;background:#fff;border:1.5px solid #e3e6eb}
.it img{max-width:32px;max-height:32px}</style>'''


def tiles(items):
    return '<div class="row">%s</div>' % ''.join('<div class="it"><i><img src="%s"></i>%s</div>' % (ic(f), l) for f, l in items)


def stack_card(p):
    # 다크 모드 대비: 아이콘 줄도 밝은 카드 위에
    html = TILE_CSS + '<style>.c{display:inline-block;padding:14px 16px 10px}</style><div class="card c">%s</div>' % tiles(p['stack'])
    w = len(p['stack']) * 98 + 4 + 36
    shot('stack-' + p['key'], html, w, 124, 'left')
    return w + PAD


def core_stack():
    html = TILE_CSS + ('<style>.c{width:%dpx;padding:16px 28px}.g{display:grid;grid-template-columns:150px 1fr;align-items:center;padding:10px 0;border-top:1px solid #eceef2}'
                       '.g:first-child{border-top:0}.g b{font:600 14px "JetBrains Mono",monospace;color:#3574f0}</style><div class="card c">%s</div>'
                       ) % (W, ''.join('<div class="g"><b>%s</b>%s</div>' % (n, tiles(i)) for n, i in CORE))
    shot('core-stack', html, W, 34 + len(CORE) * 109, 'both')


# ───────── README ─────────
def readme(stack_w):
    img = lambda f, w, alt: '<img src="assets/%s.png" width="%d" alt="%s"/>' % (f, w, alt)
    a = lambda href, inner: '<a href="%s">%s</a>' % (href, inner)
    out = ['<p>%s</p>' % img('header', CW, '김주우 · Infra · Backend Engineer'), '',
           '<p align="center">']
    for i, row in enumerate(TOP):
        if i:
            out.append('  <br/>')
        out += ['  ' + a(href, img('btn-' + k, 248, '%s %s' % (t, s))) for k, _, t, s, href in row]
    out += ['</p>', '', '<br/>', '', img('sec-education', CW, 'Education'), '', img('edu', CW, 'Education'), '', '<br/>', '',
            img('sec-projects', CW, 'Projects'), '']
    for p in PROJECTS:
        out += [img('proj-' + p['key'], CW, p['name']), '',
                '<p>' + ' '.join(a(href, img('link-' + k, 136 + PAD, LINK[k][1])) for k, href in p['links']) + '</p>', '',
                img('stack-' + p['key'], stack_w[p['key']], p['name'] + ' 기술 스택'), '']
        out += ['- ' + b for b in p['bullets']]
        out += ['', '<br/>', '']
    out += [img('sec-awards', CW, 'Awards'), '', img('awards', CW, 'Awards'), '', '<br/>', '',
            img('sec-stack', CW, 'Core Stack'), '', img('core-stack', CW, 'Core Stack'), '']
    open(os.path.join(ROOT, 'README.md'), 'w', encoding='utf-8').write('\n'.join(out))


if __name__ == '__main__':
    if '--all' in sys.argv:  # 헤더 · 위쪽 버튼은 승인본(drafts/header-A)을 그대로 둔다
        header()
        top_buttons()
    link_buttons()
    for k in SECTIONS:
        section(k)
    rows_card('edu', EDU)
    rows_card('awards', AWARDS)
    sw = {}
    for p in PROJECTS:
        project_card(p)
        sw[p['key']] = stack_card(p)
    core_stack()
    readme(sw)
    print('done', len(os.listdir(A)), 'images')
