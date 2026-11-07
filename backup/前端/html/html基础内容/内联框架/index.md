---
{
  "id": "35a5a2dd-8276-8053-a026-f34c5ebb2f69",
  "url": "https://app.notion.com/p/35a5a2dd82768053a026f34c5ebb2f69",
  "created_time": "2026-05-08T07:28:00.000Z",
  "last_edited_time": "2026-05-08T07:52:00.000Z"
}
---

#  内联框架

内联框架就是在一个一个页面内开一个画中画
## 内联框架
  `<iframe>`标签：声明内联框架（双标签）
## `<iframe>`标签属性
  `src`属性：指明内嵌网站的地址
  `width`和`height`属性：指定其宽高
  `frameborder`属性：是否显示内嵌网页边框（值：yes/no）
  `allowfullscreen`属性：此网站全屏展示
## 内联框架内链接跳转
  在内联框架内的链接有3种跳转方式
  这取决于`<a>`标签的`target`属性的值↓
  > `_parent`在其父级嵌套页面中跳转         
    `_top`直接在最外层跳转
    `_blank`直接打开一个新窗口
