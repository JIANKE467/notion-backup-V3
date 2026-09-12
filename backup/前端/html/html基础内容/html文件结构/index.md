---
{
  "id": "3585a2dd-8276-8021-9ed4-e3f36252bd51",
  "url": "https://app.notion.com/p/HTML-3585a2dd827680219ed4e3f36252bd51",
  "created_time": "2026-05-06T08:04:00.000Z",
  "last_edited_time": "2026-05-08T07:50:00.000Z"
}
---

#  HTML文件结构

```html
<!DOCTYPE html>
<html lang="zh">
  <head>
  </head>
  <body>
  </body>
</html>
```
这就是基础HTML文件结构
## 解释
`<!DOCTYPE html>`：声明文档类型和HTML版本
`<html>`：双标签，这个网页的所有信息被这个标签包住
`<head>`：双标签，页头内容，定义网页的基本信息，如标题、介绍、特殊信息。一般不会在这里编写网页中需要展示的内容
`<body>`：双标签，页身，几乎所有页面中需要展示的内容都在这里编写
## 页头标签<head>
页头有哪些标签可用？（这里只介绍两种）
`<title>`：双标签，声明网页的标题
`<meta>`：单标签，定义页面的特殊信息，如页面的关键字，页面的描述以及一些针对于搜索引擎的属性等
举个例子：
```html
<meta charset="UTF-8">
```
这个不用死记，知道原理，可以查权威文档：
https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/meta/name
## 页身标签
只介绍一个
<div>：双标签，盒子标签，是个容器
