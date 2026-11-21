---
{
  "id": "3e85a2dd-8276-80c9-b950-f68a35efe174",
  "url": "https://app.notion.com/p/3e85a2dd827680c9b950f68a35efe174",
  "created_time": "2026-09-27T09:50:00.000Z",
  "last_edited_time": "2026-10-11T08:36:00.000Z"
}
---

#  “比较“相关接口

下面分成两种接口介绍：
# `Comparable`接口
### 作用：
`java.lang.Comparable` 接口，让类**自身**具备可比较的能力
### 工作原理：
1. 在类定义时实现`Comparable`接口并重写`compareTo()` 方法，来使得类拥有“比较”的能力
PS：`compareTo()` 方法用来定义比较规则
1. 在使用时调用排序算法（sort等方法）
1. 排序方法会在其内部调用compareTo() 方法并直接在原有对象的基础上进行排序
示例：
```java
//类定义

public class Test implements Comparable<Test>{
	int a;
	
	//构造方法，用来为成员变量a赋值
	public Test(int a){
	this.a=a;
	}
	
	//在类内重写compareTo()方法以获得比较的能力
	@Override
	public int compareTo(Test o) {
      return this.a - o.a;
      //这里简化了比较的过程，仅用a-b来实现
    }

	}

```
```java
//使用，以自然排序算法sort为例
Test test1 =new Test(5);
Test test2 =new Test(4);
test1.sort(test2);
```
### 关键方法说明
1. `compareTo()` 方法
作用：定义比较规则（比较哪个成员变量）
传入：被比较的元素（该数据结构**里的某个元素的引用）**
返回：正/负/零  类型的数值
注意：该方法只需要定义，无需手动调用，比较算法有关方法会自动在其内部调用。
使用：定义时在参数列表创建一个与被比较对象相同类型的局部变量，用于接收比较的对象，重写时可以使用减法来实现一个最简单的正负输出逻辑，调用时由排序算法自动调用（无需手动调用）

1. 排序算法（比较算法）
以`sort`方法为例↓（自然排序）
作用：直接在原对象基础上重新排序
传入：待排序的数据结构的对象（如数组）
返回：不会返回值，而是直接在原对象上做修改
使用：无需重写定义，在调用时传入待排序的数据结构的对象

# Comparator接口
### 作用：
Comparator也是一个比较器，但它适用于无法在数据结构实现类中实现`Comparable`接口及重写`compareTo()`方法的情况（代码不开源，无权限等）
这是一个外挂的比较器，而非`Comparable`接口那种将比较能力嵌入原类中
### 工作原理
1. 由于无法修改原类，因此单独定义一个比较器类，该类实现Comparator接口并重写`compare()`方法
1. 在使用时调用排序算法（sort等方法）
1. 排序方法会在其内部调用compare() 方法并直接在原有对象的基础上进行排序
```java
//原始类定义
class Person {
    String name; 
    int age;
    // 注意：没实现 Comparable！
}
```
```java
// 单独写的比较器类定义
class AgeComparator implements Comparator<Person> {
    @Override
    public int compare(Person p1, Person p2) {
        return p1.age-p2.age;   
    }
}
```
```java
// 调用
Person[] persons = {...};
Arrays.sort(persons, new AgeComparator());
```
### 关键方法说明
1. compare()方法
作用：定义比较规则（比较哪个成员变量）（外挂版）
传入：被比较的元素和比较的元素o1和o2（由于不能像compareTo方法嵌入原类，因此需要显示声明两个元素，且无法用“this”）
返回：正/负/零  类型的数值
注意：该方法只需要定义，无需手动调用，比较算法有关方法会自动在其内部调用。
使用：定义时在参数列表创建一个与被比较对象相同类型的局部变量，用于接收比较的对象，重写时可以使用减法来实现一个最简单的正负输出逻辑，调用时由排序算法自动调用（无需手动调用）

1. 排序算法（比较算法）
以`sort`方法为例↓（自然排序）
作用：直接在原对象基础上重新排序
传入：待排序的数据结构的对象（如数组）
返回：不会返回值，而是直接在原对象上做修改
使用：无需重写定义，在调用时传入待排序的数据结构的对象
