/* 前端运行配置（可安全提交）。
 *
 * apiBase：后端 API 的地址。留空字符串表示「与页面同源」——
 *   当页面由 FastAPI 进程托管时（uvicorn api.main:app，同一端口既提供 web/ 又提供 /api/*），
 *   保持留空即可；当页面托管在 GitHub Pages、后端在别处时，填后端地址，例如：
 *   apiBase: "https://kb-api.example.workers.dev"
 *
 * 注意：把后端地址公开写在仓库里等于公开该服务的 URL，请确保后端已做限流/防滥用。
 */
window.KB_CONFIG = {
  apiBase: ""
};
