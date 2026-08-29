---
{
  "id": "3665a2dd-8276-8084-921f-e9485a0b2103",
  "url": "https://app.notion.com/p/3665a2dd82768084921fe9485a0b2103",
  "created_time": "2026-05-20T07:59:00.000Z",
  "last_edited_time": "2026-05-20T08:14:00.000Z"
}
---

#  元素的定位与合并

# 指定元素位置
可以通过网格线（Grid Lines）的编号来指定元素的位置。
### 属性
- grid-column-start:指定列开始网格线
- grid-column-end: 指定列结束网格线
- grid-row-start:  指定行开始网格线
- grid-row-end: 指定行结束网格线
或使用简写属性↓
- grid-column: 列开始线 和 结束线
- grid-row: 行开始线 和 结束线
### 值
grid-column-start/grid-column-end/grid-row-start/grid-row-end：
- 网格线序号（从左往右数，从1开始）
grid-column/grid-row:
- 序号/序号
# 合并单元格
Grid （网格布局）可以让一个元素跨越多个格子（合并单元格）
**合并单元格需要在内部嵌套的盒子中设置属性↓**
### 属性
grid-column：声明从哪合并到哪
### 值
- `网格线序号/网格线序号`
- `span 数字`：从当前位置跨几个格子
ps：网格线序号可以是负数，负数是倒着数
