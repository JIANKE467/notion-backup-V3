---
{
  "id": "3e85a2dd-8276-8004-8441-cebb69a5c367",
  "url": "https://app.notion.com/p/set-3e85a2dd827680048441cebb69a5c367",
  "created_time": "2026-09-27T08:12:00.000Z",
  "last_edited_time": "2026-09-30T12:01:00.000Z"
}
---

#  set接口（集合）

# set接口
作用：set接口定义了**存储不重复的元素**的数据结构【集合】（这里的集合是数学意义上的集合，而非我们之前提到的集合类也就是Java集合框架）
继承关系：`set`接口直接继承自集合根接口`Collection`
实现位置：**`AbstractCollection`**及其子类
# 注意
数据结构“集合“
- 不允许出现重复元素
- 不支持随机访问（没下标）
# Set接口定义的方法
Set接口是从Collection中直接继承的，因此，Set支持的功能其实也就和Collection中定义的差不多
同样是插入，删除等（需要自己查）
# 实现类
### **HashSet（哈希集合）**
- **底层结构**：基于 `HashMap` 实现
- **特点**：无法保证顺序，允许 `null` 元素，不支持随机访问
使用：
```java
public static void main(String[] args) {
		//创建哈希集合
    Set<String> set = new HashSet<>();
    //插入元素
    System.out.println(set.add("AAA"));
    //删除元素
    System.out.println(set.remove("AAA"));
    
    System.out.println(set);
}
```
### **LinkedHashSet**
- **底层结构**：基于 `LinkedHashMap` 实现（链表 + 哈希表）
- **特点**：维护元素的**插入顺序**
- **性能**：略低于 HashSet，迭代性能更好
使用：同上
### **TreeSet**
- **底层结构**：基于红黑树（`TreeMap`）实现
- **特点**：可排序，不允许 `null`
使用：同上
