---
{
  "id": "3625a2dd-8276-801d-9bba-f6038197499a",
  "url": "https://app.notion.com/p/3625a2dd8276801d9bbaf6038197499a",
  "created_time": "2026-05-16T08:56:00.000Z",
  "last_edited_time": "2026-05-16T09:30:00.000Z"
}
---

#  内边距

# 总设置
## 属性
padding：设置边距大小

## 值
边距大小
- 像素
- 百分比：相对父元素宽度大小（宽高都按父元素宽度计算😓）
# 四边分别设置
## 属性
`padding-top`， `padding-right`，`padding-bottom`，`padding-left`
## 值
值同总设置
## 简写
```css
.test {  
padding: 10px;             /* 四边都是10px */  
padding: 10px 20px;        /* 上下10px，左右20px */  
padding: 10px 20px 30px;   /* 上10px，左右20px，下30px */  
padding: 10px 20px 30px 40px; /* 上10px，右20px，下30px，左40px */}
```
# 注意⚠️
给行内元素设置内边距，盒模型不参与垂直方向上的布局计算
人话：给行内元素设置内边距，外部左右的元素会被挤开，但上下的元素不会被挤开，但盒子却实实在在的被撑大了（背景变大）
