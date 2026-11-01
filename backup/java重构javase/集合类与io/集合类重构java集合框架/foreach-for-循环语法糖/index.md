---
{
  "id": "3e85a2dd-8276-80fd-aea1-e35aeb5b0e87",
  "url": "https://app.notion.com/p/foreach-for-3e85a2dd827680fdaea1e35aeb5b0e87",
  "created_time": "2026-09-27T07:57:00.000Z",
  "last_edited_time": "2026-09-27T08:01:00.000Z"
}
---

#  **foreach（ for 循环）语法糖**

`foreach` 是一种用于遍历集合/数组的循环语法，和for循环没有本质区别
是一种语法糖（for循环针对集合/数组的简便写法）
## **基本语法**
```plain text
for (元素类型 变量名 : 待遍历的对象) {
    // 循环体，变量代表当前元素
}
```
冒号 `:` 左边是**临时变量的声明**，右边是**要遍历的目标**。
# 示例
```java
// 遍历数组
int[] arr = {1, 2, 3};
for (int num : arr) {
    System.out.println(num);
}
```
