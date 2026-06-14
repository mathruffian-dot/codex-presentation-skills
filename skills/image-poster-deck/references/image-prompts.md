# 圖片型投影片提示規格

每頁提示至少包含：

```text
Use case: scientific-educational 或 productivity-visual
Asset type: 16:9 full-slide presentation image
Primary request: 本頁要傳達的主張
Scene/backdrop: 場景與視覺隱喻
Style/medium: 插畫、攝影、紙雕、電影感等
Composition/framing: 主體位置、文字區與視覺動線
Color palette: 全份簡報共用色彩
Text (verbatim): "精確短句"
Constraints: 文字必須逐字正確、可投影閱讀
Avoid: 額外文字、亂碼、浮水印、假 logo、過度裝飾
```

## 範例

```text
Use case: scientific-educational
Asset type: 16:9 full-slide presentation image
Primary request: 呈現「不能只看答對率判斷試題品質」
Scene/backdrop: 教育研究者站在兩張大型數據圖表之間，左側是 80% 答對率，右側是高低分組差異
Style/medium: 精緻扁平插畫，學術但親近
Composition/framing: 中央人物，左右圖表形成比較，底部保留乾淨空間
Color palette: 米白、藍綠、橘色
Text (verbatim): "好題目，不只看答對率"
Constraints: 只出現指定中文，16:9，文字巨大清楚
Avoid: 額外文字、英文字、亂碼、浮水印、logo、密集數字
```

## 無法精準生字時

不要反覆要求模型生成長中文。縮短文字，或改用 `image-editable-deck`。
