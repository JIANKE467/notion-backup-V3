---
{
  "id": "3bb5a2dd-8276-8083-8883-d3b8ce64e6d6",
  "url": "https://app.notion.com/p/3bb5a2dd827680838883d3b8ce64e6d6",
  "created_time": "2026-08-13T12:28:00.000Z",
  "last_edited_time": "2026-09-10T07:40:00.000Z"
}
---

#  第一章：基本类型包装类

[包装类介绍](包装类介绍/index.md)
  Java存在两种数据类型，基本数据类型和引用数据类型
  基本数据类型是按照面向过程的逻辑去设计的，因此无法使用面向对象的特性（如对象/类/接口等）
  包装类就是用来将基本数据类型转换成引用数据类型的
  # 赋值语法
  语法一：创建一个包装类的对象（已弃用）
  语法二：和基本数据类型 赋值语法一致
  语法三：调用`valueOf()`方法赋值
  PS：其中第一 ，三种方法完全等价，第二种方法会给每个变量创建对象，不会使用缓存（见本节最后）[关于缓存](https://app.notion.com/p/3bb5a2dd827680018081d0f360743366#3bb5a2dd8276808ab1f2fefc468984b6) 
  ```java
包装类名 对象名 = new 包装类名(值); //语法一
包装类名 变量名 = 值; //语法二
包装类名 对象名 = 包装类名.valueOf(值); //语法三
  ```
  ```java
//这里以integer（int的包装类）为例
Integer a = 10; //写法一（自动装箱）
Integer a = new Integer(10);  //写法二（已弃用 不推荐使用）
Integer a = Integer.valueOf(10);  //写法三
  ```
  | 基本数据类型 | 对应包装类 | 名称 |
  | --- | --- | --- |
  | int | Integer（注意第一个字母是大写i不是l） | 整形 |
  | byte | Byte | 字节型 |
  | boolean | Boolean | 布尔类型 |
  | short  | Short | 短整形 |
  | char | Character | 字符型 |
  | long  | Long | 长整型 |
  | float  | Float | 浮点型 |
  | double | Double | 双精度浮点型 |
  # 自动装箱/自动拆箱
  自动装箱：基本数据类型的值可以自动类型转换成对应的包装类
  ```java
int a = 10;
Integer b = a;
  ```
  自动拆箱：包装类的值可以自动类型转换成对应的基本数据类型
  ```java
Integer a = 10;
int b = a;
  ```
  > 通过自动拆箱和自动装箱包装类的变量也可以轻松参与运算，而不用手动类型转换
  # 注意
  包装类和包装类之间比较是否相等时，比较的是引用
  ```java
Integer a = new Integer(100);
Integer b = new Integer(100);

System.out.println(a == b);
//运行结果是false
  ```
  包装类和基本数据类型的变量之间比较是否相等时，比较的是值
  ```java
Integer a = new Integer(10);
int b = 10;

System.out.println(a == b); 
//运行结果是true
  ```
  # 原理
  ### 包装类
  包装类利用了封装的思想，将基本数据类型封装成了引用数据类型。
  我们可以通过查看相应类的代码得知，包装类就是把基本数据类型的变量封装到了类里，并提供了可供调用的的方法（以integer为例）
  ```java
public final class Integer extends Number{

.....

	private final int value;  //类中实际上就靠这个变量在存储包装的值
	
	public Integer(int value) {
	    this.value = value;
	}
}
  ```
  # 关于缓存
  Java 对部分包装类对象进行了缓存。自动装箱时，如果值在缓存范围内，可能直接复用已有对象，而不是创建新对象。
  ```java
//使用自动装箱
Integer a = 10;
Integer b = 10;
System.out.println(a == b);
//运行结果是true
  ```
  ```java
//不使用自动装箱
Integer a = new Integer(100);
Integer b = new Integer(100);
System.out.println(a == b);
//运行结果是false
  ```
  - 上面所说的语法1和语法3都是自动装箱 都会使用缓存
  - 语法2 会给每个变量创建对象，不会使用缓存
  - 使用缓存后，多个值相同的变量会被指向同一个对象
  - 缓存只在一定范围内生效，出了缓存范围，将会给每一个变量创建对象。如对于 `Integer`：**默认缓存范围是 ****`-128 ~ 127`**
  # 包装类中的其他方法
  decode()方法：十六进制和八进制的字符串转成十进制
  valueOf()方法：除了传入变量的值外，还可以将字符串转化为字符型（内部）
  toHexString()方法：将十进制转化为其他进制
  略
[特殊包装类](特殊包装类/index.md)
  有两个特殊的包装类上节并没有提及，现在此说明
  这两个数据类型在使用及语法上与其他数据类型没有差异
  # BigInteger包装类（针对超大数）
  BigInteger包装类没有对应的基本数据类型
  在基本数据类型中，long是最大的数据类型，其包装类Long上节课已经提及
  而BigInteger包装类是用于超大数字的数据类型（没有位数限制，取决于机器内存大小）
  # BigDecimal包装类（精确计算小数）
  BigDecimal包装类没有对应的基本数据类型
  我们前面提到浮点类型无法精确计算
  BigDecimal包装类则解决了这个问题，无论多大的数，无论小数点多少位，它都可以精确计算
