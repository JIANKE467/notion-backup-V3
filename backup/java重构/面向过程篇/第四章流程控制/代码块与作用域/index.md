---
{
  "id": "3a85a2dd-8276-8016-817d-f95b8083f63a",
  "url": "https://app.notion.com/p/3a85a2dd82768016817df95b8083f63a",
  "created_time": "2026-07-25T07:33:00.000Z",
  "last_edited_time": "2026-07-25T07:40:00.000Z"
}
---

#  代码块与作用域

除了类，方法等需要用花括号包裹内容外，也可以随意创建代码块，如
```java
public static void main(String[] args) {
    int a = 10;   //此时变量在最外层定义
     {
     System.out.println(a);   //处于其作用域内部的代码块可以使用
     }
    System.out.println(a);   //这里肯定也可以使用
}
```
- 创建代码块不会改变执行顺序(仍然按先后顺序执行）
- 代码块会改变其中变量的作用域（在代码块中定义的变量作用域只能在代码块中）
