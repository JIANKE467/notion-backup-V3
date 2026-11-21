---
{
  "id": "3615a2dd-8276-8083-bb1b-dcf4f1e8e9a4",
  "url": "https://app.notion.com/p/3615a2dd82768083bb1bdcf4f1e8e9a4",
  "created_time": "2026-05-15T07:21:00.000Z",
  "last_edited_time": "2026-05-15T07:31:00.000Z"
}
---

#  对齐方式

## 属性
text-align
## 值
- start：如果内容方向是左至右，则等于 left，反之则为 right。
- end：如果内容方向是左至右，则等于 right，反之则为 left。
- left：行内内容向左侧边对齐。
- right：行内内容向右侧边对齐。
- center：行内内容居中。
- justify：文字向两侧对齐，对于非等宽字体不会搞得一侧是锯齿状，对最后一行无效。
- justify-all：和 justify 一致，但是强制使最后一行两端对齐。
- match-parent：和 inherit 类似，区别在于 start 和 end 的值根据父元素的书写方向确定，并被替换为恰当的 left 或 right 值。
## PS
**text-align属性只能添加到块级元素中，并对其中的行内元素生效**
不能添加到行内元素中（因为行内元素占据的空间本身就是内容的宽度，没有多余的空间来让其对齐）
