---
{
  "id": "40a5a2dd-8276-806c-9e8e-daf4b9d29879",
  "url": "https://app.notion.com/p/40a5a2dd8276806c9e8edaf4b9d29879",
  "created_time": "2026-10-31T06:29:00.000Z",
  "last_edited_time": "2026-10-31T07:35:00.000Z"
}
---

#  类加载器

## 说在最前面
本节内容应用于框架开发，一般开发者仅了解原理即可
## 一、类加载器介绍
### 是什么
类加载器是 JVM 中负责把 `.class` 字节码文件读入内存、并生成对应 `java.lang.Class` 对象的组件。
- 类加载器在程序**第一次使用某个类时**才加载它（按需加载），而非启动时全部加载。
- 同一个类（同一个加载器 + 同一个类名）在 JVM 中**只加载一次**，对应唯一的 `Class` 对象。
- JVM 内置三层加载器，构成父子层级：
| 加载器 | 加载范围 | 说明 |
|---|---|---|
| Bootstrap ClassLoader | `JRE/lib` 核心类库 | C++ 实现，Java 层拿不到引用（返回 `null`） |
| Extension ClassLoader | `JRE/lib/ext` | JDK 9 后被 Platform ClassLoader 替代 |
| Application ClassLoader | 用户 classpath | 程序默认使用的加载器 |
| 自定义 ClassLoader | 任意来源 | 用户继承 `ClassLoader` 实现 |
### 工作原理
1. 双亲委派机制
收到加载请求时，先逐层**向上委托**给父加载器，父加载器加载不了才由自己加载。
- **作用**：① 避免类重复加载；② 防止核心类被篡改（如自定义的 `java.lang.String` 不会被加载）。
```java
// 观察加载器层级
ClassLoader loader = Demo.class.getClassLoader();
System.out.println(loader);                 // AppClassLoader
System.out.println(loader.getParent());     // ExtClassLoader
System.out.println(loader.getParent().getParent()); // null（Bootstrap是C++实现的）
```
2. 加载流程
```plain text
loadClass()  →  先查缓存 → 委托父加载器 → 父加载不了 → findClass()
findClass()  →  子类重写，定义"字节码从哪来"
defineClass() → 把 byte[] 转成 Class 对象
```
3. 类的完整生命周期（了解）
加载 → 验证 → 准备 → 解析 → 初始化 → 使用 → 卸载
- **准备阶段**：静态变量分配内存并赋**默认值**（`static int a = 1` 此时是 0）。
- **初始化阶段**：执行静态变量显式赋值和静态代码块。
- **缓存机制**：加载过的类会被缓存——所以改了 `.class` 文件必须重启 JVM 才生效。
---
## 二、自定义类加载器
### 为什么自定义？
内置加载器只认固定位置（classpath / JDK 目录）和固定规则。以下场景它们干不了：
| 场景 | 说明 |
| --- | --- |
| **非标准来源的类** | 类在网络上、数据库里、加密文件中（运行时解密加载，防反编译） |
| **热部署** | JVM 对同名类只加载一次；换新加载器实例即可重新加载新字节码 |
| **类隔离** | JVM 中类的身份 = 类名 + 加载器实例；给每个应用独立加载器，同名类不同版本可共存（Tomcat、OSGi） |
| **SPI 回调** | 核心接口由 Bootstrap 加载，但实现在 classpath 里，父加载器"看不见"，需线程上下文类加载器 |
### 如何自定义？
**三步**：继承 `ClassLoader` → 重写 `findClass()` → 在其中调用 `defineClass()`。
```java
public class MyClassLoader extends ClassLoader {
    private String classPath;
    public MyClassLoader(String classPath) {
        this.classPath = classPath;
    }
    @Override
    protected Class<?> findClass(String name) throws ClassNotFoundException {
        byte[] data = loadClassData(name);      // 自定义：字节码从哪来
        if (data == null) {
            throw new ClassNotFoundException(name);
        }
        return defineClass(name, data, 0, data.length);  // 字节 → Class对象
    }
    private byte[] loadClassData(String name) throws IOException {
        // 类名 → 文件路径，读取字节码
        String fileName = classPath + File.separator
                + name.replace('.', File.separatorChar) + ".class";
        return Files.readAllBytes(Paths.get(fileName));
    }
}
```
使用（注意走 `loadClass` 而非 `findClass`，保留双亲委派）：
```java
MyClassLoader loader = new MyClassLoader("/some/path");
Class<?> clazz = loader.loadClass("com.test.Test");
Object obj = clazz.getDeclaredConstructor().newInstance();  // 反射创建实例
```
**关键注意点**：
- **重写 ****`findClass`**** 而不是 ****`loadClass`**：`loadClass` 里有双亲委派逻辑，重写它会破坏委派机制（除非有意为之，如 Tomcat）。
- **不要重复 ****`defineClass`**：同一个加载器对同一个类二次 define 会抛 `LinkageError`。
- **`defineClass`**** 有安全检查**：`java.*` 开头的包名直接抛 `SecurityException`——塞不进假的 `String`。
- **坑**：两个不同加载器加载的同名类是**两个不兼容的类型**，强转会抛 `ClassCastException`（报错信息里类名完全相同，非常迷惑）。
