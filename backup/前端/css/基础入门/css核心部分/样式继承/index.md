---
{
  "id": "35f5a2dd-8276-80b5-8be1-fd37f3fe60d3",
  "url": "https://app.notion.com/p/35f5a2dd827680b58be1fd37f3fe60d3",
  "created_time": "2026-05-13T07:43:00.000Z",
  "last_edited_time": "2026-05-13T08:07:00.000Z"
}
---

#  样式继承

**在嵌套标签时，子元素会自动继承父元素的部分css属性（并非全部）**
文本相关的属性，如 color, font-family, font-size, line-height, visibility, cursor 等会被继承
其他属性如盒子模型相关的 margin, padding, border, width, height 等，都不会自动继承

- 如果不想继承父元素的属性，可以手动定义子元素的属性，如
  将color属性设为 `initial`（浏览器默认）或`revert`（用户默认）
- 如果某属性不支持自动继承，可以将属性值设为`inherit`，就会继承父元素属性
