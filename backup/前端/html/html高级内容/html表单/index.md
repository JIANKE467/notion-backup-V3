---
{
  "id": "35a5a2dd-8276-805a-82d1-fe7d23532d01",
  "url": "https://app.notion.com/p/html-35a5a2dd8276805a82d1fe7d23532d01",
  "created_time": "2026-05-08T07:52:00.000Z",
  "last_edited_time": "2026-05-09T12:19:00.000Z"
}
---

#  html表单

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
