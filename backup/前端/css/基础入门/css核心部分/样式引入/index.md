---
{
  "id": "35c5a2dd-8276-808d-a800-e188894ba638",
  "url": "https://app.notion.com/p/35c5a2dd8276808da800e188894ba638",
  "created_time": "2026-05-10T08:10:00.000Z",
  "last_edited_time": "2026-06-17T06:28:00.000Z"
}
---

#  样式引入

将css样式引入html有三种方法
## 1. 直接在标签里设置style属性（内联样式）
这种方法想必很熟悉
## 2. 在同一文件内定义<style>标签（内部样式）

通过在<style>标签中设置对应的样式和需要应用的组件来批量设置
## 3. 使用外部的css文件（外部样式）
在外部文件中写好css
在HTML中使用<link>标签连接
### <link>标签
<link>标签：引入资源
### 属性
- rel：关系类型（资源应用到哪）
- href资源地址
- type资源 MIME 类型（资源文件类型）
- media适配设备
- sizes图标尺寸
PS：rel的值决定该资源是应用给图标还是样式表等…
引入css固定写法：
```html
<link rel="stylesheet" type="text/css" href="css地址">
```
# 现在常用第3种，方便维护
# 样式表优先级
内联样式 > 内部样式表 = 外部样式表 > 浏览器默认样式
