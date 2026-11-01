---
{
  "id": "3e55a2dd-8276-8088-bc7d-ca73f9ffa12e",
  "url": "https://app.notion.com/p/3e55a2dd82768088bc7dca73f9ffa12e",
  "created_time": "2026-09-24T08:30:00.000Z",
  "last_edited_time": "2026-09-24T09:52:00.000Z"
}
---

#  集合根接口

所有集合的祖先都是集合根接口`Collection`，我们这节通过根接口了解集合的相关功能
# 说在最前面
集合依旧是创建一个对象➡️数据存在对象中➡️用类中的各种方法操作数据
# **Java 集合类与数组的区别**
**核心区别：数组是固定长度、存储基本类型与对象的基础数据结构；集合是可动态扩容、只能存储对象、提供丰富操作方法的框架体系。** 数组是语言层面的"哑"容器，集合是构建其上的"管理生态"。
# 功能
**添加功能**
| **方法** | **说明** |
| --- | --- |
| `boolean add(E e)` | 添加一个元素 |
| `boolean addAll(Collection<? extends E> c)` | 添加一个集合的所有元素 |
**删除功能**
| **方法** | **说明** |
| --- | --- |
| `boolean remove(Object o)` | 删除指定元素 |
| `boolean removeAll(Collection<?> c)` | 删除指定集合中包含的所有元素（交集） |
| `boolean removeIf(Predicate<? super E> filter)` | 根据条件删除（JDK 8+） |
| `void clear()` | 清空集合 |
**判断功能**
| **方法** | **说明** |
| --- | --- |
| `boolean contains(Object o)` | 判断是否包含指定元素 |
| `boolean containsAll(Collection<?> c)` | 判断是否包含指定集合的所有元素 |
| `boolean isEmpty()` | 判断集合是否为空 |
| `boolean equals(Object o)` | 比较相等 |
**获取功能**
| **方法** | **说明** |
| --- | --- |
| `int size()` | 返回元素个数 |
| `Iterator<E> iterator()` | 返回迭代器，用于遍历 |
| `Spliterator<E> spliterator()` | 返回可分割迭代器（并行遍历用） |
| `Stream<E> stream()` | 返回顺序流（JDK 8+） |
| `Stream<E> parallelStream()` | 返回并行流（JDK 8+） |
**转换功能**
| **方法** | **说明** |
| --- | --- |
| `Object[] toArray()` | 转成对象数组 |
| `<T> T[] toArray(T[] a)` | 转成指定类型的数组 |
**保留功能**
| **方法** | **说明** |
| --- | --- |
| `boolean retainAll(Collection<?> c)` | 保留指定集合中包含的元素（取交集 |
