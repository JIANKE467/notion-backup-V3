---
{
  "id": "3db5a2dd-8276-80bf-9e55-d713895473c1",
  "url": "https://app.notion.com/p/Lambda-3db5a2dd827680bf9e55d713895473c1",
  "created_time": "2026-09-14T09:25:00.000Z",
  "last_edited_time": "2026-09-20T09:46:00.000Z"
}
---

#  **Lambda表达式**

这个是匿名内部类的语法糖（不全是）
先回顾一下匿名内部类：[核心要点：在创建对象的语句后加上花括号（花括号内就是匿名内部类，在此处实现接口/ 抽象类未实现的方法）](https://app.notion.com/p/3db5a2dd8276806190c1d8e1efcba247#3e15a2dd827680188e7cef58a8665457) 
**如果一个接口中有且只有一个待实现的抽象方法**，那么我们可以将匿名内部类简写为Lambda表达式
### 语法
```java
Study test = () -> System.out.println("我是学习方法！"); 

//上面的等价于下面的写法

Study test = new Studay(){
	@Override
	public void main(){
	System.out.println("我是学习方法！");
	} 
}
```

• 标准格式为：`接口名 对象名 = ([参数类型 参数名称,]...) ‐> { 代码语句，包括返回值 }`
### 注意⚠️
- **Lambda表达式只能应用于接口，抽象类不行**
-  接口内部必须有且仅有一个抽象方法（可以有多个方法，但是必须保证其他方法有默认实现，必须留一个抽象方法出来）
- Lambda表达式有多种省略写法↓
```java


// ① 完整形态：有括号、有类型、有大括号、有 return
c = (String a, String b) -> { return a.length() - b.length(); };

// ② 省略参数类型（编译器根据接口自动推断）
c = (a, b) -> { return a.length() - b.length(); };

// ③ 方法体只有一句时，去掉大括号和 return（必须一起去掉）
c = (a, b) -> a.length() - b.length();

// ④ 只有一个参数时，括号也可以省
Consumer<String> printer = s -> System.out.println(s);

// ⑤ 零个参数：括号不能省
Runnable r = () -> System.out.println("hello");

```
# 要点：
接口只有一个待实现方法，其匿名内部类可以写成lambda表达式
依旧是创建对象语句，只不过等号右边换成`(参数列表)->{代码}`
