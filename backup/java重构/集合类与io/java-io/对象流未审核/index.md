---
{
  "id": "3fd5a2dd-8276-80f3-b47d-eb139b694beb",
  "url": "https://app.notion.com/p/3fd5a2dd827680f3b47deb139b694beb",
  "created_time": "2026-10-18T09:39:00.000Z",
  "last_edited_time": "2026-10-18T10:03:00.000Z"
}
---

#  对象流「未审核」

# 对象流是什么
对象流用于读写 Java 对象：把对象及其引用关系转换为字节序列，或从字节序列中恢复对象。这个过程分别称为**序列化**和**反序列化**。
对象流写出的不只是字段值，还包含恢复对象所需的类描述信息和对象引用信息（对象图）；方法的代码不会被序列化。对象流通常包装普通字节流（如文件字节流）使用。
| 操作 | 使用的类 | 作用 |
| --- | --- | --- |
| 序列化 | `ObjectOutputStream` | 将对象写入底层输出流 |
| 反序列化 | `ObjectInputStream` | 从底层输入流中读取并恢复对象 |
**注意：**对象流不是 `FilterInputStream` / `FilterOutputStream` 的子类，但构造时都需要传入一个普通输入或输出流。
# ObjectOutputStream（对象序列化）
作用：将对象及其对象图写入底层输出流。
继承与实现：继承自 `OutputStream`，并实现 `ObjectOutput` 接口。
构造方法：
| 构造方法 | 说明 |
| --- | --- |
| `ObjectOutputStream(OutputStream out)` | 将对象写入指定的输出流；创建时会写入对象流头信息 |
常用方法：
| 方法 | 说明 | 传入参数 |
| --- | --- | --- |
| `writeObject(Object obj)` | 序列化对象并写出；对象及其可达引用对象也会按规则处理 | 对象引用 |
| `writeUnshared(Object obj)` | 以非共享方式写出指定对象 | 对象引用 |
| `reset()` | 重置对象流的共享引用状态，后续写出时不复用之前记录的对象句柄 | 无 |
| `flush()` | 刷新输出流，将缓冲内容写到底层流 | 无 |
| `close()` | 关闭对象流及其底层输出流 | 无 |
`defaultWriteObject()`、`putFields()` 等方法用于类自定义序列化实现，通常在类的 `writeObject` 特殊方法中使用，初学时一般不需要直接调用。
# ObjectInputStream（对象反序列化）
作用：从底层输入流读取对象数据，并恢复对象。
继承与实现：继承自 `InputStream`，并实现 `ObjectInput` 接口。
构造方法：
| 构造方法 | 说明 |
| --- | --- |
| `ObjectInputStream(InputStream in)` | 从指定输入流读取对象；会读取并校验对象流头信息 |
常用方法：
| 方法 | 返回类型 | 说明 | 传入参数 |
| --- | --- | --- | --- |
| `readObject()` | `Object` | 读取并恢复一个对象；可能抛出 `ClassNotFoundException` | 无 |
| `readUnshared()` | `Object` | 以非共享方式读取一个对象 | 无 |
| `available()` | `int` | 返回可在不阻塞情况下读取的字节数估计值，不代表对象数量 | 无 |
| `close()` | `void` | 关闭对象流及其底层输入流 | 无 |
`defaultReadObject()`、`readFields()` 等方法用于类自定义反序列化实现，通常不需要在普通读取代码中直接调用。
# 使用示例
对象所属的类需要实现 `Serializable`。它是一个标记接口，不需要实现额外方法。
```java
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

public class ObjectStreamDemo {
    static class Person implements Serializable {
        private static final long serialVersionUID = 1L;

        private String name;
        private int age;

        Person(String name, int age) {
            this.name = name;
            this.age = age;
        }

        @Override
        public String toString() {
            return "Person{name='" + name + "', age=" + age + "}";
        }
    }

    public static void main(String[] args) {
        // 序列化：把对象写入文件
        try (ObjectOutputStream out = new ObjectOutputStream(
                new FileOutputStream("person.dat"))) {
            out.writeObject(new Person("小明", 18));
        } catch (IOException e) {
            e.printStackTrace();
        }

        // 反序列化：从文件恢复对象
        try (ObjectInputStream in = new ObjectInputStream(
                new FileInputStream("person.dat"))) {
            Person person = (Person) in.readObject();
            System.out.println(person);
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
```
# 序列化注意事项
- **类必须支持序列化：**对象的类需要实现 `java.io.Serializable`。如果对象图中包含其他对象，这些对象通常也需要可序列化；否则写出时可能抛出 `NotSerializableException`。不需要保存的字段可考虑声明为 `transient`，或使用自定义序列化逻辑。
- **静态字段不属于对象实例状态：**`static` 字段不会作为该对象的实例字段被序列化；`transient` 字段也不会按默认规则写出，反序列化后通常为默认值（如 `null`、`0`、`false`）。
- **声明 `serialVersionUID`：**它用于检查序列化版本兼容性。类的版本不兼容时，反序列化可能抛出 `InvalidClassException`。显式声明可避免仅依赖编译器计算的默认值。
- **读写顺序要对应：**连续写入多个对象时，读取端应按相同顺序调用 `readObject()`，并将返回的 `Object` 转换为正确类型。
- **对象引用会被跟踪：**对象流能够保留对象之间的共享引用和循环引用。同一个对象重复写出时，流可能复用已记录的引用；若需要在同一流中重新写出对象的最新状态，可在适当位置调用 `reset()`。
- **不要反序列化不可信数据：**反序列化可能触发对象构造相关逻辑，带来安全风险；只处理可信来源的数据。
- 关闭对象流也会关闭它包装的底层流。优先使用 `try-with-resources` 管理资源。
# 与数据流的区别
| 对比项 | 对象流 | 数据流 |
| --- | --- | --- |
| 主要用途 | 读写对象及其对象引用关系 | 按基本数据类型读写值 |
| 典型方法 | `writeObject()`、`readObject()` | `writeInt()`、`readInt()`、`writeUTF()`、`readUTF()` |
| 使用要求 | 对象类需支持序列化 | 读写双方需约定相同的数据类型和顺序 |
| 常见底层流 | 文件字节流、网络字节流等 | 文件字节流、网络字节流等 |
