---
{
  "id": "3df5a2dd-8276-80af-8452-f5d7e823f27e",
  "url": "https://app.notion.com/p/3df5a2dd827680af8452f5d7e823f27e",
  "created_time": "2026-09-18T14:16:00.000Z",
  "last_edited_time": "2026-09-19T07:36:00.000Z"
}
---

#  泛型的界限

我们知道，泛型可以接收多种数据类型的数据，但什么都接收未免也太不安全了，因此泛型的界限就是对泛型可接收的类型的限制
# 语法
### 泛型上界
表示泛型必须是该类或该类的子类
```java
<泛型名 super 类>
```
例
```java
// 类或方法声明中使用 extends 定义上界
class Box<T extends Number> { }          // 泛型参数的上界
void print(List<? extends Number> list) { }  // 通配符上界

```
### 泛型下界
表示泛型必须是该类或该类的父类
泛型下界只能用于通配符“？”
```java
<？ super 类>
```
例
```java
void addNumbers(List<? super Integer> list) { }
```
泛型下界很少使用，且有一堆特性，可暂时忽略
