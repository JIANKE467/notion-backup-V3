---
{
  "id": "3fb5a2dd-8276-8008-9632-c58b1892d5c5",
  "url": "https://app.notion.com/p/3fb5a2dd827680089632c58b1892d5c5",
  "created_time": "2026-10-16T08:20:00.000Z",
  "last_edited_time": "2026-10-16T09:26:00.000Z"
}
---

#  缓冲流

经过前面章节的学习，我们知道文件字节/字符流可以对文件进行读取或写入操作，但不论是文件字符流还是文件字节流，它们都是从直接从硬盘中读取（忽略系统优化）
缓冲流则是一个~~预读取~~（实际上不是预读取，）操作，它可以提前将文件读取到内存中，这样等获取数据时就无需再从硬盘中读取了
依旧分为字节缓冲流和字符缓冲流
# 字节缓冲流
  来源：都在`java.io`包中，且字节缓冲流类都继承自相应的文件字节流类
  ### **BufferedInputStream（缓冲字节输入流）**
  作用：以字节为单位读取文件到内存中
  **构造方法：**
  | 构造方法签名 | 作用 | 传入 |
  | --- | --- | --- |
  | BufferedInputStream(InputStream in) | 创建字节缓冲流对象（默认大小） | 文件字节流对象 |
  | BufferedInputStream(InputStream in, int size)  | 创建字节缓冲流对象（自定义大小） | 文件字节流对象，缓存区大小（单位：字节） |
  ```java
BufferedInputStream(InputStream in)              
// 单参数，默认缓冲区大小 8192 字节，传入文件字节流对象
BufferedInputStream(InputStream in, int size)    
// 2参数，自定义缓冲区大小，传入文件字节流和缓存区大小
  ```
  **常用方法：**
  - 由于字节缓冲流类都继承自相应的文件字节流类，所以继承了文件字节流有的所有方法
  **使用方法：**
  1. 调用构造方法创建缓冲流
  1. 执行文件字节流操作或调用文件工具类
  1. 关闭缓冲流
  ### **BufferedOutputStream（缓冲字节输出流）**
  来历：位于 `java.io` 包中，接收一个 `OutputStream` 作为底层输出流，常用于包装文件字节输出流。
  作用：先将程序中的字节写入内存缓冲区，缓冲区满或调用刷新、关闭操作时，再批量写入底层输出流，以减少直接写入次数。
  **构造方法：**
  | 构造方法签名 | 作用 | 传入 |
  | --- | --- | --- |
  | `BufferedOutputStream(OutputStream out)` | 创建字节缓冲输出流（默认缓冲区大小） | 底层输出流 |
  | `BufferedOutputStream(OutputStream out, int size)` | 创建指定缓冲区大小的字节缓冲输出流 | 底层输出流、缓冲区大小（单位：字节） |
  ```java
BufferedOutputStream(OutputStream out)
// 使用默认大小的缓冲区
BufferedOutputStream(OutputStream out, int size)
// 自定义缓冲区大小，size 单位为字节
  ```
  **常用方法：**
  | 方法 | 功能 | 传入 | 返回 |
  | --- | --- | --- | --- |
  | `write(int b)` | 将一个字节写入缓冲区；缓冲区满时会写入底层输出流 | 一个字节值 | 无 |
  | `write(byte[] b, int off, int len)` | 将字节数组中指定范围的数据写入缓冲区 | 字节数组、起始下标、写入长度 | 无 |
  | `flush()` | 将缓冲区中尚未写出的数据刷新到底层输出流 | 空 | 无 |
  | `close()` | 刷新并关闭流，同时释放系统资源 | 空 | 无 |
  由于它继承了输出流的写入方法，也可以直接调用 `write(byte[] b)` 写入整个字节数组。
  **使用方法：**
  1. 创建底层文件字节输出流，并用缓冲流包装
  1. 调用 `write()` 写入字节
  1. 使用完关闭缓冲流（会自动刷新，并关闭底层流）
  ```java
byte[] data = {65, 66, 67};
try (BufferedOutputStream output = new BufferedOutputStream(
        new FileOutputStream("路径"))) {
    output.write(data);
    // 需要在关闭前确保数据写出时，可调用 output.flush()
} catch (IOException e) {
    e.printStackTrace();
}
  ```
# 字符缓冲流
  ### **BufferedReader（缓冲字符输入流）**
  来历：位于 `java.io` 包中，接收一个 `Reader` 作为底层字符流，常用于包装 `FileReader`。
  作用：以字符为单位缓冲读取文本内容，并提供按行读取的功能。
  **构造方法：**
  | 构造方法签名 | 作用 | 传入 |
  | --- | --- | --- |
  | `BufferedReader(Reader in)` | 创建字符缓冲输入流（默认缓冲区大小） | 底层字符输入流 |
  | `BufferedReader(Reader in, int size)` | 创建指定缓冲区大小的字符缓冲输入流 | 底层字符输入流、缓冲区大小（单位：字符） |
  ```java
BufferedReader(Reader in)
// 使用默认大小的缓冲区
BufferedReader(Reader in, int size)
// 自定义缓冲区大小，size 表示字符数
  ```
  **常用方法：**
  | 方法 | 功能 | 传入 | 返回 |
  | --- | --- | --- | --- |
  | `read()` | 读取一个字符，读到末尾返回 `-1` | 空参调用 | 字符值（`int`），末尾返回 `-1` |
  | `read(char[] cbuf, int off, int len)` | 将字符读入数组，可指定存放位置和最多读取的字符数 | 字符数组、起始下标、最多读取长度 | 实际读取的字符数，末尾返回 `-1` |
  | `readLine()` | 读取一行文本，不包含行结束符 | 空参调用 | 行内容；读到末尾且没有更多内容时返回 `null` |
  | `ready()` | 判断下一次读取是否可以保证不阻塞 | 空 | `true` 或 `false` |
  | `close()` | 关闭流并释放系统资源 | 空 | 无 |
  **使用方法：**
  需要导入 `java.io` 包。读取文本时应注意字符集；下面示例使用 Java 11+ 的 `FileReader` 字符集构造方法。
  1. 创建 `FileReader`，并用 `BufferedReader` 包装
  1. 调用 `readLine()` 逐行读取，返回 `null` 时表示读完
  1. 使用完关闭缓冲流（底层流也会随之关闭）
  ```java
try (BufferedReader reader = new BufferedReader(
        new FileReader("路径", StandardCharsets.UTF_8))) {
    String line;
    while ((line = reader.readLine()) != null) {
        System.out.println(line);
    }
} catch (IOException e) {
    e.printStackTrace();
}
  ```
  **注意：**
  `readLine()` 会去掉行结束符；如果需要保留换行，应在处理每一行时自行添加。文件字符集应与读取时指定的字符集一致，避免乱码。
  ### **BufferedWriter（缓冲字符输出流）**
  来历：位于 `java.io` 包中，接收一个 `Writer` 作为底层字符流，常用于包装 `FileWriter`。
  作用：先将程序中的字符写入内存缓冲区，再批量写入底层字符输出流；还提供了写入平台适用换行符的方法。
  **构造方法：**
  | 构造方法签名 | 作用 | 传入 |
  | --- | --- | --- |
  | `BufferedWriter(Writer out)` | 创建字符缓冲输出流（默认缓冲区大小） | 底层字符输出流 |
  | `BufferedWriter(Writer out, int size)` | 创建指定缓冲区大小的字符缓冲输出流 | 底层字符输出流、缓冲区大小（单位：字符） |
  ```java
BufferedWriter(Writer out)
// 使用默认大小的缓冲区
BufferedWriter(Writer out, int size)
// 自定义缓冲区大小，size 表示字符数
  ```
  **常用方法：**
  | 方法 | 功能 | 传入 | 返回 |
  | --- | --- | --- | --- |
  | `write(int c)` | 写入一个字符到缓冲区 | 字符值（`int`） | 无 |
  | `write(char[] cbuf, int off, int len)` | 写入字符数组中的指定范围 | 字符数组、起始下标、字符数 | 无 |
  | `write(String str)` | 写入字符串 | 字符串 | 无 |
  | `newLine()` | 写入当前系统适用的换行符 | 空 | 无 |
  | `flush()` | 将缓冲区中的字符刷新到底层输出流 | 空 | 无 |
  | `close()` | 刷新并关闭流，同时释放系统资源 | 空 | 无 |
  **使用方法：**
  1. 创建底层字符输出流，并用缓冲流包装
  1. 调用 `write()` 写入字符或字符串；需要换行时调用 `newLine()`
  1. 使用完关闭缓冲流（会自动刷新，并关闭底层流）
  ```java
try (BufferedWriter writer = new BufferedWriter(
        new FileWriter("路径", StandardCharsets.UTF_8))) {
    writer.write("第一行");
    writer.newLine();
    writer.write("第二行");
} catch (IOException e) {
    e.printStackTrace();
}
  ```
  **注意：**
  `BufferedWriter` 的 `flush()` 可以在流关闭前提交缓冲区中的字符；关闭流时也会先刷新。若要在原文件末尾追加内容，应让底层 `FileWriter` 使用追加模式；默认构造方式会覆盖原有内容。写入文本时应明确并保持字符集一致。
# 注意
- 需要澄清一点事实：缓冲流仅优化了多次访问，它仍是读取到缓冲流这行才会运行的，并没有优先运行的能力
- 字符缓冲流和普通流一样，关闭流内存就释放了（释放缓冲区），它只是提供了一个缓冲能力
