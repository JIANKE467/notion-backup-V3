---
{
  "id": "3d45a2dd-8276-8006-a11b-fdfa43d46bb5",
  "url": "https://app.notion.com/p/String-3d45a2dd82768006a11bfdfa43d46bb5",
  "created_time": "2026-09-07T09:02:00.000Z",
  "last_edited_time": "2026-09-09T08:28:00.000Z"
}
---

#  String类

String本身也是一个类，只不过它比较特殊，每个用双引号括起来的字符串，都是String类型的一个实例对象：
```java
public static void main(String[] args) {
    String str = "Hello World!";
}
```
注意⚠️：使用双引号创建的两个字符串，如果内容相同，JVM会优化为同一个对象
注意⚠️：使用构造方法创建的两个字符串，内容相同，也不会被优化为一个对象
# 语法
```java
String 变量名;
```
和基本数据类型使用方法一致，不再赘述
# String类拥有的方法
String的对象名就是String引号内的字符串
### 获取字符串信息
1. `length()`获取长度
1. `isEmpty()` 判断是否为空字符串
1. `isBlank()`判断是否为空或空白
1. `charAt(i)` 获取第i个字符
### 查找字符串
- `indexOf()`：第一次出现的位置
- `lastIndexOf()`：最后一次出现的位置
- `contains()`：是否包含
- `startsWith()`：是否以某内容开头
- `endsWith()`：是否以某内容结尾
### 比较字符串内容
- `equals()`：比较内容是否相同
- `equalsIgnoreCase()`：忽略大小写比较内容
- `compareTo()`：比较字典顺序
- `compareToIgnoreCase()`：忽略大小写比较顺序
### 截取字符串
- `substring(6)`：从指定位置截取到结尾
- `substring(0, 5)`：截取 `[0,5)`
### 替换字符串
- `replace()`：替换所有匹配内容
- `replaceFirst()`：替换第一个匹配内容
- `replaceAll()`：使用正则表达式替换
### 去除空白
- `trim()`：去除首尾空白
- `strip()`：去除首尾 Unicode 空白
- `stripLeading()`：去除开头空白
- `stripTrailing()`：去除结尾空白
### 转换大小写
- `toUpperCase()`：转大写
- `toLowerCase()`：转小写
