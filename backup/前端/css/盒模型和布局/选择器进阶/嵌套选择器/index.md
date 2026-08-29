---
{
  "id": "36a5a2dd-8276-80a5-96a7-fd2dabf94cd1",
  "url": "https://app.notion.com/p/36a5a2dd827680a596a7fd2dabf94cd1",
  "created_time": "2026-05-24T08:26:00.000Z",
  "last_edited_time": "2026-05-24T08:41:00.000Z"
}
---

#  嵌套选择器

嵌套选择器就是让css支持嵌套写法（没想到吧，这东西24年前还不支持）
直接上例子：
```css
.card {
  background-color: white;
}

.card p { line-height: 1.6; }
.card a { color: blue; }
```
等价于
```css
.card {
  background-color: white;
  
  p { line-height: 1.6; }
  a { color: blue; }
}
```
## 注意⚠️
在嵌套选择器中，使用伪选择器和类选择器仍然要声明伪选择器和类选择器的父选择器
这时，我们可以使用`&`符号代表父选择器
```css
.card::before { content: "xxxx"; }
```
等价于
```css
.card {
  ::before { content: "xxxx"; }
}
```
