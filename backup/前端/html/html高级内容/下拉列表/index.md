---
{
  "id": "35b5a2dd-8276-80dd-8ac7-f581e006c2af",
  "url": "https://app.notion.com/p/35b5a2dd827680dd8ac7f581e006c2af",
  "created_time": "2026-05-09T13:01:00.000Z",
  "last_edited_time": "2026-05-09T13:21:00.000Z"
}
---

#  下拉列表

## `<select>`标签（双标签）
  使用`<select>`标签定义下拉选择框（双标签）
  `<select>`标签要嵌套到表单里（不嵌套也行，但是没法提交）
  ### 属性
  size属性：定义显示在外面的数量
  multiple属性：决定是否可以多选（布尔属性）
  name属性：组件名称，**不设置这个没有办法向后端提交表单**
## `<option>`标签（双标签）
  <option>标签是嵌套在<select>标签中的，用来声明下拉选项
  ### 属性
  value属性：定义传给后端的值
  selected属性：默认选项
  下拉选项文本直接在option两个标签间写（直接写不用加标签）
