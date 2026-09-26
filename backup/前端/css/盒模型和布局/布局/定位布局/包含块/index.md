---
{
  "id": "3645a2dd-8276-8091-bb55-ea4e049ed150",
  "url": "https://app.notion.com/p/3645a2dd82768091bb55ea4e049ed150",
  "created_time": "2026-05-18T09:33:00.000Z",
  "last_edited_time": "2026-05-18T09:41:00.000Z"
}
---

#  包含块

css的部分属性计算不基于父盒子，而是基于“包含块”
## 有哪些属性？
- 尺寸（Size）：当元素的 width, height, padding, margin 设置为百分比（%）时，这些值是相对于包含块计算的。
- 定位（Position）：当元素使用绝对定位（absolute）或固定定位（fixed）时，它的偏移属性（top, right, bottom, left）是相对于包含块的边缘进行
## 如何确定包含块？
1. 静态与相对定位 ：父元素就是包含块
1. 绝对定位：找最近的position 值不为 static 的祖先元素的内边距区域，如果所有祖先元素都没有设置定位，这个初始包含块通常就是浏览器窗口
1. 固定定位 :它的包含块始终是视口
