---
{
  "id": "3b95a2dd-8276-808c-b076-e01aa95d4013",
  "url": "https://app.notion.com/p/Java8-3b95a2dd8276808cb076e01aa95d4013",
  "created_time": "2026-08-11T12:28:00.000Z",
  "last_edited_time": "2026-08-11T12:38:00.000Z"
}
---

#  （Java8）接口的默认和静态方法

# 接口的默认实现
相较于先前接口中只能写方法头，从Java8开始接口添加了以下新特性
- 可以写方法的默认实现（用default关键字修饰）
```java
public interface Study {
    default void test() {   //使用default关键字为接口中的方法添加默认实现
        System.out.println("我是默认实现");
    }
}
```
- 如果方法在接口中有默认实现，则子类中可以不实现（不强制）
- 可以写静态方法和静态变量
# 调用接口中的静态成员
语法：
```java
接口名.成员名
```
