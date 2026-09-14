param(
  [int]$Port = 8123,
  [switch]$SkipCensus
)
# ASCII-ONLY ON PURPOSE: Windows PowerShell 5.1 reads a BOM-less .ps1 as ANSI,
# so any Chinese comment in this file would come out as mojibake.
#
# Runs the authoritative browser regression for the knowledge base:
#   1. serve the repo root over http (the pages fetch web/data/*.json)
#   2. verify-hardened.mjs        -- 24 behavioural / data / contrast checks
#   3. verify-contrast-census.mjs -- 3 themes x 7 pages text contrast census
# Results land in tools/web-audit/out/*.json (gitignored).
# Exit code: 0 all pass, 2 some check failed, 1 the harness itself broke.

$ErrorActionPreference = 'Continue'
$env:PYTHONIOENCODING = 'utf-8'
$OutputEncoding = [Text.Encoding]::UTF8
[Console]::OutputEncoding = [Text.Encoding]::UTF8

$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
Set-Location $RepoRoot
$Py = if ($env:KB_PYTHON) { $env:KB_PYTHON } else { 'D:\python\python.exe' }
if (-not (Test-Path $Py)) { $Py = 'python' }

$env:AUDIT_BASE = "http://127.0.0.1:$Port/"
$srv = Start-Process -FilePath $Py -ArgumentList '-m', 'http.server', "$Port" `
  -WorkingDirectory $RepoRoot -PassThru -WindowStyle Hidden

$worst = 0
try {
  $up = $false
  for ($i = 0; $i -lt 25; $i++) {
    Start-Sleep -Milliseconds 400
    try {
      $null = Invoke-WebRequest -Uri "$($env:AUDIT_BASE)web/index.html" -UseBasicParsing -TimeoutSec 3
      $up = $true; break
    } catch {}
  }
  if (-not $up) { Write-Output "FAILED: static server did not come up on port $Port"; exit 1 }
  Write-Output "repo root : $RepoRoot"
  Write-Output "server    : $($env:AUDIT_BASE)"

  $targets = @('tools\web-audit\verify-hardened.mjs',
               'tools\web-audit\scan-hidden-content.mjs')
  if (-not $SkipCensus) { $targets += 'tools\web-audit\verify-contrast-census.mjs' }

  foreach ($t in $targets) {
    Write-Output ''
    Write-Output "=== $t ==="
    node $t 2>&1
    $code = $LASTEXITCODE
    Write-Output ("node exit: {0}" -f $code)
    if ($code -ne 0 -and $worst -eq 0) { $worst = $code }
  }
} finally {
  if ($srv -and -not $srv.HasExited) { Stop-Process -Id $srv.Id -Force; Write-Output 'server stopped' }
}

Write-Output ''
if ($worst -eq 0) { Write-Output 'WEB AUDIT: ALL OK' } else { Write-Output "WEB AUDIT: FAILED (exit $worst)" }
exit $worst
