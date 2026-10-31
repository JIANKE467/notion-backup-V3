---
{
  "id": "3625a2dd-8276-80b8-a04e-e07b69fed27a",
  "url": "https://app.notion.com/p/3625a2dd827680b8a04ee07b69fed27a",
  "created_time": "2026-05-16T08:31:00.000Z",
  "last_edited_time": "2026-05-16T09:19:00.000Z"
}
---

#  盒子边框

# 总设置
## 边框属性
border-width：控制边框的宽度
border-style：控制边框的样式
border-color：设置边框颜色
border-radius：设置边框圆角
## 值
边框宽度
- 像素

边框样式
- none - 无样式，默认值
- solid - 实线样式，一根普通的边框线，也是用的最多的一种
- dashed - 虚线形式dotted - 点线形式，一堆小点点围绕盒子
- double - 双实线形式，两条实线围绕盒子（边框宽度至少需要2-3px才能正确显示）
- ridge/groove - 相框形式，比较古老的样式，不符合现代审美

边框颜色
- rgb
- 预设值

边框圆角
- 像素：设置的圆角半径
- 百分比：圆角百分比，设置出来就是圆角被削了一部分（真丑）
# 单独设置四个边
## 属性
border-top：上边样式
border-bottom：下边样式
border-left：左边样式
border-right：右边样式
## 值
同总设置

# 注意⚠️
- `boder`是`border-width`，`border-style`，`border-color`（宽度，颜色，风格）的简写属性，可以在boder属性下写到一起
- 如果同时使用了边框总设置和单边设置，此时会按照声明的顺序进行覆盖
- `border-top`是`border-top-color`，`border-top-width`，`border-top-style`的简写（其他三个边一样是简写）
- 对于圆角的设置可以只设置某个角圆角：`border-top-left-radius：50px`
