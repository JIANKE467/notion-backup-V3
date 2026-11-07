---
{
  "id": "3b85a2dd-8276-8029-a23d-d4c31b27b2e7",
  "url": "https://app.notion.com/p/3b85a2dd82768029a23dd4c31b27b2e7",
  "created_time": "2026-08-10T14:19:00.000Z",
  "last_edited_time": "2026-08-11T12:42:00.000Z"
}
---

#  接口

# 接口
接口不是一种类（没有class）
接口比抽象类更抽象，抽象类中还可以实现部分方法，接口中不会实现任何方法
接口只描述了某一具体功能，不含任何细节（静态的除外）
接口使用关键字`interface`修饰
```java
public interface Test { 
}
```
- 在接口中定义方法会被自动添加public和abstract两个修饰符（Java会默认添加这两个修饰符，无需手写）
- 接口也不能实例化
- 接口中不允许存在成员变量和成员方法（只能有方法定义）
- 接口中定义的方法只能是public权限（必须让子类能看到才能实现）
# 接口实现
接口不通过继承实现，而是通过关键字`implements`实现
```java
public class Student extends Person implements 接口名{ 
}
```
另外，接口可以同时实现多个
```java
public class Student extends Person implements Study, A, B, C {  //多个接口的实现使用逗号隔开
  
}
```
# 将对象引用给接口
可以将对象引用给接口，和多态一样，此时对象只能使用接口中定义过的方法，不能使用类中有但接口中未定义过的方法
- 将对象引用给接口后，可以使用强制类型转换将其类型转换回对象原本的类型（向下转型）
# 接口继承
- 接口不能被类继承，但接口可以被接口继承，并且接口支持多继承
```java
public  子接口 extends 父接口A,B,C {
}
```
- 接口的继承其实就是接口功能融合
