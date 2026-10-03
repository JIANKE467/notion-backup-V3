---
{
  "id": "3695a2dd-8276-80d2-ab4f-ea0361055004",
  "url": "https://app.notion.com/p/3695a2dd827680d2ab4fea0361055004",
  "created_time": "2026-05-23T07:11:00.000Z",
  "last_edited_time": "2026-05-23T07:25:00.000Z"
}
---

#  空间分配

这节介绍在页面空间改变时，盒子的缩放逻辑
## 属性
flex-shrink属性：制盒子缩小倍数
flex-grow属性：控制盒子放大倍数
flex-basis属性：统一控制元素在主轴上占据的空间大小
flex属性：是前面三个属性的简写
## 值
flex-shrink：
- 数字：代表盒子缩小倍数，默认1，0代表不缩小
flex-grow：
- 数字：代表盒子放大比例，默认0，0代表不放大
- 如果所有盒子的 flex-grow 都为 1，它们将平分剩余空间。
- 如果一个盒子的 flex-grow 为 2，其他盒子都为 1，那么它将获得比其他盒子多一倍的剩余空间，以此类推。
flex-basis：
- 默认值是 auto，表示盒子的大小由其内容或 width/height 属性决定。
- 也可以设置一个具体的长度值，如 100px，那么盒子在主轴上的尺寸也会自动调整为100px
flex：
```css
.flex-item {
  flex: 1 0 auto;
}
```
等价于
```css
.flex-item {
  flex-grow: 1;
  flex-shrink: 0;
  flex-basis: auto;
}
```
