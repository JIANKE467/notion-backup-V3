---
{
  "id": "40a5a2dd-8276-8016-bfee-eefe373a5cb7",
  "url": "https://app.notion.com/p/40a5a2dd82768016bfeeeefe373a5cb7",
  "created_time": "2026-10-31T08:08:00.000Z",
  "last_edited_time": "2026-10-31T08:08:00.000Z"
}
---

#  **预设注解**

JDK预设了以下注解，作用于代码：
- [@Override](https://www.itbaima.cn/zh-CN/document/qrd0xfttsz32gpqg?segment=4)检查（仅仅是检查，不保留到运行时）该方法是否是重写方法。如果发现其父类，或者是引用的接口中并没有该方法时，会报编译错误。
- [@Deprecated](https://www.itbaima.cn/zh-CN/document/qrd0xfttsz32gpqg?segment=4)标记过时方法。如果使用该方法，会报编译警告。
- [@SuppressWarnings](https://www.itbaima.cn/zh-CN/document/qrd0xfttsz32gpqg?segment=4)指示编译器去忽略注解中声明的警告（仅仅编译器阶段，不保留到运行时）
- [@FunctionalInterface](https://www.itbaima.cn/zh-CN/document/qrd0xfttsz32gpqg?segment=4)Java 8 开始支持，标识一个匿名函数或函数式接口。
- [@SafeVarargs](https://www.itbaima.cn/zh-CN/document/qrd0xfttsz32gpqg?segment=4)Java 7 开始支持，忽略任何使用参数为泛型变量的方法或构造函数调用产生的警告。
