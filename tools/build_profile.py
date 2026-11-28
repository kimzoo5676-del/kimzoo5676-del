"""프로필 README의 기술 아이콘 카드(Core Stack · 프로젝트별 기술 줄)를 만든다.

README 본문은 손으로 쓰는 마크다운이고, 이 도구는 assets/의 아이콘 카드 이미지만 다시 만든다.
카드는 밝은 바탕 · 회색 테두리 · 파란 강조(Pretendard / JetBrains Mono)이고,
GitHub 다크 모드에서도 글자가 묻히지 않도록 바탕을 밝게 칠한다.
사용: python3 tools/build_profile.py   (Chrome 필요. 글꼴은 FONTS 폴더의 정적 TTF)
기술을 바꾸면 README의 이미지 대체 글(alt)과 width도 같이 맞춘다(출력되는 width 값).
"""
import os, subprocess

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
.card{background:#fbfbfc;border:1.5px solid #dfe2e8;border-radius:16px}
'''
W = 900  # 카드 폭(px)
PAD = 10  # 카드 둘레 투명 여백. 캔버스 폭 CW = W + 2*PAD
CW = W + 2 * PAD


def shot(name, html, w, h, pad):
    # pad='both': Core Stack 카드(캔버스 CW), pad='left': 프로젝트 기술 줄(왼쪽 선만 맞춤)
    if pad == 'both':
        html, w = '<div style="padding:0 %dpx">%s</div>' % (PAD, html), w + 2 * PAD
    else:
        html, w = '<div style="padding-left:%dpx">%s</div>' % (PAD, html), w + PAD
    src = os.path.join(TMP, name + '.html')
    open(src, 'w', encoding='utf-8').write('<!doctype html><meta charset="utf-8"><style>%s</style>%s' % (BASE, html))
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--allow-file-access-from-files',
                    '--default-background-color=00000000', '--force-device-scale-factor=2', '--window-size=%d,%d' % (w, h),
                    '--screenshot=' + os.path.join(A, name + '.png'), 'file://' + src], stderr=subprocess.DEVNULL, check=True)


def ic(name):
    return 'file://' + os.path.join(T, 'icons', name)


# ───────── 데이터 ─────────
S = lambda f, l: (f, l)
STACKS = {
    'newlearn': [S('kubernetes.svg', 'Kubernetes'), S('argocd.svg', 'Argo CD'), S('terraform.svg', 'Terraform'), S('java.svg', 'Java'), S('spring.svg', 'Spring Boot'), S('postgresql.svg', 'PostgreSQL'), S('redis.svg', 'Redis')],
    'modi': [S('docker.svg', 'Docker'), S('githubactions.svg', 'GitHub Actions'), S('oracle.svg', 'Oracle Cloud'), S('spring.svg', 'Spring Boot'), S('fastapi.svg', 'FastAPI'), S('postgresql.svg', 'PostgreSQL'), S('redis.svg', 'Redis')],
    'zoolog': [S('k3s.svg', 'k3s'), S('argocd.svg', 'Argo CD'), S('spring.svg', 'Spring Boot'), S('react.svg', 'React'), S('typescript.svg', 'TypeScript'), S('postgresql.svg', 'PostgreSQL')],
    'yeobo': [S('docker.svg', 'Docker Swarm'), S('jenkins.svg', 'Jenkins'), S('prometheus.svg', 'Prometheus'), S('spring.svg', 'Spring Boot'), S('postgresql.svg', 'PostgreSQL'), S('fastapi.svg', 'FastAPI')],
    'ourwish': [S('githubactions.svg', 'GitHub Actions'), S('aws.svg', 'AWS EC2'), S('django.svg', 'Django'), S('drf.svg', 'DRF'), S('vue.svg', 'Vue.js'), S('sqlite.svg', 'SQLite')],
}
CORE = [('Infra', [S('docker.svg', 'Docker'), S('kubernetes.svg', 'Kubernetes'), S('aws.svg', 'AWS'), S('terraform.svg', 'Terraform'), S('argocd.svg', 'Argo CD'), S('prometheus.svg', 'Prometheus'), S('githubactions.svg', 'GitHub Actions')]),
        ('Backend', [S('spring.svg', 'Spring Boot'), S('fastapi.svg', 'FastAPI'), S('django.svg', 'Django')]),
        ('Data', [S('postgresql.svg', 'PostgreSQL'), S('redis.svg', 'Redis'), S('flyway.svg', 'Flyway')]),
        ('Language', [S('java.svg', 'Java'), S('python.svg', 'Python'), S('typescript.svg', 'TypeScript')])]


# ───────── 이미지 ─────────
TILE_CSS = '''<style>.row{display:flex;gap:10px;padding:2px}.it{width:88px;text-align:center;font:600 12px/1.25 Pretendard,sans-serif;color:#3d3f45}
.it i{display:flex;align-items:center;justify-content:center;width:56px;height:56px;margin:0 auto 7px;border-radius:14px;background:#fff;border:1.5px solid #e3e6eb}
.it img{max-width:32px;max-height:32px}</style>'''


def tiles(items):
    return '<div class="row">%s</div>' % ''.join('<div class="it"><i><img src="%s"></i>%s</div>' % (ic(f), l) for f, l in items)


def stack_card(key, items):
    html = TILE_CSS + '<style>.c{display:inline-block;padding:14px 16px 10px}</style><div class="card c">%s</div>' % tiles(items)
    w = len(items) * 98 + 4 + 36
    shot('stack-' + key, html, w, 124, 'left')
    return w + PAD


def core_stack():
    html = TILE_CSS + ('<style>.c{width:%dpx;padding:16px 28px}.g{display:grid;grid-template-columns:150px 1fr;align-items:center;padding:10px 0;border-top:1px solid #eceef2}'
                       '.g:first-child{border-top:0}.g b{font:600 14px "JetBrains Mono",monospace;color:#3574f0}</style><div class="card c">%s</div>'
                       ) % (W, ''.join('<div class="g"><b>%s</b>%s</div>' % (n, tiles(i)) for n, i in CORE))
    shot('core-stack', html, W, 34 + len(CORE) * 109, 'both')


if __name__ == '__main__':
    pct = lambda px: ('%.2f' % (int(px * 10000 / CW) / 100)).rstrip('0').rstrip('.') + '%'  # README width 값(내림)
    core_stack()
    print('core-stack width="100%"')
    for k, items in STACKS.items():
        print('stack-%s width="%s"' % (k, pct(stack_card(k, items))))
