---
{
  "id": "3f65a2dd-8276-80a8-9b03-ca15760d9d35",
  "url": "https://app.notion.com/p/jdk9-3f65a2dd827680a89b03ca15760d9d35",
  "created_time": "2026-10-11T09:10:00.000Z",
  "last_edited_time": "2026-10-11T10:14:00.000Z"
}
---

#  集合工厂方法（jdk9）

# 作用
集合工厂方法是用于快速创建内容固定（不可变）且只读的数据结构
# 特性
- 集合工厂方法是静态方法，它们定义在`List`、`Set`、`Map` 接口内部
- 用集合工厂方法创建的数据结构内容不可变，只能读不能写
# 对比
使用传统方式创建集合
```java
//先创建集合对象
List<String> list = new ArrayList<>();
//再调用add方法添加内容
list.add("a");
list.add("b");
list.add("c");
```
使用集合工厂方法
```java
List<String> list = List.of("a", "b", "c");  
// 一行写完
```
# 使用
有三种工厂方法：
### **1️⃣ ****`List.of()`**** / ****`Set.of()`**** / ****`Map.of()`**** —— 直接创建**
作用：直接创建不可变集合
使用：直接调用方法即可，别忘了这几个of方法不在List/Set/Map接口的实现类里，而是作为静态方法定义在接口内，所以直接`接口.of()`调用
传入：直接将集合元素作为参数传入
调用：方法和普通集合一样
```java
List<String> list = List.of("a", "b", "c");
Set<Integer> set = Set.of(1, 2, 3);
Map<String, Integer> map = Map.of("apple", 1, "banana", 2);
```
原理：为了加快创建速度，List/Set/Map 下有10个静态方法of()的重载（不用创建对象，元素直接作为参数传入）
注意⚠️：
- Map.of()方法最多传入10个元素，而List.of()和Set.of()则没有这个限制
- 不能传入空元素nul
### **2️⃣ ****`Map.entry()`**** +**`Map.ofEntries()`**—— 构造不可变键值对**
当Map集合超过了10个键值对就不能使用**`Map.of()`**方法，而需要使用**`Map.entry()`**** **方法
```java
Map<String, Integer> map = Map.ofEntries(
    Map.entry("apple", 1),
    Map.entry("banana", 2),
    Map.entry("cherry", 3),
    Map.entry("date", 4),
    Map.entry("elderberry", 5)
    // ...任意多对，没有数量上限
);

```
注意⚠️：
- 只有Map接口有**`entry()`**方法，List/Set接口没有该方法
- **`Map.entry()`**** 和**`Map.ofEntries()` 是搭配使用的，两个方法都不能单独使用
调用：方法和普通集合一样

### **3️⃣ ****`List.copyOf()`**** / ****`Set.copyOf()`**** / ****`Map.copyOf()`**** —— 拷贝转换（jdk10）**
作用：传入一个已有集合，返回一个它的不可变的拷贝
```java
//已创建集合
List<String> mutable = new ArrayList<>(List.of("a", "b", "c"));
```
```java
//拷贝已有集合
List<String> snapshot = List.copyOf(mutable);
```
调用：方法和普通集合一样
