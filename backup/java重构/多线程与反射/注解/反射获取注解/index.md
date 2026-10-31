---
{
  "id": "40a5a2dd-8276-8048-aaed-daa36aab02b0",
  "url": "https://app.notion.com/p/40a5a2dd82768048aaeddaa36aab02b0",
  "created_time": "2026-10-31T09:30:00.000Z",
  "last_edited_time": "2026-10-31T09:59:00.000Z"
}
---

#  反射获取注解

# 注意
注解需要指定**保留策略（保留到运行时）**才能在运行时被反射获取，否则注解早就被编译器删除了，运行时根本看不到
`@Retention(RetentionPolicy.值)`
> 注解定义时@Retention元注解的RetentionPolicy的值需要设置为RUNTIME
# 获取步骤
分不同情况
### 如果注解贴在类上（类前面）
1. 获取类的class对象
1. 调用class对象的getAnnotation方法获取注解对象（传入参数为：注解的类型.class）
1. getAnnotation方法返回该注解的一个**实例对象，**调用该对象的方法来查看注解成员的值
```java
Class<?> clazz = User.class;

// 获取指定注解
Table table = clazz.getAnnotation(Table.class);
if (table != null) {
    System.out.println(table.name());  // 输出: user
}


//其他方法见下面👇（正文部分就不详细介绍了）
// 判断是否存在某注解
boolean hasTable = clazz.isAnnotationPresent(Table.class);

// 获取所有注解（仅本类声明的）
Annotation[] declared = clazz.getDeclaredAnnotations();

// 获取所有注解（含继承的，仅对类有效）
Annotation[] all = clazz.getAnnotations();

```
### 如果注解贴在字段上
1. 获取类的class对象
1. 获取指定class对象中的指定成员（反射获取类的成员字段）[获取成员字段的方法](https://app.notion.com/p/4075a2dd827680f08728cb60e4e017a7#4075a2dd827680c2b491dfa4f9d08e08) 
1. 调用getAnnotation方法获取注解对象（传入参数为：注解的类型.class）
1. getAnnotation方法返回该注解的一个**实例对象，**调用该对象的方法来查看注解成员的值
### **获取构造器、参数上的注解**
这个省略，用到了再现查
