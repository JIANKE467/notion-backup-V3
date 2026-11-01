---
{
  "id": "3db5a2dd-8276-803c-843a-fe737578906d",
  "url": "https://app.notion.com/p/3db5a2dd8276803c843afe737578906d",
  "created_time": "2026-09-14T09:41:00.000Z",
  "last_edited_time": "2026-09-14T09:59:00.000Z"
}
---

#  方法引用

方法引用是基于上一节Lambda表达式的基础上的
方法引用就是将一个已在别处实现的方法，直接作为接口中抽象方法的实现（需要方法定义一致）
### 用代码说明
```java
//接口定义
public interface Study {
    int sum(int a, int b);   //待实现的求和方法
}
```
```java
//在别处实现的求和方法
public class Other{
	public static int plus(int a, int b){
		return a+b;
		}
}
```
```java
//用匿名内部类实现接口（Lambda写法）
Studay studay = (int a, int b)->Other.plus(a,b)
```
直接在箭头右侧写上相关方法的引用即可
