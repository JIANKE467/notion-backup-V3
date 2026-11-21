---
{
  "id": "3db5a2dd-8276-8083-b667-ded6509487e4",
  "url": "https://app.notion.com/p/3db5a2dd82768083b667ded6509487e4",
  "created_time": "2026-09-14T10:08:00.000Z",
  "last_edited_time": "2026-09-16T03:39:00.000Z"
}
---

#  异常类型


### 运行时异常`RuntimeException`
这种异常可以通过编译器，但运行时会报错，所有的运行时异常都继承自`RuntimeException`
### 编译时异常（受检异常）`Exception`
一般是逻辑错误，无法通过编译器，默认继承自`Exception`类的异常都是编译时异常
### 错误
错误比异常更严重，可能导致严重后果，如：`OutOfMemoryError`内存溢出错误可能导致JVM崩溃
所有错误都继承自Error类
