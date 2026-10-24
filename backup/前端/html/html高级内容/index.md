---
{
  "id": "35a5a2dd-8276-80c0-92a8-f5da96f8c454",
  "url": "https://app.notion.com/p/html-35a5a2dd827680c092a8f5da96f8c454",
  "created_time": "2026-05-08T07:52:00.000Z",
  "last_edited_time": "2026-05-10T07:47:00.000Z"
}
---

#  html高级内容


[html表单](html表单/index.md)
  ## 表单
    `<form>`标签定义表单（双标签）
    可在其内部嵌套组件
    ### 属性
    > action：指定表单数据提交的目标 URL。
      method：指定表单提交方法。常用值包括 GET 和 POST。
      enctype：指定表单数据编码类型，特别是在文件上传时。常用值包括 application/x-www-form-urlencoded、multipart/form-data 和 text/plain。
      target：指定表单提交后响应的目标窗口或框架。常用值包括 _self、_blank、_parent和 _top。
      name：为表单指定名称，便于在 JavaScript 中引用。
      id：为表单指定唯一标识符，便于在 CSS 和 JavaScript 中引用。
      autocomplete：指定表单是否启用自动完成功能。取值可以是 on 或 off。
      novalidate：禁用表单的默认验证。
  ## 输入框
    `<input>`标签定义输入框（单标签）（表单最常嵌套组件）
    ### `<input>`标签属性
    `value`属性：设置输入框自带的值（默认值）
    `size`属性：控制输入框的长度
    `maxlength`属性：限制输入文本最大长度
    `placeholder`属性：输入框提示信息
    `disbaled`属性：关闭输入框（布尔属性，无值）
    `readonly`属性：输入框设成只读（布尔属性，无值）
    `type`属性：设置输入类型，有以下值↓
    > 
      email：电子邮件地址输入，支持格式验证
      url：URL输入，支持格式验证
      tel：电话号码输入
      number：数字输入，可以使用上下箭头进行增减
      range：范围输入，通常以滑块形式呈现
      date：日期选择输入，通常显示日期选择器
      time：时间选择输入，通常显示时间选择器
      datetime-local：本地日期和时间输入
      month：月份选择输入
      week：周选择输入
      color：颜色选择输入，通常显示颜色选择器
      file：文件选择输入，允许用户上传文件
      hidden：隐藏输入，不在页面上显示
      search：搜索框输入，通常在样式上有所不同
      button：普通按钮
      submit：提交按钮
      reset：重置按钮
[表单提交](表单提交/index.md)
  ## `<label>`标签
    <label>标签：语义化标签（双标签），它可以和输入框绑定（嵌套进去/使用for属性+对应id）

    作用：
    - 点击文字也能选中输入框
    - 提高表单可访问性（无障碍）

    不用<label>标签不影响页面，但编辑器有警告
  ## 向后端传输
  ### 声明提交按钮
  提交按钮有两种声明方法↓
  1. <input>标签的type属性设为submit（会自动变成一个提交按钮，按下就会提交其所在的表单）
  1. 使用<button>标签（双标签）（type属性设为submit）

  按钮属性↓
  type属性：值有submit（提交），reset（重置）
  ### 设置输入框属性
  记得给<input>标签设置name属性，否则点击提交不会被提交
[<input>标签type属性详细值](input标签type属性详细值/index.md)
  ## 时间选择器
  time：时间选择器
  date：日期选择器
  datetime-local：日期+时间选择器
  week：周选择器
  month：月份选择器
  ## 数字和范围选择器
  number：数字选择器（可用max属性min属性限制最大和最小值，可用step属性调整步长）
  range：数值选择器（滑块形式）
  ## 单选框和多选框
  radio：单选框
  PS：单选框注意设置value属性（传给后端的值）和name属性（同一组的单选框要使用相同的name属性），checked属性用来设置默认勾选项（布尔属性）

  checkbox：多选框
  PS：同样注意设置value属性（传给后端的值）和name属性（同一组的单选框要使用相同的name属性）
[下拉列表](下拉列表/index.md)
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
[文本域](文本域/index.md)
  <textarea>标签：声明文本域（双标签）
  ### 属性
  rows属性：控制文本域的默认行数
  col属性：控制文本域默认的列数
  maxlength属性：限制最大输入长度
  placeholder属性：提示信息
  disabled属性：关闭文本域（布尔属性）
  readonly属性：将文本域设成只读（布尔属性）
  PS：文本域的默认内容直接写到两个标签中间即可
[html矢量图](html矢量图/index.md)
  ## <svg>标签
  <svg>标签声明矢量图（双标签）
  在<svg>内嵌套xml代码（与html很接近）
  这里不详细介绍xml语法
  PS：<svg>标签实际上是声明了一个画布，这个画布默认300×150大小，超出画布的部分会被遮住不显示
  ## `<map>`标签
  `<map>`标签：声明图片映射（双标签）
  `<map>`标签配合`<img>`标签使用
  用于在图片中指定特定的区域，这些区域可以执行跳转
  `<map>`标签内嵌套`<area>`标签（图片热点区域），通过设置`<area>`标签属性定义图片的特定区域形状和大小
  ### <area>标签属性
  > shape区域形状
    coords坐标
    href点击后跳转
    alt描述文本
  PS：需要在<map>标签中定义name属性，并在对应的图片中将usemap属性设置为该值，即可完成图片映射
[无障碍](无障碍/index.md)
  我们还可以对网页做无障碍优化
  要求：
  1. 尽量使用语义化标签（这样读屏器知道当前选择的是什么组件）
  1. 如果无法使用语义化标签，可以使用一写属性使其语义化
  ### 语义化属性
  - 图片的alt属性（图片替代文本）
  - role属性：值声明当前div标签是什么东西
  - aira-*属性：声明当前组件有什么属性（如：输入框只读）
