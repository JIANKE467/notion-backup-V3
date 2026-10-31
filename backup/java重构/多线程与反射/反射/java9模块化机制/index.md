---
{
  "id": "4095a2dd-8276-80d4-b569-eea950eb89d1",
  "url": "https://app.notion.com/p/Java9-4095a2dd827680d4b569eea950eb89d1",
  "created_time": "2026-10-30T02:18:00.000Z",
  "last_edited_time": "2026-10-30T03:25:00.000Z"
}
---

#  (Java9)模块化机制

# 解决什么痛点
Java9以前，访问权限由修饰符控制↓
| 访问修饰符 | 当前类 | 同一个包下的类 | 不同包下的子类 | 不同包下的类 |
| --- | --- | --- | --- | --- |
| public | ✅ | ✅ | ✅ | ✅ |
| protected | ✅ | ✅ | ✅ | ❌ |
| 默认 | ✅ | ✅ | ❌ | ❌ |
| private | ✅ | ❌ | ❌ | ❌ |
但这带来一个问题：包可以被伪造！
我可以写一个类，然后声明它属于某个包（即使它不属于这个包），这样就突破了传统的访问权限限制了
例子：
```java
//我不是Java.io包的类，但我就声明为Java.io，怎么滴😜
package java.io;
public class Hacker {
    //这里写恶意代码你不炸了😅
}
```
模块化机制则在向前兼容的同时，彻底堵死了通过乱声明包名来绕过权限控制的漏洞
# 模块化机制原理
通过在模块根目录创建`module-info.java`文件，并在该文件中定义哪些包可被外部访问
文件结构示例：
```java
demo/                          ← 根目录
├── greeting.module/           ← 模块1：提供功能
│   ├── module-info.java
│   └── com/
│       └── shop/
│           ├── api/
│           │   └── Greeter.java
│           └── internal/
│               └── SecretUtil.java
└── app.module/                ← 模块2：使用功能
    ├── module-info.java
    └── com/
        └── myapp/
            └── Main.java

```
- **`module-info.java`****文件权限控制的粒度是“包”，不能精确到“类”。** 你无法在 module-info 里写 “只导出 `Greeter` 这一个类”，只能声明暴露哪个包
# `module-info.java`文件
下面讲解`module-info.java`文件的编辑
### **完整语法骨架**
```java
[open] [注解] module 模块名 {
    requires  [static] [transitive] 模块名;
    exports   包名 [to 模块1, 模块2];
    opens     包名 [to 模块1, 模块2];
    uses      接口全名;
    provides  接口全名 with 实现类全名;
}
```
### **七大指令速查**
**module —— 模块声明**
```plain text
module com.shop.payment { }
```
- 模块名是唯一必须写的部分
- 命名惯例：反转域名（和包名一样），全局唯一
- 模块体内**什么都可以不写** —— 最小合法模块
**requires —— 我依赖谁**
```java
requires java.sql;                  
// 基本依赖(不能缺少）
requires static jackson.databind;   
// 可选依赖（运行时允许缺席）
requires transitive java.logging;   
// 传递依赖（下游自动继承）
```
- `static`：编译需要，运行可无 → 适合可选功能
- `transitive`：我的 API 签名用到了某模块的类型时必写 → 下游不用重复声明
- `java.base` 自动依赖，永远不用写
**exports —— 开放编译期访问（粒度=包）**
```java
exports 包名;                      
// 对所有模块开放的包
exports 包名 to 模块名;      
// 对特定模块开放的包
```
- ⚠️ 只能写**包名**，不能写到类
- ⚠️ 不递归：`com.shop.api` 和 `com.shop.api.model` 要各写一行
- 未导出的包 → 外部编译期 import 直接报错
**opens —— 开放运行期深反射**
```java
opens 包名;
// 允许所有模块对该包进行深反射
opens 包名 to 模块名;
// 只允许指定模块对该包进行深反射
```
- `opens` 解决的是运行时反射访问（例如框架反射读取私有字段），不是让外部代码在编译期 `import` 这个包
- `opens` 和 `exports` 不同：`exports` 面向普通编译期/运行期访问；`opens` 面向反射
**uses —— 声明我需要哪种服务**
```java
uses com.shop.spi.PaymentGateway;
```
- 写在服务消费者模块的 `module-info.java` 中
- 配合 `ServiceLoader` 查找服务实现；服务接口所在包必须对消费者可访问
**provides —— 声明我提供哪种服务实现**
```java
provides com.shop.spi.PaymentGateway
    with com.shop.payment.internal.AlipayGateway;
```
- 写在服务提供者模块中，`with` 后面是实现类
- 实现类所在包不必 `exports`；模块系统仍可通过服务机制找到实现
- 实现类需有 `public` 无参构造器，或提供符合规则的 `public static provider()` 方法
**open —— 整个模块开放深反射**
```java
open module com.shop.payment {
    // 其他 requires / exports / uses / provides 指令
}
```
- `open` 是 `module` 的修饰符，不是独立的模块指令；这里为便于速查，把它作为第七项
- 它会让模块内所有包都可被其他模块深反射，但不会让这些包在编译期自动可见，也不等于 `exports`
- `open module` 中不能再单独写 `opens` 指令；若只想开放少数包，应使用普通 `module` 加定向 `opens`

# 示例
```java
module com.shop.payment {
    requires java.sql;
    requires transitive java.logging;
    requires static jackson.databind;

    exports com.shop.api;                    // 对外门面包
    exports com.shop.spi to com.shop.app;    // 定向导出

    opens com.shop.model to spring.core, jackson.databind;

    uses com.shop.spi.RiskChecker;
    provides com.shop.spi.PaymentProvider
        with com.shop.internal.AlipayProvider;
}

```
