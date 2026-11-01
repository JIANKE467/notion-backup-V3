---
{
  "id": "3b15a2dd-8276-806a-9827-ee5e02c735c3",
  "url": "https://app.notion.com/p/3b15a2dd8276806a9827ee5e02c735c3",
  "created_time": "2026-08-03T12:03:00.000Z",
  "last_edited_time": "2026-08-03T13:24:00.000Z"
}
---

#  包声明和导入

# 包的作用
包用来给类分类，大项目有很多的类，这时我们可以使用包将功能类似的类放到一个包中
# 包的命名
建议使用域名反写来命名
```java
com.baidu
```
### 注意⚠️
- **当一个类加入包中后，*****需要在类的最上面添加package关键字来指明当前类所处的包***
```java
package com.test;   //在放入包中，需要在类的最上面添加package关键字来指明当前类所处的包

public class Main {   //将Main类放到com.test这个包中
    public static void main(String[] args) {

    }
}
```
# 包的导入
> **使用同一个包下的类，不需要导入包**
  **使用不同包下的类需要先导入包（使用import关键字）**
```java
package com.test;

import com.test.entity.Person;   //使用import关键字导入其他包中的类

public class Main {
    public static void main(String[] args) {
        Person person = new Person();   //只有导入之后才可以使用，否则编译器不知道这个类从哪来的
    }
}
```
- 可以使用`*`表示导入这个包中全部的类
- Java中会默认导入`java.lang`这个包下的所有类（所以println等常用方法无需导入也能使用）
- 主方法一般这样简写`public static void main(String[] args) `，但如果发生歧异（在当前包里创建了String类），就需要写全来显示声明`public static void main(java.lang.String[] args) `
- **在调用方法/变量时，如果不声明包名，则默认为在当前包下寻找（不声明类名，默认在当前类下寻找）**
- Java 5 引入了静态导入，它允许你**直接使用其他类中的静态变量或静态方法，而不用写类名**
  ```java
import static 包名.类名.静态成员名;
import static 包名.类名.*;  //可以使用*通配符导入所有静态成员
  ```
# 吐槽
Java为什么允许创建名叫Sring的类啊？这下好了，又多一个特性
想保持逻辑统一性你就让他把主方法写全呀，现在主方法已经有三种写法了（难绷）
