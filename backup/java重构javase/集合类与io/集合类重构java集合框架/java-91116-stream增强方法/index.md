---
{
  "id": "3f95a2dd-8276-8099-a783-fa8024c3be79",
  "url": "https://app.notion.com/p/Java-9-11-16-Stream-3f95a2dd82768099a783fa8024c3be79",
  "created_time": "2026-10-14T02:15:00.000Z",
  "last_edited_time": "2026-10-14T03:51:00.000Z"
}
---

#  **(Java 9/11/16) Stream增强方法**

由于jdk8推出的Stream流很实用，因此jdk9/11/16再次扩展了Stream流的功能
# jdk9
新增方法：
### **takeWhile() 取前缀**
- 功能：对流进行截取
- 传入参数：“谓词”，也就是判断条件
- 返回：截取后的流
- 工作原理：从流的第一个元素开始，根据传入的判断条件判断是否符合，一旦读到不符合的元素，立即截断流，并返回前面的所有元素（不包含截断处的元素）
名词解释：
前缀➡️就是截断位置前的所有元素
谓词➡️就是判断条件，使用Lambda表达式
例：
```java
//创建集合
List<Integer> nums = List.of(1, 2, 3, 7, 8, 4, 5, 9);

		//获取流 
nums.stream()
		//取前缀
		.takeWhile(n -> n < 3)
		//结束流
    .forEach(System.out::print);  // 输出: 12
```
### **dropWhile()** 去前缀
- 功能：对流进行截取
- 传入参数：“谓词”，也就是判断条件
- 返回：截取后的流
- 工作原理：从流的第一个元素开始，根据传入的判断条件判断是否符合，一旦读到不符合的元素，立即截断流，并返回后面的所有元素（不包含截断处的元素）
名词解释：
前缀➡️就是截断位置前的所有元素
谓词➡️就是判断条件，使用Lambda表达式
例：
```java
//创建集合
List<Integer> nums = List.of(1, 2, 3, 7, 8, 4, 5, 9);

		//获取流
nums.stream()
		//去前缀
		.dropWhile(n -> n < 3)
		//结束流
    .forEach(System.out::print);  // 输出: 78459

```
### **iterate() 方法扩展**
- 功能：用来生成流的方法（不是获取流）
- 工作原理：根据传入的种子和迭代算法，通过与上一个元素计算生成下一个元素
- 传入（Java8）：传入两个参数（初始值，迭代函数）
- 传入（Java9）：传入三个参数（初始值，终止条件，迭代函数）
- 返回：生成的流
- 注意⚠️：由于生成流时还没有流，因此链式调用中不是先调用获取流的方法，而是直接调用生成流的方法
例：
```java
//Java8
			 //生成流
Stream.iterate(1, n -> n * 2)
			 //截断流（否则会无限生成）   
      .limit(5)  
       //结束流              
      .forEach(System.out::print);  // 1 2 4 8 16

```
```java
//Java9
			//生成流
Stream.iterate(1, n -> n < 100, n -> n * 2)
			//结束流
      .forEach(System.out::println);
// 1 2 4 8 16 32 64
```
### **ofNullable()**
- 功能：**把“可能为 null 的引用”安全地转换成流（防止空指针异常）**
- 工作原理：值为 null 时返回空流，值非 null 时返回单元素流
- 传入：待转换成流的引用
- 返回：流
例：
```java
Stream.ofNullable("hello")  // 返回流hello
Stream.ofNullable(null)     // 返回空流
```
# jdk11
新增方法:
### Predicate.not()
非 Stream 接口的方法，而是 `java.util.function.Predicate` 的静态方法
- 功能：给传入的谓词取反
- 工作原理：将一个谓词作为参数传入，返回它的取反谓词
- 传入：待取反谓词
- 返回：取反谓词
- 存在意义：Lambda表达式可以不用这种而是直接在执行的操作前挂一个！来取反，但如果是一个写好的取反类的对象则不支持！取反，这时`Predicate.not()`就派上用场了
例：
```java
// Java 11：方法引用保留，语义清晰
//可以给引用使用
list.stream().filter(Predicate.not(String::isBlank));
//也可以给Lambda表达式使用
list.removeIf(Predicate.not(s -> s.startsWith("WARN")));
```
# jdk16
新增方法:
### **toList()**
- 功能：**把流中的元素直接收集为一个不可变 List**
- 工作原理：不用传参，在链式调用中调用该方法即将流转换成List
- 传入：不用传参，该方法是空参调用的
- 返回：一个List
例：
```java
// 直接调用即可，括号里什么都不填
List<String> result = stream.map(String::toUpperCase)
														.toList();
```
### **mapMulti()**
- 功能：**把每个元素替换为零个或多个元素**
- 工作原理：传入一个Lambda声明替换规则，按该规则替换后返回
- 传入：一个Lambda表达式，该Lambda表达式有两个形参（当前流元素类型，输出类型），通过在Lambda中控制调用`输出类型.accept（替换内容）`的次数来控制入元素的数量
例
```java
			//调用替换方法
stream.mapMulti((element, downstream) -> {
    downstream.accept(结果1);   // 将结果1替换全部元素
    downstream.accept(结果2);   // 将结果2替换全部元素（不覆盖结果1）
});

```
可以发现这种方法可以实现所有元素多对一替换
