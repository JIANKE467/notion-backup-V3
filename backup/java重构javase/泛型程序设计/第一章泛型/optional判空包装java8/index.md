---
{
  "id": "3e55a2dd-8276-80e1-8150-da88783a05d5",
  "url": "https://app.notion.com/p/Optional-Java8-3e55a2dd827680e18150da88783a05d5",
  "created_time": "2026-09-24T07:13:00.000Z",
  "last_edited_time": "2026-09-24T08:26:00.000Z"
}
---

#  Optional判空包装（Java8）

# 判空目的
Java虽说不让操作指针，但是有空指针异常的，如果你调用一个不存在的对象的方法，那么就会报错，所以某些时候我们无法确定传入的值是否为空，就需要判空（避免程序报错终止）
# 传统判空
传统判空使用if语句来判断
```java
public class Student{
	String name; 
	
	public void main(String[] args){
		if(name!=null){System.out.println(name);}
		else{System.out.println("name变量未赋值！");}
	}
}
```
这看起来是不是挺常规的
但如果是链式调用的判空就会出现if嵌套的情况，这对可读性及维护性很不利↓
```java
if (user != null) {
    Address address = user.getAddress();
    if (address != null) {
        String city = address.getCity();
        if (city != null) {
            System.out.println(city);
        }
    }
}

```
> PS：Java原生支持链式调用，像这样 `对象名.方法1().方法2().方法3()`
# 判空包装
原理很简单：Java自带了一个Optional类专门用来判空，将判空逻辑写到了该类的方法里
使用方法：创建该类的对象，将待判空的引用作为参数传入，调用该类的方法来获取判空结果
注意⚠️：
- Optional类不能直接new，而是使用其内部的三个方法`of` / `ofNullable` / `empty`来创建对象
- Optional类是泛型类，使用时需要声明类型
### 创建对象方法
Optional类不能直接new，而是使用其内部的三个方法`of` / `ofNullable` / `empty`来创建对象
| **方法** | **说明** | **示例** |
| --- | --- | --- |
| `empty()` | 创建空的 Optional对象 | `Optional.empty()` |
| `of(value)` | 包装值，**值不能为 null**，否则抛 NPE | `Optional.of("abc")` |
| `ofNullable(value)` | 包装值，**允许为 null**（推荐常用） | `Optional.ofNullable(maybeNull)` |
```java
Optional<String> opt1 = Optional.of(a);      // 不能传 null，传了直接报错
Optional<String> opt2 = Optional.ofNullable(a); // 可以传 null，返回空 Optional
Optional<String> opt3 = Optional.empty();          // 直接创建空的
```
### 获取判空结果（判空后操作）
**判断是否有值**
| **方法** | **说明** | **示例** |
| --- | --- | --- |
| `isPresent()` | 有值返回 true | `opt.isPresent()` |
| `isEmpty()` | 无值返回 true（Java 11+） | `opt.isEmpty()` |
**获取值**
| **方法** | **说明** | **示例** |
| --- | --- | --- |
| `get()` | 取值，**空则抛异常**（⚠️ 不推荐） | `opt.get()` |
| `orElse(默认值)` | 空则返回默认值 | `opt.orElse("默认")` |
| `orElseGet(供应者)` | 空则执行 lambda 生成默认值（**惰性**） | `opt.orElseGet(() -> "默认")` |
| `orElseThrow(异常)` | 空则抛指定异常 | `opt.orElseThrow(() -> new RuntimeException("空了"))` |
**消费值（有值时做事）**
| **方法** | **说明** | **示例** |
| --- | --- | --- |
| `ifPresent(消费者)` | 有值就执行，没值跳过 | `opt.ifPresent(v -> print(v))` |
| `ifPresentOrElse(消费者, Runnable)` | 有值执行前者，无值执行后者（Java 9+） | `opt.ifPresentOrElse(v -> print(v), () -> print("空"))` |
**转换值（链式调用的核心 ⭐）**
| **方法** | **说明** | **示例** |
| --- | --- | --- |
| `map(函数)` | 转换值，普通转换 | `opt.map(User::getName)` |
| `flatMap(函数)` | 转换值，**函数返回的本身是 Optional 时用** | `opt.flatMap(u -> Optional.ofNullable(u.getName()))` |
| `filter(谓词)` | 条件过滤，不满足变空 | `opt.filter(u -> u.getAge() >= 18)` |
**多选一（Java 9+）**
| **方法** | **说明** | **示例** |
| --- | --- | --- |
| `or(供应者)` | 空则换另一个 Optional | `opt.or(() -> Optional.of("备用"))` |
| `stream()` | 转成 Stream（有 0 或 1 个元素） | `opt.stream()` |
**其他**
| **方法** | **说明** | **示例** |
| --- | --- | --- |
| `equals(obj)` | 比较两个 Optional | `opt1.equals(opt2)` |
| `hashCode()` | 哈希值 | `opt.hashCode()` |
| `toString()` | 打印，形如 `Optional[abc]` 或 `Optional.empty` | `opt.toString()` |
# 链式调用示例
```java
private static void test(String str){
    Integer i = Optional.ofNullable(str).map(String::length).orElse(-1);
    System.out.println(i);
}
```
当然，一般会缩进成这种形式（好看）
```java
private static void test(String str){
    Integer i = Optional
            .ofNullable(str)   //创建对象
            .map(String::length)   //使用map来进行映射，将当前类型转换为其他类型，或者是进行处理
            .orElse(-1);
    System.out.println(i);
}
```
