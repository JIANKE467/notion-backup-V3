---
{
  "id": "3725a2dd-8276-8024-96cf-e57e017d9a8e",
  "url": "https://app.notion.com/p/3725a2dd8276802496cfe57e017d9a8e",
  "created_time": "2026-06-01T03:42:00.000Z",
  "last_edited_time": "2026-06-01T03:58:00.000Z"
}
---

#  颜色渐变

# 属性
background-image：设置背景渐变
# 值
### 线性渐变函数：
颜色沿着一条直线过渡
**语法**
`linear-gradient(方向，颜色1 百分比, 颜色2 百分比，...)`
**最少参数写法：**
`linear-gradient(颜色1 , 颜色2 )`
例：
```css
.container {
  width: 300px;
  height: 50px;
  background-image: linear-gradient(to right, red, yellow);
}
```
**方向参数：**
| to bottom | 上 → 下（默认） |
| --- | --- |
| to top | 下 → 上 |
| to right | 左 → 右 |
| to left | 右 → 左 |
| to right bottom | 左上 → 右下 |
**还可以使用图片渐变：**
```css
background:
  linear-gradient(rgba(0,0,0,.4), rgba(0,0,0,.4)),
  url(bg.jpg);
```

- 径向渐变 函数：颜色从一个中心点向外辐射过渡
