---
{
  "id": "3b35a2dd-8276-806b-a9d4-cfe0b32d3698",
  "url": "https://app.notion.com/p/Object-3b35a2dd8276806ba9d4cfe0b32d3698",
  "created_time": "2026-08-05T12:01:00.000Z",
  "last_edited_time": "2026-08-05T12:59:00.000Z"
}
---

#  顶层Object类

除非手动指定要继承的类，否则所有类都默认继承Object类
换一种说法，所有类的顶层都是Object类
# 重要特性
> 方法参数如果是父类类型，那么可以接收这个父类本身的对象，也可以接收所有子类对象。
人话：如果一个方法希望传入一个父类的对象，那传入子类的对象也是允许的
```java
/*方法*/
void main (Father a){
}//方法期望传入父类对象
```
```java
/*父类*/
public class Father{
}

/*子类*/
public class Son extends Father{
}
```
```java
/*方法调用*/
对象名.test(new Father()); //✅方法传入父类对象
对象名.test(new Son()); //✅方法法传入子类对象
```
