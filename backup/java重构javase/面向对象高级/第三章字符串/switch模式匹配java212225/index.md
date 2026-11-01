---
{
  "id": "3d75a2dd-8276-80d2-80be-f4f35a7e902c",
  "url": "https://app.notion.com/p/Switch-Java21-22-25-3d75a2dd827680d280bef4f35a7e902c",
  "created_time": "2026-09-10T08:50:00.000Z",
  "last_edited_time": "2026-09-10T08:59:00.000Z"
}
---

#  Switch模式匹配（Java21/22/25）

**这节是复制的，而且太新了，有部分还是预览功能，看看就好，不重要**

前面我们介绍了switch表达式，相比传统的switch语法，它可以非常方便地实现分支判断和结果返回：
```java
public static Integer test(String str) {
    return switch (str) {  //直接使用switch表达式的结果作为返回值
        case "A" -> 1;
        case "B" -> 2;
        default -> 0;
    };
}
```
在Java 14中对switch进行了进一步增强，引入了模式匹配，可以直接判断目标类型，此功能最终在Java 21实装。原来我们如果要实现类型判断的分支语句，需要像这样编写：
```java
if(obj instanceof String) {
    System.out.println("String");
} else if(obj instanceof Integer){
    System.out.println("Integer");
} else {
    System.out.println("Other");
}
```
现在switc支持模式匹配后，我们可以像这样编写：
```java
public static void test(Object obj) {
    String type = switch (obj) {
        case String s -> "String";   //直接在case后写上类型和变量名称即可进行类型匹配
        case Integer i -> "Integer";
        case null -> "Null";   //甚至还可以直接判断null
        default -> "Other";
    };
    System.out.println(type);
}
```
我们注意到，模式匹配中的类型后面必须跟一个变量名字，哪怕我根本就不用它，这似乎有点鸡肋，能否有一种办法省略掉呢？在Java 22之后，我们可以使用`_`下划线来直接取代，表示这是一个后续不会使用的未命名的变量：
```java
String type = switch (obj) {
    case String _ -> "String";   //直接使用_表示未命名变量
    case Integer _ -> "Integer";
    case null -> "Null";
    default -> "Other";
};
```
还新增了when守卫条件，对记录类内部成员的类型嵌套匹配
