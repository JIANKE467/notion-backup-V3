---
{
  "id": "3f95a2dd-8276-80b3-b95f-c29f692a2525",
  "url": "https://app.notion.com/p/3f95a2dd827680b3b95fc29f692a2525",
  "created_time": "2026-10-14T08:10:00.000Z",
  "last_edited_time": "2026-10-17T07:15:00.000Z"
}
---

#  文件字节流

本节的核心是FileInputStream类及**FileOutputStream类**，下面围绕该类进行展开
# FileInputStream类（文件字节输入流）
来历：FileInputStream是`InputStream` 的具体实现类，位于 `java.io` 包中
作用：用于获取文件的字节流（把硬盘上的一个文件，以**字节**为单位读取到程序内存中）（输入文件到流）
### 常用方法
构造方法（创建FileInputStream类的对象时支持的传入参数）：
```java
FileInputStream(File file)          
// 通过 File 对象创建
FileInputStream(String name)        
// 通过文件路径名创建
FileInputStream(FileDescriptor fdObj) 
// 通过文件描述符创建
```
读取方法：
| 方法 | 功能 | 传入 | 返回 |
| --- | --- | --- | --- |
| **read()** | 一次读取一个字节，下次调用读取下一个，读到末尾返回-1 | 空参调用 | 读到的那个字节值，读到末尾返回-1 |
| **read(byte[] b)** | 一次读多个字节，将读到的值放入传入的数组中，每次读都从数组的0下标覆盖写入 | 传入一个数组 | 读到的字节数，读到的值放到了数组中，读到末尾返回-1 |
| **int read(byte[] b, int off, int len)** | 依旧将数据存到数组中，不过可以控制存放位置、读取量 | 数组（存放读到的数据），起始下标，读取字节 | 读到的字节数，读到的值放到了数组中，读到末尾返回-1 |
| 方法 | 功能 | 传入 | 返回 |
| --- | --- | --- | --- |
| **skip(n)** | 跳过并丢弃 n 个字节的数据 | 跳过字节数 | 字节流 |
| **available()** | 返回剩余可读取（不受阻塞）的字节估计数 | 空 | 字节数 |
| **Descriptor getFD()** | 获取文件描述符对象。 | 空 | 对象 |
| 方法 | 功能 | 传入 | 返回 |
| --- | --- | --- | --- |
| **close()** | 关闭流并释放系统资源（**使用完必须调用）** | 空 | 无 |
### 使用方法
需要导入`java.io`包
1. 创建FileInputStream类的对象以创建流
```java
FileInputStream fis = new FileInputStream("路径");
//将文件路径作为参数传入以明确要读取哪个文件
```
1. 调用read() 方法读取流（以**int read(byte[] b, int off, int len)**签名的方法为例）
```java
byte[] buffer = new byte[1024];
int len = fis.read(buffer, 0, 512); // 最多读512字节存入buffer
```
1. 关闭流并释放系统资源
```java
fis.close();
```
### 注意
IO操作可能受很多因素影响导致抛异常（文件被占用，硬盘正忙），因此需要捕获异常（使用try catch捕获异常）
可以空处理/打印堆栈/稍后重试
```java
public static void main(String[] args) {
    try {   
		    //注意，IO相关操作会有很多影响因素，有可能出现异常，所以需要明确进行处理
        FileInputStream inputStream = new FileInputStream("路径");
        //路径支持相对路径和绝对路径
    } catch (FileNotFoundException e) {
		    //打印异常堆栈
        e.printStackTrace();
    }
}
```
# **FileOutputStream类（文件字节输出流）**
来历：FileOutputStream是`OutputStream`的具体实现类，位于`java.io`包中
作用：用于将程序中的字节写入文件（把内存中的数据，以**字节**为单位写入硬盘上的文件）（从流中输出）
### 常用方法
构造方法（创建FileOutputStream类的对象时支持的传入参数）：
```java
FileOutputStream(File file)
// 通过 File 对象创建，默认覆盖文件原有内容
FileOutputStream(String name)
// 通过文件路径名创建，默认覆盖文件原有内容
FileOutputStream(File file, boolean append)
// 通过 File 对象创建，可指定是否追加写入
FileOutputStream(String name, boolean append)
// 通过文件路径名创建，可指定是否追加写入
FileOutputStream(FileDescriptor fdObj)
// 通过文件描述符创建
```
写入方法：（跟字节输入流差不多）
| 方法 | 功能 | 传入 | 返回 |
| --- | --- | --- | --- |
| **write(int b)** | 写入一个字节（一次只写入参数的前 8 位，超出部分会被忽略） | 字符/数字/十六进制 | 无 |
| **write(byte[] b)** | 将数组中的所有字节写入文件 | 一个字节数组 | 无 |
| **write(byte[] b, int off, int len)** | 将数组中从 `off` 开始的 `len` 个字节写入文件 | 字节数组、起始下标、写入字节数 | 无 |
| **flush()** | 刷新输出流，使待写数据提交到底层输出目标 | 空 | 无 |
| **close()** | 关闭流并释放系统资源（使用完必须调用） | 空 | 无 |
### 使用方法
需要导入`java.io`包
1. 创建FileOutputStream类的对象以创建流
```java
FileOutputStream fos = new FileOutputStream("路径");
// 将文件路径作为参数传入，以明确要写入哪个文件
```
1. 调用write()方法写入字节（以`write(byte[] b)`为例）
```java
byte[] data = {65, 66, 67};
fos.write(data); // 将数组中的字节写入文件
```
1. 关闭流并释放系统资源
```java
fos.close();
```
### 注意
IO操作可能受很多因素影响导致抛异常（路径不存在、文件无法创建、磁盘正忙等），因此需要捕获异常（使用try catch捕获异常）
异常可以空处理/打印堆栈/稍后重试；
默认创建FileOutputStream时，如果目标文件已经存在，会先清空原有内容再写入；如果需要保留原内容并在末尾追加，应使用带`append`参数的构造方法，并将其设为`true`
FileOutputStream写入的是字节，不是字符；写入文本时需要先按指定字符集将字符串转换为字节
```java
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

public static void main(String[] args) {
    try (FileOutputStream outputStream = new FileOutputStream("路径")) {
        // 路径支持相对路径和绝对路径
        byte[] data = "示例文本".getBytes(StandardCharsets.UTF_8);
        outputStream.write(data);
    } catch (IOException e) {
        // 打印异常堆栈
        e.printStackTrace();
    }
}
```
