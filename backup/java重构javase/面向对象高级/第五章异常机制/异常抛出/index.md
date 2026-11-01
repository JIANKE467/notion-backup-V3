---
{
  "id": "3dd5a2dd-8276-8089-ab45-d7a417bcd028",
  "url": "https://app.notion.com/p/3dd5a2dd82768089ab45d7a417bcd028",
  "created_time": "2026-09-16T02:54:00.000Z",
  "last_edited_time": "2026-09-16T14:09:00.000Z"
}
---

#  异常抛出

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
