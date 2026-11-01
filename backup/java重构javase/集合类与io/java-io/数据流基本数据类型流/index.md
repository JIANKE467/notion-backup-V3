---
{
  "id": "3fd5a2dd-8276-803a-a0d7-f521bd959b65",
  "url": "https://app.notion.com/p/3fd5a2dd8276803aa0d7f521bd959b65",
  "created_time": "2026-10-18T08:46:00.000Z",
  "last_edited_time": "2026-10-18T09:39:00.000Z"
}
---

#  数据流（基本数据类型流）

与字节/字符流不同，数据流（基本数据类型流）支持以基本数据类型为单位进行读写
分两个类
**注意⚠️：基本数据类型流只能作为普通流的包装来使用，不能单独使用**
# **DataInputStream（输入数据流）**
继承：**DataInputStream继承自FilterInputStream（文件字节输入流）**
作用：用于读取数据（按基本数据类型）
构造方法：
| **构造方法** | **说明** |
| --- | --- |
| `DataInputStream(InputStream in)` | 传入一个DataInputStream类型对象 |
常用方法：
除了继承的方法，还有以下方法
| **方法** | **返回类型** | **说明** | 传入参数 |
| --- | --- | --- | --- |
| `readBoolean()` | boolean | 读取 1 个字节，非 0 为 true | 无 |
| `readByte()` | byte | 读取 1 个有符号字节 | 无 |
| `readUnsignedByte()` | int | 读取 1 个无符号字节（0~255） | 无 |
| `readShort()` | short | 读取 2 字节有符号短整数 | 无 |
| `readUnsignedShort()` | int | 读取 2 字节无符号短整数 | 无 |
| `readChar()` | char | 读取 2 字节字符 | 无 |
| `readInt()` | int | 读取 4 字节有符号整数 | 无 |
| `readLong()` | long | 读取 8 字节长整数 | 无 |
| `readFloat()` | float | 读取 4 字节浮点数 | 无 |
| `readDouble()` | double | 读取 8 字节双精度浮点数 | 无 |
| `readUTF()` | String | 读取改良 UTF-8 编码的字符串 | 无 |
批量读取
| **方法** | **说明** | 传入参数 |
| --- | --- | --- |
| `read()` | 读取下一个字节 | 无 |
| `read(byte[] b)` | 读若干字节存入缓冲数组 b | 数组引用 |
| `read(byte[] b, int off, int len)` | 读最多 len 个字节到 b 的 off 位置起 | 数组引用，起始下标，读字节数 |
| `readFully(byte[] b)` | **阻塞式**地读满整个 b 数组，否则抛 EOFException | 数组引用 |
| `readFully(byte[] b, int off, int len)` | 阻塞式读满 len 个字节 | 数组引用，起始下标，读字节数 |
| `skipBytes(int n)` | 跳过 n 个字节 | 字节数 |
例子：
```java
try {
		DataInputStream dis = new DataInputStream(new FileInputStream("data.bin"));
    dis.readInt();
    dis.readDouble();
    dis.readUTF();
    dis.close();
    }
catch(IOException e){

} 
```
# **DataOutputStream （输出数据流）**
继承：**DataOutputStream 继承自 FilterOutputStream，并实现 DataOutput 接口**
作用：用于按基本数据类型将数据写入底层输出流
构造方法：
| **构造方法** | **说明** |
| --- | --- |
| `DataOutputStream(OutputStream out)` | 传入一个 OutputStream 类型的对象，通常包装文件字节流等普通输出流 |
常用方法：
除了继承的方法，还有以下方法
| **方法** | **说明** | 传入参数 |
| --- | --- | --- |
| `writeBoolean(boolean v)` | 写入 1 个字节，true 写为 1，false 写为 0 | 布尔值 |
| `writeByte(int v)` | 写入 1 个字节（只写低 8 位） | 整数值 |
| `writeShort(int v)` | 写入 2 个字节（只写低 16 位） | 整数值 |
| `writeChar(int v)` | 写入 2 个字节的字符 | 字符值 |
| `writeInt(int v)` | 写入 4 个字节的整数 | 整数值 |
| `writeLong(long v)` | 写入 8 个字节的长整数 | 长整数值 |
| `writeFloat(float v)` | 写入 4 个字节的浮点数 | 浮点数值 |
| `writeDouble(double v)` | 写入 8 个字节的双精度浮点数 | 双精度浮点数值 |
| `writeBytes(String s)` | 将字符串中每个字符的低 8 位写出；不适合写入一般 Unicode 文本 | 字符串 |
| `writeChars(String s)` | 将字符串中的每个字符按 2 个字节写出 | 字符串 |
| `writeUTF(String s)` | 以改良 UTF-8 格式写入字符串，并在前面写入字节长度 | 字符串 |
批量写入
| **方法** | **说明** | 传入参数 |
| --- | --- | --- |
| `write(int b)` | 写出一个字节（取低 8 位） | 整数值 |
| `write(byte[] b)` | 将数组中的字节写出 | 字节数组 |
| `write(byte[] b, int off, int len)` | 将数组从 off 位置开始的 len 个字节写出 | 字节数组，起始下标，写入字节数 |
| `flush()` | 刷新输出流，将缓冲的数据写到底层流 | 无 |
| `size()` | 返回目前写出的字节数 | 无 |
注意：
- 写入与读取时，数据类型和顺序必须对应；例如先 `writeInt()` 再 `writeDouble()`，读取时也应先 `readInt()` 再 `readDouble()`。
- `writeUTF()` 写入的是改良 UTF-8 格式，应使用 `DataInputStream.readUTF()` 读取；字符串编码后的长度不能超过 65535 字节。
- `DataOutputStream` 是普通输出流的包装流，关闭它时也会关闭底层输出流。
例子：
```java
try (DataOutputStream dos =
         new DataOutputStream(new FileOutputStream("data.bin"))) {
    dos.writeInt(100);
    dos.writeDouble(3.14);
    dos.writeUTF("Java");
} catch (IOException e) {
    e.printStackTrace();
}
```
