---
{
  "id": "3de5a2dd-8276-808a-a9a4-ed1c0d5d6f29",
  "url": "https://app.notion.com/p/3de5a2dd8276808aa9a4ed1c0d5d6f29",
  "created_time": "2026-09-17T11:50:00.000Z",
  "last_edited_time": "2026-09-17T12:12:00.000Z"
}
---

#  数组工具类

在Java中操作数组还得遍历，非常麻烦，因此Java提供了数组工具类用来便捷操作数组
# 数组工具类（Arrays类）
Arrays类可以直接调用，不用写包名（Arrays类属于java.util包，而编译器会自动`import java.util.*`）
### 打印/转字符串
| **方法** | **说明** | **示例** |
| --- | --- | --- |
| `toString(arr)` | 一维数组转字符串，格式 `[1, 2, 3]` | `Arrays.toString(new int[]{1,2})` → `[1, 2]` |
| `deepToString(arr)` | **嵌套数组**转字符串，递归处理 |  |
PS：查看数组要么遍历，要么`toString(arr)` 不能直接println，否则会显示哈希地址
### 排序
| **方法** | **说明** |
| --- | --- |
| `sort(arr)` | 升序排序（基本类型用**双轴快排**，对象用 **TimSort**）**oracle.com** |
| `sort(arr, from, to)` | 只排序 `[from, to)` 范围 |
| `sort(objArr, comparator)` | 对象数组按自定义比较器排序 |
| `parallelSort(arr)` | **并行排序**（Fork/Join，大数组更快） |
### 查找
| **方法** | **说明** | **示例** |
| --- | --- | --- |
| `binarySearch(arr, key)` | **二分查找**，返回下标 | — |
| `binarySearch(arr, from, to, key)` | 指定范围内查找 | — |
| `binarySearch(objArr, key, comparator)` | 按自定义比较器查找 |  |
PS：
1. **数组必须先排好序**，否则结果是垃圾值
1. **找不到时不返回 -1**，而是返回 `(插入点) - 1`
1. 找到多个相同值时，返回哪个下标不确定
### 填充
| **方法** | **说明** | **示例** |
| --- | --- | --- |
| `fill(arr, val)` | 全部元素填充为 val | `Arrays.fill(a, 0)` |
| `fill(arr, from, to, val)` | 填充 `[from, to)` 范围 |  |
### 拷贝
| **方法** | **说明** | **备注** |
| --- | --- | --- |
| `copyOf(arr, newLen)` | 拷贝到指定长度 | 变长补默认值，变短截断 |
| `copyOfRange(arr, from, to)` | 拷贝 `[from, to)` 范围 | 相当于字符串的 `substring` |
| `System.arraycopy(src, srcPos, dest, destPos, len)` | 底层 native 拷贝 |  |
### 比较
| **方法** | **说明** |
| --- | --- |
| `equals(arr1, arr2)` | 长度和每个元素都相等才返回 true |
| `deepEquals(arr1, arr2)` | **嵌套数组**深度比较 |
| `compare(arr1, arr2)` | 字典序比较，返回负/零/正 |
| `mismatch(arr1, arr2)` | 返回第一个不同处的下标，全同返回 -1 |
PS：**`==`**** 比较的是地址，****`equals`**** 才比较内容**
### 转list（后面介绍list）
| **方法** | **说明** |
| --- | --- |
| `asList(T... a)` | 数组转 List |
### 其他
| **方法** | **说明** | **版本** |
| --- | --- | --- |
| `hashCode(arr)` / `deepHashCode(arr)` | 计算数组哈希值 | — |
| `stream(arr)` | 数组转 Stream，可用函数式处理 | JDK 8 |
| `setAll(arr, generator)` | 按公式批量赋值 | JDK 8 |
| `spliterator(arr)` | 可拆分迭代器（并行用） |  |
