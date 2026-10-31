---
{
  "id": "3f65a2dd-8276-8032-82c3-eeb3e9aa3cc6",
  "url": "https://app.notion.com/p/Collections-3f65a2dd8276803282c3eeb3e9aa3cc6",
  "created_time": "2026-10-11T08:42:00.000Z",
  "last_edited_time": "2026-10-11T09:06:00.000Z"
}
---

#  **Collections工具类**

我们知道，集合框架的设计分为三层：接口（定义行为），实现类（实现接口），通用算法（将实现类组合起来，做成一些常用算法）
**java.util.Collections** 就是第三层，Java集合框架的通用算法

PS：我们前面提到的自然排序**`sort()`**方法就是由**`Collections`**类定义

## 常用的集合算法(方法)：
| 算法分类 | 方法名 | 功能描述 |
| --- | --- | --- |
| 排序 | sort() | 对 List 进行升序排序 |
| 混排 | shuffle() | 随机打乱 List 中元素的顺序 |
| 反转 | reverse() | 反转 List 中元素的顺序 |
| 二分查找 | binarySearch() | 在有序 List 中二分查找指定元素 |
| 填充 | fill() | 用指定元素替换 List 中的所有元素 |
| 复制 | copy() | 将一个 List 的元素复制到另一个 List |
| 最大/最小值 | max() / min() | 返回集合中的最大或最小元素 |
| 统计频次 | frequency() | 返回指定元素在集合中出现的次数 |
| 不相交判断 | disjoint() | 判断两个集合是否有公共元素 |
| 不可变集合 | unmodifiableXxx() | 返回集合的只读视图 |
| 线程安全 | synchronizedXxx() | 返回线程安全的集合包装 |
上一节我们已经以sort() 方法为例演示了集合框架通用算法的调用，其他方法的使用都与之类似，**作为开发者只需要关心方法传入什么，返回什么即可**
用的时候查，不详细说了
