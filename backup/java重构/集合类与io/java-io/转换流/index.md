---
{
  "id": "3fb5a2dd-8276-8081-b371-cdd53bee4b39",
  "url": "https://app.notion.com/p/3fb5a2dd82768081b371cdd53bee4b39",
  "created_time": "2026-10-16T09:24:00.000Z",
  "last_edited_time": "2026-10-17T07:18:00.000Z"
}
---

#  转换流

转换流相当于文件字节/字符流的一个工具类
如果想将一个类型的流传入另一个类型的流，传统的做法是遍历内容后写入另一个流
那有老铁问了：我记得前面讲过转换流类型的方法呀
这其实是个重大误区：前面有转换流流类型方法的类叫Stream[(Java 8) Stream流](https://app.notion.com/p/3f75a2dd827680bc91aecfd079a2a38c) ，它不隶属于java.io包，而是集合框架的东西，特性和方法完全不同（虽然都是流）
转换流就是专门用于**字节流和字符流之间相互转换**的
**（转换流转换的不是元素类型而是流类型）**
# InputStreamReader类（字节流➡️字符流）
作用：将字节流转换成字符流
构造方法：
```java
// 1. 使用平台默认字符集
InputStreamReader(InputStream in)

// 2. 使用指定字符集名称（最常用）
InputStreamReader(InputStream in, String charsetName)
    // charsetName 如 "UTF-8"、"GBK"，无效时抛 UnsupportedEncodingException
```
工作原理：传入字节流对象，返回字符流对象，这个类光调用构造方法就够用
# OutputStreamWriter类（字符流➡️字节流）
作用：将字符流转换成字节流
构造方法：
```java
// 1. 使用平台默认字符集
OutputStreamWriter(OutputStream out)

// 2. 使用指定字符集名称（最常用）
OutputStreamWriter(OutputStream out, String charsetName)
    // charsetName 如 "UTF-8"、"GBK"，无效时抛 UnsupportedEncodingException

```
工作原理：传入字符流对象，返回字节流对象，这个类光调用构造方法就够用
