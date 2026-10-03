---
{
  "id": "3665a2dd-8276-8016-a0c4-e1614dbd139a",
  "url": "https://app.notion.com/p/3665a2dd82768016a0c4e1614dbd139a",
  "created_time": "2026-05-20T09:13:00.000Z",
  "last_edited_time": "2026-05-20T09:38:00.000Z"
}
---

#  网格区域

我们可以直接利用网格快捷直观的布局，而不是用传统方法填充
## 传统网格填充方式：
1. 按顺序自动填充
1. 指定单元格的起始网格线和结束网格线（合并单元格的方法）
1. 用span指定跨几格（合并单元格的方法）
PS：说这么多其实底层只有一种填充方法：自动填充（因为第2，3种都是基于自动填充的单元格合并）
## 使用grid-template-areas属性快速填充：
```html
<div class="grid-box">
  <div class="grid-item header">1</div>
  <div class="grid-item nav">2</div>
  <div class="grid-item content">3</div>
  <div class="grid-item footer">4</div>
</div>
```

```css
.grid-box {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: 40px 140px 40px;

  grid-template-areas:
    "header header header"   /* 从上往下从左往右，编写每个格子分别属于哪个盒子，连续的两个或多个格子会自动相连 */
    "nav    content content"
    "nav    footer footer";
}
```
可以发现，该属性直接将布局较直观的表示了出来，并且省去了繁琐的合并单元格过成
**注意⚠️**
**grid-template-areas属性使用元素别名来布局，需要先给相应元素设置别名**
**使用****`grid-area`****属性**
```css
.grid-item { background-color: gray; }
.header  { grid-area: header; }
.aside { grid-area: nav; }
.main    { grid-area: content; }
.footer  { grid-area: footer; }
```
**如果某个格子想留空，可以使用点号 (.) 来表示一个空的网格单元**
