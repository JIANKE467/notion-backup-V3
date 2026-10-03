---
{
  "id": "35f5a2dd-8276-80b2-9407-c0887f61aa0c",
  "url": "https://app.notion.com/p/35f5a2dd827680b29407c0887f61aa0c",
  "created_time": "2026-05-13T08:20:00.000Z",
  "last_edited_time": "2026-05-15T06:28:00.000Z"
}
---

#  文本字体

# 指定字体
CSS使用`font-family`属性来指定字体
- 可以同时设置多种字体来增强兼容性（优先级从左向右）
```css
p {  font-family: 'Microsoft YaHei', 'PingFang SC';}
```
- 可以不指定具体字体，而是指定字体族（更有兼容性）
### 字体族：
**字体族不代表具体字体，只代表某种字体风格**
serif（衬线字体）
sans-serif（无衬线字体）
monospace（等宽字体）
cursive（手写字体）
fantasy（奇幻字体）
# 自定义字体
使用`@font-face`做选择器名来创建自定义字体：
需要指定属性↓
`font-family`字体名称
 `src`字体地址
```css
@font-face {  
font-family: 'YuanShen';  
src: url("../font/yuanshen.ttf");  
/* 使用url("")函数来指定位置，注意这个不一定是本地文件，甚至可以是一个网络文件 */
}
```
# 注意
字体属性会被自动继承
