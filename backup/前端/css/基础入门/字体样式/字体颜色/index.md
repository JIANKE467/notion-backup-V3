---
{
  "id": "3615a2dd-8276-8056-916f-db949a6592f2",
  "url": "https://app.notion.com/p/3615a2dd82768056916fdb949a6592f2",
  "created_time": "2026-05-15T06:59:00.000Z",
  "last_edited_time": "2026-05-15T07:16:00.000Z"
}
---

#  字体颜色

## 相关属性
color：控制颜色
## 预设值
有red，blue，green…等
## RGB值
需要使用 rgb() 函数
```css
.test{
color:rgb(r值,g值,b值);
}
```
或
用16进制表示三个值↓
```css
.test{
color:#FFFFFF;
}
```
### PS
- rgb范围：0~255
- rgb表示法也可以表示阿尔法通道（透明度）：需要使用 rgba() 函数 或直接16进制表示
- 阿尔法通道范围：0~1（小数）
- α通道16进制表示时范围是：0~255
