/* 前端运行配置（可安全提交）。
 *
 * apiBase：后端 API 的地址。
 *   - 留空 "" → 与页面同源（页面由 FastAPI 进程托管时用这个：uvicorn api.main:app）
 *   - 填地址   → 页面在 GitHub Pages、后端在别处时用这个
 *
 * 当前值指向已部署的 Cloudflare Worker（2026-09-09 部署，账号 Tylorwang671）。
 * 注意：*.workers.dev 在中国大陆网络通常被 DNS 污染/SNI 屏蔽；
 *   web/search.html 在后端不可达时会**自动回退到本地静态分片检索**（data/index.json + data/search/all.json），
 *   因此这个地址在国内打不开也不会让页面失效。
 * 若日后绑定自定义域名（cloudflare/wrangler.toml 的 routes），把这里换成自定义域名即可。
 */
window.KB_CONFIG = {
  apiBase: "https://suk-kb-api.suk-kb.workers.dev"
};
