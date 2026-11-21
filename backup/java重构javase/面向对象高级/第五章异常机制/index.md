---
{
  "id": "3db5a2dd-8276-8007-80c7-f4963fc2bc8f",
  "url": "https://app.notion.com/p/3db5a2dd8276800780c7f4963fc2bc8f",
  "created_time": "2026-09-14T10:02:00.000Z",
  "last_edited_time": "2026-09-16T14:43:00.000Z"
}
---

#  第五章：异常机制

首先声明：各种的异常，就是不同的异常类 (详见下面各类继承树)
```java
Throwable                    ← 异常体系的根
├── Error                    ← 严重错误，不该捕获
│   ├── OutOfMemoryError
│   ├── StackOverflowError
│   └── NoClassDefFoundError
│
└── Exception                ← "异常"主体
    ├── RuntimeException     ← 运行时异常（非受检）
    │   ├── NullPointerException
    │   ├── IndexOutOfBoundsException
    │   ├── ClassCastException
    │   └── ArithmeticException
    │
    └── 其他 Exception 子类   ← 受检异常
        ├── IOException
        ├── SQLException
        └── InterruptedException

```

[异常类型](异常类型/index.md)

  ### 运行时异常`RuntimeException`
  这种异常可以通过编译器，但运行时会报错，所有的运行时异常都继承自`RuntimeException`
  ### 编译时异常（受检异常）`Exception`
  一般是逻辑错误，无法通过编译器，默认继承自`Exception`类的异常都是编译时异常
  ### 错误
  错误比异常更严重，可能导致严重后果，如：`OutOfMemoryError`内存溢出错误可能导致JVM崩溃
  所有错误都继承自Error类
[自定义异常](自定义异常/index.md)
  自定义异常就是对异常类的定义，JavaSE自带了700多种异常，但他们是通用的技术性错误，在实际业务中，我们需要更确切的信息表达具体异常信息，如：余额不足，文件过大…
  这就需要我们自定义异常类
  # 语法
  自定义异常实际上就是定义`RuntimeException`或`Exception`或`Error`类的子类
  ```java
public class 自定义异常名 extends 父类异常{
  异常内容...
}
  ```
  # 注意⚠️
  - 不要再异常类体中写异常处理逻辑，虽然这在语法上完全允许，但在设计上一定要避免（设计原则上：异常应该是轻量，只读，无副作用的）
  - 异常类只做异常的传递，具体的处理由另外的模块负责（设计规范，非语法强制）
  ```plain text
异常发生点          异常类（信使）           处理点
┌──────────┐      ┌──────────────┐      ┌──────────────┐
│ throw new├─────→│  携带信息      ├─────→│  try-catch / │
│ MyEx(...)│      │  code、msg 等  │      │  全局处理器    │
└──────────┘      └──────────────┘      └──────────────┘
  抛出异常           只装数据            写处理逻辑

  ```
[异常抛出](异常抛出/index.md)
  - 异常抛出就是创建异常类的对象
  - 抛出异常（创建对象）时，传入的参数一般是异常信息和异常路径
  - 和return类似，异常抛出后（执行到throw）方法将被终止，后续代码不会执行

  # 手动抛异常
  为了防止传入非法参数，我们可以在业务方法中对参数进行判断，不符合范围则手动抛出异常
  ```java
//业务逻辑
public int test(int a,int b){
	if(b == 0){
		throw new RuntimeException("被除数不能为0");
	}
	return a/b;
} 
  ```
  ### 语法：
  ```java
throw new 异常类名(参数);
  ```
  # 自动抛异常
  除了手动抛异常外，Java还能自动检测一些异常（该能力是由JDK 类库里写的 throw，但对使用者来说“感觉是自动的”）
  自动抛异常不需要开发者手动写throw和判断逻辑
  ### Java能自动检测如下异常：
  1. 空指针
  1. 除0
  1. 数组越界
  1. 类型转换错误
  1. 内存溢出/栈溢出
  1. 数字格式错误
  # throws声明
  `throws` 用于方法声明中，表示该方法**可能抛出的异常**
  ### 语法
  ```java
修饰符 返回类型 方法名(参数) throws 异常类型1, 异常类型2 {
    // 方法体
}
  ```
  ### throws声明的作用
  Java编译器规定了一些受检异常（编译时异常）：
  ```java
Throwable                    ← 异常体系的根
├── Error                    ← 严重错误，不该捕获
│   ├── OutOfMemoryError
│   ├── StackOverflowError
│   └── NoClassDefFoundError
│
└── Exception                ← "异常"主体
    ├── RuntimeException     ← 运行时异常（非受检）
    │   ├── NullPointerException
    │   ├── IndexOutOfBoundsException
    │   ├── ClassCastException
    │   └── ArithmeticException
    │
    └── 其他 Exception 子类   ← 受检异常
        ├── IOException
        ├── SQLException
        └── InterruptedException

  ```
  - ~~**编译器不允许未处理的受检异常（编译时异常）通过编译**~~
  - **编译器强制要求开发者处理受检异常（要么catch捕获，要么throws上抛），否则不能通过编译，但有些受检异常是无法规避的（如：网络未连接，文件找不到），使用throws声明代表我知道可能报错但我选择向上抛**
  - 非受检异常（运行时异常）则不强制要求处理
  # 又可以喷Java了😅
  什么叫编译器强制要求处理受检异常，但有些受检异常无法避免？啊，网络未连接，文件找不到…这种东西怎么看都是运行时异常吧，非得把语法逻辑搞的这么反直觉
  c#，Kotlin，Go人家全部都没有受检异常这一说
  本意是强制处理易恢复项，实际上纯增加工作量，因为受检异常太多了，没写几个逻辑就要处理一个受检异常，而且你不处理就得一直往上抛，上面的每一层都得写throws（方法签名污染）
  如果开发者假处理（只chtch不写逻辑），又会吞异常，非常sb
[异常捕获](异常捕获/index.md)
  程序出现异常就会逐层上抛，直到JVM，JVM收到任何异常都会终止程序并在控制台打印栈追踪信息，如果要避免程序终止就需要捕获异常
  # 语法
  我们可以将代码编写到`try`语句块中，只要是在这个范围内发生的异常，都可以被捕获，使用`catch`关键字指定需要捕获的异常类型
  ```java
public static void main(String[] args) {

...

    try {    
      可能发生异常的语句...
       
    } catch (异常类型 对象名){   //因为异常本身也是一个对象，catch中实际上就是用一个局部变量去接收异常
				异常处理逻辑...
				
    } 
   
   
    
}
  ```
  - 因为异常本身也是一个对象，catch中实际上就是用一个局部变量去接收异常，方便我们操作
  - catch中捕获的类型只能是Throwable的子类，也就是说要么是抛出的异常，要么是错误，不能是其他的任何类型
  - printStackTrace()方法可以打印异常的栈追踪信息
  - 也可以将catch中的异常类型写成Throwable类，这样就能捕获所有异常了 
  - 异常捕获后可以继续运行后面的代码
  也可以这样（多种异常用共用一种处理）
  ```java
try {    
      可能发生异常的语句...
       
    } catch (异常类型1|异常类型2 对象名){  
				异常处理逻辑...
				
    } 
  ```
  或者是这样（**多重异常捕获**）（多个异常多种处理逻辑）
  ```java
try {    
      可能发生异常的语句...
       
    } catch (异常类型1 对象名1){  
				异常处理逻辑...
				
    } catch (异常类型2 对象名2){
		    异常处理逻辑...
		    
    } ...
  ```
  - 这种需要注意catch的顺序，会先捕获写在前面的异常（如果把父类写在前面，子类写在后面，那子类的异常就会被父类先捕获）
  还可以使用finally，无论是否捕获异常，finally都会执行
  ```java
try {
    //....
}catch (Exception e){
            
}finally {
  	System.out.println("lbwnb");   //无论是否出现异常，都会在最后执行
}
  ```
  - 可以不写catch部分，只写finally部分（发生异常程序终止，但在那之前会执行finally）
[断言表达式](断言表达式/index.md)
  这节功能太小众了，仅做了解

  **断言**是一种调试机制，用于在开发/测试阶段**验证你对程序状态的假设**——断定某个条件“一定为真”，如果不真，说明代码有 bug，立即报错。
  # 语法
  ```java
assert 布尔表达式;
assert 布尔表达式 : 错误详情信息;  // 带提示信息的写法
  ```
  # 注意
  - **Java 断言默认不启用**，`assert` 语句会被 JVM 直接跳过，写了也不生效
  - 使用断言表达式需要修改JVM参数
  ```java
# 只开启某个类
java -ea:com.example.MyClass MyApp

# 开启所有类（最常用）
java -ea MyApp

# 关闭（默认）
java -da MyApp

  ```
