---
{
  "id": "3d65a2dd-8276-80f0-b892-ed6ea5265187",
  "url": "https://app.notion.com/p/StringBuilder-3d65a2dd827680f0b892ed6ea5265187",
  "created_time": "2026-09-09T08:50:00.000Z",
  "last_edited_time": "2026-09-09T09:07:00.000Z"
}
---

#  StringBuilder类

# 什么是StringBuilder类？
由于String类不可修改的特性，每次拼接/截取都会产生新的对象，极大影响了效率
因此诞生了StringBuilder类
StringBuilder类和String类一样，都是存储字符串的数据类型，
但StringBuilder类允许修改存储内容，修改内容不会产生新对象，提高了效率
# 用法
注意⚠️：StringBuilder类不能像String一样直接赋值（String直接赋值实际上是语法糖，底层还是new一个对象），需要new一个对象，将要存储的值作为参数传入
```java
StringBuilder a = new StringBuilder("hello word")
```
# StringBuilder拥有的方法
| 方法 | 作用 | 示例 |
| --- | --- | --- |
| `append()` | 追加内容 | `sb.append("Hello")` |
| `insert()` | 在指定位置插入 | `sb.insert(0, "Hi ")` |
| `delete()` | 删除一段字符 | `sb.delete(0, 2)` |
| `deleteCharAt()` | 删除指定位置字符 | `sb.deleteCharAt(0)` |
| `replace()` | 替换一段字符 | `sb.replace(0, 5, "Java")` |
| `reverse()` | 字符串反转 | `sb.reverse()` |
| `toString()` | 转换成 `String` | `String s = sb.toString()` |
| `length()` | 获取当前长度 | `sb.length()` |
| `capacity()` | 获取当前容量 | `sb.capacity()` |
| `setCharAt()` | 修改指定位置字符 | `sb.setCharAt(0, 'J')` |
| `charAt()` | 获取指定位置字符 | `sb.charAt(0)` |
| `substring()` | 截取字符串 | `sb.substring(0, 3)` |
