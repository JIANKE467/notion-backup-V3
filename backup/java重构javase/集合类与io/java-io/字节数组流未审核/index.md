---
{
  "id": "3fd5a2dd-8276-8030-b039-e41b346a8081",
  "url": "https://app.notion.com/p/3fd5a2dd82768030b039e41b346a8081",
  "created_time": "2026-10-18T10:04:00.000Z",
  "last_edited_time": "2026-10-18T10:08:00.000Z"
}
---

#  字节数组流「未审核」

# 字节数组流是什么
字节数组流用 `byte[]` 作为数据来源或存放位置，在内存中读写字节，不直接操作文件。`ByteArrayOutputStream` 把写入的数据暂存在内部缓冲区；`toByteArray()` 可以取出这些数据。`ByteArrayInputStream` 则从已有的字节数组中读取数据。[[1]](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/ByteArrayOutputStream.html) [[2]](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/ByteArrayInputStream.html)
# 两个核心类
| 类 | 继承关系 | 作用 |
| --- | --- | --- |
| `ByteArrayOutputStream` | `OutputStream` | 把字节写入内存中的字节数组 |
| `ByteArrayInputStream` | `InputStream` | 从已有的字节数组中读取字节 |
常用构造方法：
| 构造方法 | 说明 |
| --- | --- |
| `ByteArrayOutputStream()` | 创建一个内存输出流 |
| `ByteArrayInputStream(byte[] buf)` | 用指定字节数组创建输入流 |
| `ByteArrayInputStream(byte[] buf, int offset, int length)` | 只读取数组中指定范围的字节 |
常用方法：
| 类 | 方法 | 说明 |
| --- | --- | --- |
| `ByteArrayOutputStream` | `write(...)` | 把字节写入内存缓冲区 |
| `ByteArrayOutputStream` | `toByteArray()` | 将已写入的数据复制到一个新的字节数组中 |
| `ByteArrayOutputStream` | `size()` / `reset()` | 查看当前字节数 / 清空已写入的数据 |
| `ByteArrayInputStream` | `read()` | 读取一个字节；读到末尾返回 `-1` |
| `ByteArrayInputStream` | `available()` | 查看还剩多少字节可读 |
# 使用示例
下面先把 `A、B、C` 对应的字节写入内存，再从字节数组中读出来：
```java
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;

public class ByteArrayStreamDemo {
    public static void main(String[] args) {
        byte[] source = {65, 66, 67}; // ASCII 中分别表示 A、B、C

        // 输出流：把字节写入内存
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        out.write(source, 0, source.length);
        byte[] data = out.toByteArray();

        // 输入流：从字节数组中读取
        ByteArrayInputStream in = new ByteArrayInputStream(data);
        int value;
        while ((value = in.read()) != -1) {
            System.out.print((char) value);
        }
    }
}
```
输出：`ABC`
# 适用场景与注意事项
- **适合临时处理内存中的字节数据**，例如先拼接数据，再交给其他流处理。
- 和 [文件字节流](https://app.notion.com/p/3f95a2dd827680b3b95fc29f692a2525) 不同，它不直接读写磁盘文件；需要保存到文件时，可再把数据写入文件流。
- 数据都放在内存中，处理特别大的数据时要留意内存占用。`toByteArray()` 会复制一份数据，也会额外占用内存。[[1]](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/ByteArrayOutputStream.html)
- 这两个字节数组流的 `close()` 不会产生实际影响；它们不负责释放文件等外部资源。[[2]](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/ByteArrayInputStream.html) [[1]](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/ByteArrayOutputStream.html)
**一句话记忆：**`ByteArrayOutputStream` 往内存里写，`ByteArrayInputStream` 从内存里的字节数组读。
