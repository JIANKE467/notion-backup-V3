---
{
  "id": "3b35a2dd-8276-8013-98c0-e762f12b95ff",
  "url": "https://app.notion.com/p/java16-3b35a2dd8276801398c0e762f12b95ff",
  "created_time": "2026-08-05T13:01:00.000Z",
  "last_edited_time": "2026-08-05T15:32:00.000Z"
}
---

#  （java16）类型判断模式匹配

# 本节介绍`instanceof`关键字
`instanceof`用于判断某对象是否属于某类，及其子类
语法：
```plain text
对象 instanceof 类名
```
返回结果是：
- `true`：是这个类型
- `false`：不是这个类型
# 应用
我们可以基于instanceof关键字，做一个简单的类型路由（对于同一个父类下的不同子类的对象采取不同的处理逻辑）
```java
/*父类*/
public class Animal{
}

/*子类1*/
public class Dog extends Animal{
} 

/*子类2*/
public class Cat extends Animal{
} 
```
```java
/*类型路由*/
void test(Animal x){
	if(x instanceof Dog){
	System.out.println("大狗狗，是狼");//如果对象来自dog类型，则显示这句话
	}else if(x instanceof Cat){
	System.out.println("圆头耄耋");//如果对象来自cat类型，则显示这句话
	}
	
}
```
- 关于为什么要求传入Animal类，但却可以传入子类dog和cat类，请参考上一节的内容
- 由于test方法使用animal类来接收参数，传入的dog和cat类的对象会自动变成Animal类（把对象引用给了Animal类），因此是无法使用Dog和cat类中的属性的（父类看不到子类内容），如果需要使用子类中的属性则要强制类型转换成原来的类⬇️
```java
void test(Animal x){
	if(x instanceof Dog){
	Dog y = (Dog)x;
	
	调用dog属性...
	
	}else if(x instanceof Cat){
	Cat z = (Cat)x;
	
	用cat属性...
	
	}
	
}
```
# Java16新特性
对于上面需要强制类型转换的问题，Java 16做了简化（可以直接在类名后跟变量名，系统会自动帮你强制转换）（变量名用于接收强转后的引用）
```java
void test(Animal x){
	if(x instanceof Dog y){
	
	调用dog属性...
	
	}
```
