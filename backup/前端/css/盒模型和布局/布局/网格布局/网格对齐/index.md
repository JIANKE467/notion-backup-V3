---
{
  "id": "3665a2dd-8276-80e1-8b32-fe179afbe6d4",
  "url": "https://app.notion.com/p/3665a2dd827680e18b32fe179afbe6d4",
  "created_time": "2026-05-20T08:14:00.000Z",
  "last_edited_time": "2026-05-20T08:50:00.000Z"
}
---

#  网格对齐

按层级分，有三大类对齐方式
# *-content
  *-content管网格在父元素中的对齐方式
  ### 属性
  justify-content：网格在父元素行轴（横轴）上的对齐方式
  align-content：网格在父元素块轴（纵轴）上的对齐方式
  ### 值
  - stretch (默认值): 如未设置格子具体宽度，网格将拉伸以填满空间
  - start: 行轴起点（左上角）
  - end: 行轴的终点（右上角）
  - center: 行轴中心位置
  - space-between: 拉伸格子间隙，铺满行轴
  - space-around: 保证每个格子两侧的间隔相等（左右）
  - space-evenly: 保证每个格子之间的间隔一致（上下左右）
# *-self
  *-self管网格内子元素单个的对齐方式，需要在子元素中设置
  ### 属性
  justify-self：子元素行轴（横轴）对齐方式
  align-self：子元素块轴（纵轴）对齐方式
  ### 值
  - stretch（默认值）：如未设置格子具体宽高，子元素将拉伸填满网格区域
  - start：对齐到起点（左上角）
  - end：对齐到终点（右下角）
  - center：居中对齐
# *-items
  *-items管网格内所有子元素整体的对齐方式，需要在父元素中设置
  ### 属性
  justify-items：所有子元素行轴（横轴）对齐方式
  align-items：所有子元素块轴（纵轴）对齐方式
  ### 值
  - stretch（默认值）：子元素拉伸填满各自的网格区域
  - start：对齐到起点
  - end：对齐到终点
  - center：居中对齐
