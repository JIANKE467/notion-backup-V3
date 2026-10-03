---
{
  "id": "3665a2dd-8276-80b3-8ebb-f832b1f2f957",
  "url": "https://app.notion.com/p/3665a2dd827680b38ebbf832b1f2f957",
  "created_time": "2026-05-20T09:39:00.000Z",
  "last_edited_time": "2026-05-23T09:11:00.000Z"
}
---

#  弹性布局

Flex布局是目前Web开发中使用最广泛、最流行的布局方式，使用弹性布局，需要先将父容器的display属性的值设置为flex
> 采用弹性布局，盒子会呈线性排列，无论是块级还是行内元素，并且即使是块级元素，也会直接无视其排斥特性。
- 弹性布局默认会将所有元素挤到同一行（不换行）
- 当一行元素过多，放不下时，子元素宽度会被强行压缩
- 可以使用flex-wrap属性来控制当展示不下时是否自动换行（避免了强行压缩）
## 属性
display：用于控制盒子的展示效果（块级？行内？网格？）
flex-wrap：是否自动换行
## 值
display：
- grid：网格（块级样式）
- inline-grid：网格（行内样式）
- inline：行内
- block：块级
- flex：弹性布局（块级样式）
- inline-flex：弹性布局（行内样式）

flex-wrap：
- wrap：换行
- nowrap（默认）：不换行
- wrap-reverse：换行，但交叉轴方向相反
[对齐方式](对齐方式/index.md)
  Flexbox 的核心在于它引入了两个非常重要的概念：主轴（Main Axis） 和 交叉轴（Cross Axis）
  - **主轴（Main Axis）**：Flex项目排列的主要方向，默认是水平从左到右。
  - **交叉轴（Cross Axis）**：与主轴垂直的方向，如果主轴是水平的，交叉轴就是垂直的。
  ## 属性
  `flex-direction`属性：改变主轴方向
  **`justify-content`** ：控制 **主轴 (Main Axis)** 上的对齐。
  **`align-content`**：控制 **交叉轴 (Cross Axis)** 上的对齐。
  ## 值
  flex-direction：
  - `row` (默认值): 主轴为水平方向，起点在左端。
  - `row-reverse`: 主轴为水平方向，起点在右端。（项目从右向左排）
  - `column`: 主轴为垂直方向，起点在上沿。
  - `column-reverse`: 主轴为垂直方向，起点在下沿。（项目从下向上排）

  justify/align-content：
  - `flex-start/start` (默认值): 从主轴起点开始对齐。
  - `flex-end/end`: 从主轴终点开始对齐。
  - `center`: 在主轴上居中对齐。
  - `space-between`: 优先两端对齐，项目之间的间隔都相等。第一个项目贴近起点，最后一个项目贴近终点。
  - `space-around`: 每个项目两侧的间隔相等。所以，项目之间的间隔比项目与边框的间隔大一倍。
  - `space-evenly`: 所有项目之间的间隔，以及项目与边框的间隔，都完全相等。

  ## PS
  主轴上只有`justify-content`属性
  交叉轴上有`align-content`，`align-items`，`align-self`三种属性
  类似于： [网格对齐](https://app.notion.com/p/3665a2dd827680e18b32fe179afbe6d4) 
  align-content要配合换行（flex-wrap属性）使用
[空间分配](空间分配/index.md)
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
