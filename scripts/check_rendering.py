# -*- coding: utf-8 -*-
"""渲染层闸门：HTML 合法性 + 无障碍（浏览器里才看得到的那一层）。

为什么单独一个脚本、还要自己起服务
----------------------------------
`validate_all.py` 是**离线**链；这两道闸门要浏览器，而且**带参页面必须带对参数**——
不带参数跑 `card.html` 测的是「没有这张卡片」的错误态（2026-09-22 首跑就踩了这个坑：
三页"全干净"里，`card.html` 其实是空态）。所以这里：

1. 用 `http.server` 在 `web/` 起一个本地静态服务（同源，`fetch` 才通）；
2. 带**真参数**跑关键页面：`card.html?id=sk-0001`、`entry.html?code=A5`、
   `facet.html?code=S1`、`topic.html?slug=...`（slug 从 `web/data/meta.json` 现取）；
3. 逐页跑 `check_markup.py`（静态文件）与 `check_a11y.py`（URL）。

工具在 `D:\Git\tools\web-standard`；缺工具或依赖时**跳过并说明**，不让别的仓库因缺它而失败。

用法
----
    D:\python\python.exe scripts/check_rendering.py            # 全跑
    D:\python\python.exe scripts/check_rendering.py --quick    # 只跑 3 页无障碍
"""
import argparse, functools, http.server, json, os, re, socketserver, subprocess, sys, threading

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(ROOT, "web")
TOOLS = r"D:\Git\tools\web-standard\scripts"
MARKUP = os.path.join(TOOLS, "check_markup.py")
A11Y = os.path.join(TOOLS, "check_a11y.py")


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def topic_slug():
    try:
        meta = json.load(open(os.path.join(WEB, "data", "meta.json"), encoding="utf-8"))
        ts = meta.get("topics") or []
        if ts and isinstance(ts[0], dict):
            return ts[0].get("slug") or ts[0].get("id") or ""
        if ts:
            return str(ts[0])
    except Exception:
        pass
    return ""


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    """默认的 SimpleHTTPRequestHandler 会把每个请求打到 stdout，
    把闸门的汇总淹没在访问日志里 —— 静音它。"""
    def log_message(self, *a):
        pass


def serve(port):
    """起本地静态服务；**端口被占就顺延**（实测 8791 常被别的会话占着，
    写死端口会让这道闸门时好时坏 —— 闸门本身不该有"今天跑不了"这种状态）。"""
    handler = functools.partial(QuietHandler, directory=WEB)
    last = None
    for p in range(port, port + 25):
        try:
            httpd = socketserver.ThreadingTCPServer(("127.0.0.1", p), handler)
            httpd.daemon_threads = True
            threading.Thread(target=httpd.serve_forever, daemon=True).start()
            return httpd
        except OSError as e:
            last = e
    raise SystemExit("25 个端口都占用：%s" % last)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true", help="无障碍只跑 3 页")
    ap.add_argument("--port", type=int, default=8791)
    args = ap.parse_args()

    for name, p in (("check_markup.py", MARKUP), ("check_a11y.py", A11Y)):
        if not os.path.exists(p):
            print("缺工具 %s（%s）—— 跳过渲染层闸门。" % (name, p))
            return 0

    # ① HTML 合法性：静态文件即可
    pages = []
    for base in (WEB, os.path.join(WEB, "note")):
        if os.path.isdir(base):
            pages += [os.path.join(base, f) for f in sorted(os.listdir(base)) if f.endswith(".html")]
    bad_markup = []
    for p in pages:
        rc, out = run([sys.executable, MARKUP, p])
        if rc != 0 or "干净" not in out:
            bad_markup.append((os.path.relpath(p, WEB), out.strip().splitlines()[-4:]))
    print("HTML 合法性：%d 个页面，%d 个有问题" % (len(pages), len(bad_markup)))
    for name, lines in bad_markup[:5]:
        print("   ✗ %s" % name)
        for ln in lines:
            print("      " + ln.strip())

    # ② 无障碍：起服务 + 带真参数
    httpd = serve(args.port)
    port = httpd.server_address[1]
    slug = topic_slug()
    urls = [("index.html", "index.html"), ("search.html", "search.html"),
            ("card.html?id=sk-0001", "card.html"),
            ("entry.html?code=A5", "entry.html"),
            ("facet.html?code=S1", "facet.html"),
            ("reads.html", "reads.html"),
            ("taxonomy.html", "taxonomy.html")]
    if slug:
        urls.append(("topic.html?slug=%s" % slug, "topic.html"))
    if args.quick:
        urls = urls[:3]
    bad_a11y = []
    for u, label in urls:
        rc, out = run([sys.executable, A11Y, "http://127.0.0.1:%d/%s" % (port, u)])
        if rc != 0 or "干净" not in out:
            bad_a11y.append((label, out.strip().splitlines()[-5:]))
    httpd.shutdown()
    print("无障碍（axe，带参真页面）：%d 页，%d 页有问题" % (len(urls), len(bad_a11y)))
    for name, lines in bad_a11y[:5]:
        print("   ✗ %s" % name)
        for ln in lines:
            print("      " + ln.strip())

    if bad_markup or bad_a11y:
        print("\n渲染层闸门：**未通过**")
        return 1
    print("\n渲染层闸门：全部通过（HTML 合法性 + 无障碍）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
