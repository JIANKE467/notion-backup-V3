---
{
  "id": "3725a2dd-8276-80f0-aaa3-c0ce433c68cf",
  "url": "https://app.notion.com/p/3725a2dd827680f0aaa3c0ce433c68cf",
  "created_time": "2026-06-01T03:34:00.000Z",
  "last_edited_time": "2026-06-01T03:41:00.000Z"
}
---

#  精灵图

精灵图（也称“雪碧图”）是一种网页图片应用处理方式。它将一个页面涉及到的所有零星图片都包含到一张大图中，然后利用 CSS 的 `background-image`、`background-position` 和 `width`、`height` 属性来显示大图中的特定部分。
> 优点：通过将多个图片合并成一张，减少了HTTP请求的数量，从而加快了页面加载速度。
```css
.vip-icon {
  display: inline-block;
  width: 40px;
  height: 40px;
  background-position: -57px 0;
  background-image: url("/img/sprites.png");
}
```
属性都是学过的，详见 [背景设置](https://app.notion.com/p/3625a2dd82768087a010eb4a876d0c08)
