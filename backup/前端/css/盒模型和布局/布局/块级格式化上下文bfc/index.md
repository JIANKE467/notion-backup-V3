---
{
  "id": "3695a2dd-8276-801c-aa39-d7cde705fe3a",
  "url": "https://app.notion.com/p/BFC-3695a2dd8276801caa39d7cde705fe3a",
  "created_time": "2026-05-23T07:47:00.000Z",
  "last_edited_time": "2026-05-23T09:12:00.000Z"
}
---

#  块级格式化上下文BFC

## 什么是BFC容器？
BFC容器内部元素不会影响外部布局（如：不会margin折叠）
BFC可以包含浮动元素
（如：浮动元素不会导致高度塌陷）
## 如何开启BFC？
- **将容器的overflow的属性为hidden（最简单）**
还有其他开启方法↓
- 根元素 `<html>`
- 浮动元素 (元素的 `float` 属性不为 `none`)
- 绝对定位元素 (元素的 `position` 值为 `absolute` 或 `fixed`)
- `display` 值为 `inline-block`, `table-cell`, `table-caption`, `flex`, `inline-flex`, `grid` 或 `inline-grid` 的元素
- `overflow` 值不为 `visible` 的块级元素（如 `hidden`, `auto`, `scroll`)
## 效果
如：margin折叠问题
我们只需要给两个盒子都开启BFC就不会发生margin折叠
## 注意⚠️
最好是在子盒子外面套一个开启了BFC的盒子，而不是直接在子盒子打开BFC（有可能会裁切）
overflow属性：内容超出盒子后做何处理
