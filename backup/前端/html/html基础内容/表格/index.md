---
{
  "id": "35a5a2dd-8276-8068-9dbe-e834354a456d",
  "url": "https://app.notion.com/p/35a5a2dd827680689dbee834354a456d",
  "created_time": "2026-05-08T06:58:00.000Z",
  "last_edited_time": "2026-05-08T07:52:00.000Z"
}
---

#  表格

表格通过嵌套标签的方式编写
## 基础表格
  `<table>`标签定义表格（双标签）
  `<caption>`标签定义表格名称（双标签）
  `<tr>`标签定义行（双标签）
  `<td>`标签定义单元格（双标签）
  `<th>`标签定义表头单元格（双标签）（与td使用方法一致）
  ```html
<table border="1">
  <caption>2025年装机清单</caption>
  <tr>
    <th>配件名称</th>
    <th>型号</th>
  </tr>
  <tr>
    <td>CPU</td>
    <td>Ultra9 285K</td>
  </tr>
  <tr>
    <td>显卡</td>
    <td>RTX4090</td>
  </tr>
</table>
  ```
  ### `<table>`标签属性
  `border`属性：其值定义边框宽度（单位像素）（默认0）
  `width`属性：控制表格宽度
  `cellspacing`属性：控制单元格间距
  `bgcolor`属性：设置表格颜色
## 高级用法（合并单元格）
  ### <td>标签属性
  `colspan`属性：横向合并单元格（值为从左到右占据单元格数）
  `rowspan`属性：纵向合并单元格（值为从上到下占据单元格数）
## 表格语义化
  用`<thead>`标签嵌套表头
  用`<tbody>`标签嵌套表身
  用`<tfoot>`标签嵌套表脚
  这三个标签没什么用，将对应的代码段放进去可以提高可读性和语义化
