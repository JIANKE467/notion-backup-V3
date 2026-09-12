---
{
  "id": "3685a2dd-8276-80c3-aec4-c9d113222de5",
  "url": "https://app.notion.com/p/3685a2dd827680c3aec4c9d113222de5",
  "created_time": "2026-05-22T08:08:00.000Z",
  "last_edited_time": "2026-05-23T07:10:00.000Z"
}
---

#  对齐方式

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
