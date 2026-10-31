---
{
  "id": "3e15a2dd-8276-8066-be69-e3b617c5504c",
  "url": "https://app.notion.com/p/3e15a2dd82768066be69e3b617c5504c",
  "created_time": "2026-09-20T09:20:00.000Z",
  "last_edited_time": "2026-09-24T06:58:00.000Z"
}
---

#  函数式接口

# 前置内容说明
本节需要熟悉“泛型”，“匿名内部类”，“Lambda表达式”等内容
链接在这里↓
[泛型与多态](https://app.notion.com/p/3df5a2dd827680ca9354f5718b41b5a3) [匿名内部类](https://app.notion.com/p/3db5a2dd8276806190c1d8e1efcba247) [Lambda表达式](https://app.notion.com/p/3db5a2dd827680bf9e55d713895473c1) 
# 是什么
我们知道，接口是对类的抽象，准确来说，接口只定义了行为，具体实现由对应的实现类实现
Java自带了一些类/方法去便于我们进行一些操作（详见[第六章：常用工具类](https://app.notion.com/p/3de5a2dd8276805f8339d7e4eff90df7) ），和他们类似，Java也自带了一些接口（函数式接口），它们不是便于开发者编程的，而是用于规定一些标准行为
因为Java希望你的程序是由“标准行为”拼接成的，这可以有效提高代码复用能力
（如：吃饭是由“张嘴”“闭嘴”“咀嚼”这些标准行为组成的，喝水是由“张嘴”闭嘴”组成，其中张嘴/闭嘴复用了吃饭的实现）
# 举个例子
需求：将一个经过一系列计算得出的字符串（假设为“小明”）赋值给Student类中的name变量
```java
//Student类
public class Student{
	String name;
	
	//给name变量赋值的方法
	public void takeName (Supplier<String> name){
			this.name=name.get()
	}
	
}
```
```java
public class Main{
	//主方法
	public static void main(String[] args){
	Student student = new Student();
	student.takeName(new Supplier(){
	  public String get(){
	  
		  一系列操作...
		  return "小明";
		  }
	  }); 
	}
}
```
或者也可以写成Lambda表达式
```java
public class Main{
	//主方法
	public static void main(String[] args){
	Student student = new Student();
	student.takeName(()->{
		  一系列操作...
		  return "小明";
	  }); 
	}
}
```
# 四大核心函数式接口
## **1. Supplier<T> —— 供给型（只出不进）**
**不接收任何参数，返回一个结果。** 像一个“工厂/生产者”。
## **2. Consumer<T> —— 消费型（只进不出）**
**接收一个参数，没有返回值。** 像“消费者”，处理完就结束。
## **3. Function<T, R> —— 函数型（进一个，出一个）**
**接收一个参数 T，返回结果 R。** 像数学中的函数 y = f(x)
## **4. Predicate<T> —— 断言型（进一个，出布尔）**
**接收一个参数，返回 boolean。** 用于条件判断
| **接口** | **抽象方法** | **输入** | **输出** | **语义** | **常见应用** |
| --- | --- | --- | --- | --- | --- |
| `Supplier<T>` | `get()` | 无 | T | 生产数据 | 工厂、惰性求值 |
| `Consumer<T>` | `accept(T)` | T | 无 | 消费数据 | forEach |
| `Function<T,R>` | `apply(T)` | T | R | 转换数据 | map |
| `Predicate<T>` | `test(T)` | T | boolean | 判断条件 | filter |
