---
{
  "id": "3665a2dd-8276-80ee-80fb-e68f4afa0522",
  "url": "https://app.notion.com/p/3665a2dd827680ee80fbe68f4afa0522",
  "created_time": "2026-05-20T06:54:00.000Z",
  "last_edited_time": "2026-05-20T07:58:00.000Z"
}
---

#  显式网格和隐式网格

网格结构有两种创建策略，显示网格和隐式网格
## 显式网格
显式网格就是你在容器中明确定义了几行几列，浏览器直接按你声明的行列创建
## 隐式网格
没在容器中明确定义行列，或容器内元素超出原定的行列数时，浏览器的默认网格创建策略
## 逻辑
当你的子元素超过了你定义的显式网格范围或没定义，CSS 会自动帮你“补网格”，这部分就是隐式网格。
## 属性
- grid-auto-rows ：控制自动生成的行（隐式行）有多高
- grid-auto-columns ：控制自动生成的列（隐式列）有多宽
- grid-auto-flow：修改填充顺序（横向/纵向）和隐式行扩展方向（横向/纵向）
## 值
grid-auto-rows ：
- 像素
grid-auto-columns ：
- 像素
grid-auto-flow：
- row：横向排列，纵向扩展
- column：纵向排列，横向扩展
## ps
grid-auto-rows 和grid-auto-columns 属性只定义扩展行列的尺寸，不能改变原有显示网格的尺寸
