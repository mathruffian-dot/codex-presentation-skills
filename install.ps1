param(
    [string]$TargetRoot = (Join-Path $HOME ".codex\skills")
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSCommandPath
$sourceRoot = Join-Path $repoRoot "skills"
$skillNames = @(
    "pptx-teaching-deck",
    "html-slide-deck",
    "image-poster-deck",
    "image-editable-deck"
)

New-Item -ItemType Directory -Force -Path $TargetRoot | Out-Null

foreach ($name in $skillNames) {
    $source = Join-Path $sourceRoot $name
    $target = Join-Path $TargetRoot $name

    if (-not (Test-Path -LiteralPath $source)) {
        throw "找不到 Skill：$source"
    }

    if (Test-Path -LiteralPath $target) {
        $backup = "$target.bak-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
        Copy-Item -LiteralPath $target -Destination $backup -Recurse
        Remove-Item -LiteralPath $target -Recurse -Force
        Write-Host "已備份：$backup"
    }

    Copy-Item -LiteralPath $source -Destination $target -Recurse
    Write-Host "已安裝：$target"
}

Write-Host ""
Write-Host "完成。請重新啟動 Codex。"
