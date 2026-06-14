# Codex Presentation Skills

給教師、研究者與研習講師使用的四個公開 Codex Skills。

| Skill | 用途 | 主要輸出 |
|------|------|----------|
| `pptx-teaching-deck` | 教學、研習、研究 PowerPoint | 可編輯 `.pptx`、預覽圖 |
| `html-slide-deck` | 離線、互動、網頁式簡報 | `index.html` 與本地資產 |
| `image-poster-deck` | Codex 內建生圖的整頁圖文融合簡報 | PNG 頁面、圖片型 `.pptx` |
| `image-editable-deck` | Codex 內建生圖的無字背景＋可編輯文字 | AI 背景、可編輯 `.pptx` |

圖片簡報預設使用 Codex 內建 `image_gen`，不需要另外申請或貼上 OpenAI API Key。

## 安裝

Windows PowerShell：

```powershell
git clone https://github.com/mathruffian-dot/codex-presentation-skills.git
cd codex-presentation-skills
.\install.ps1
```

安裝位置：

```text
~/.codex/skills/pptx-teaching-deck
~/.codex/skills/html-slide-deck
~/.codex/skills/image-poster-deck
~/.codex/skills/image-editable-deck
```

重新啟動 Codex 後即可使用。

也可只下載單一 Skill 資料夾，再放入 `~/.codex/skills/`。

## 使用範例

```text
使用 pptx-teaching-deck，
把這份研究摘要製作成 8 頁可編輯 PPTX，
完成後渲染並逐頁檢查文字溢出與來源。
```

```text
使用 html-slide-deck，
把這份課程內容製作成可離線開啟的 HTML 簡報，
支援方向鍵、章節選單、頁碼與列印模式，
完成後用瀏覽器逐頁測試。
```

```text
使用 image-poster-deck，
把這份課程大綱製作成 6 頁海報式圖片簡報。
使用 Codex 內建生圖，每頁只保留一個短句，
檢查中文字後再打包成 PPTX。
```

```text
使用 image-editable-deck，
為這份研究簡報生成無字 AI 背景，
所有中文、數值與圖表標籤使用可編輯 PowerPoint 物件，
完成後逐頁渲染檢查。
```

更多研習用提示見 [`examples/prompts.md`](examples/prompts.md)。

## 使用邊界

- PPTX Skill 需要 Codex 環境提供 Presentations 能力。
- HTML Skill 預設使用原生 HTML／CSS／JavaScript，可直接離線開啟。
- 圖片型 Skills 需要 Codex 環境提供內建圖片生成能力。
- 一般內建生圖不需要 API Key；只有使用者明確選擇 API／CLI 路線時才需要。
- 不應將 API key、學生個資或未公開研究資料寫入簡報。
- AI 產出仍需人工核對數值、引文、圖片授權與版面。

## 驗證

```powershell
python .\scripts\validate.py
```

GitHub Actions 會在每次 push 與 pull request 自動執行相同檢查。

## 授權

MIT
