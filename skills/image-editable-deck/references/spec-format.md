# Plate 模式 spec.yaml

畫布為 16:9，座標單位是 PowerPoint 英吋：`13.333 × 7.5`。

```yaml
style:
  palette:
    bg: "#0D1B2A"
    primary: "#00C6FF"
    highlight: "#FFD700"
    text: "#FFFFFF"
    muted: "#A5B4CB"
    card: "#1E3A5F"
  font: "Microsoft JhengHei"
  title_font: "Microsoft JhengHei"
  body_font: "Microsoft JhengHei"

pages:
  - page: 1
    image: page_01
    img_x: 0
    img_y: 0
    img_w: 13.333
    img_h: 7.5
    blocks:
      - type: badge
        text: "研究判讀"
        x: 0.7
        y: 0.7
        w: 2.2
        h: 0.5
        bg: primary
        color: bg
        size: 14
      - type: title
        text: "好題目\n不只看答對率"
        x: 0.7
        y: 1.6
        w: 5.2
        h: 2.5
        size: 48
        color: text
        bold: true
```

支援區塊：

- `title`、`subtitle`、`body`、`highlight`、`muted`
- `badge`
- `card`
- `bar`
- `progress`
