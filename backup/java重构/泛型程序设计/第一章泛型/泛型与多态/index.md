---
{
  "id": "3df5a2dd-8276-80ca-9354-f5718b41b5a3",
  "url": "https://app.notion.com/p/3df5a2dd827680ca9354f5718b41b5a3",
  "created_time": "2026-09-18T13:30:00.000Z",
  "last_edited_time": "2026-09-18T13:42:00.000Z"
}
---

#  泛型与多态

这节没有啥，主要就是讲接口，抽象类，记录类型（Java16）也可以用泛型，因为他们都是特殊的类，所以用法和类差不多（都是加到类名后面）
# 接口
定义
```java
public interface Study<T> {
    T test();
}
```
传入实际类型
```java
static class Test implements Study<Integer> {
	@Override
	...
}
```
或者继续使用泛型
```java
static class Test implements Study<T> {
	@Override
	...
}
```
# 继承
继承也一样
```java
static class Father<T> {
    
}

static class Son extends Father<String> {

}
```
