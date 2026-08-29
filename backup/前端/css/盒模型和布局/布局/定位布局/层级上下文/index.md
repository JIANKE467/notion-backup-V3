---
{
  "id": "3655a2dd-8276-801d-9683-f2df14a5ed5b",
  "url": "https://app.notion.com/p/3655a2dd8276801d9683f2df14a5ed5b",
  "created_time": "2026-05-19T09:09:00.000Z",
  "last_edited_time": "2026-05-19T09:34:00.000Z"
}
---

#  层级上下文

## 什么是层级上下文
浏览器不是简单按 z-index 全局排序。
而是：
> 每个“堆叠上下文”内部独立排序。
可以理解成：
- 页面被分成多个“图层世界”
- 每个世界内部比 z-index
- 不同世界之间整体排序
## 谁会创建堆叠上下文
- 盒子存在非static定位，且使用了z-index属性（即使是z-index: 0）此时盒子会创建一个新的层级上下文盒子
- 使用了fixed定位（即使没有z-index），会直接创建一个新的层级上下文盒子
- 使用了sticky定位且处于粘滞状态时，会创建一个新的层级上下文
- 盒子使用了filter、perspective、clip-path、isolation: isolate和will-change属性时。
- 盒子使用了transform进行了三维变换（下一章介绍）
- 盒子使用了opacity属性改变了盒子的透明度
## 所以
**即便子层级的z-index超级大，但父层级的z-index较小，子元素仍会被压在下面**
