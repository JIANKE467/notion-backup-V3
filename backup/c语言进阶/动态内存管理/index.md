---
{
  "id": "2785a2dd-8276-80c6-868b-c08137a685df",
  "url": "https://www.notion.so/2785a2dd827680c6868bc08137a685df",
  "created_time": "2025-09-24T08:45:00.000Z",
  "last_edited_time": "2025-09-24T09:39:00.000Z"
}
---

#  动态内存管理

## malloc（开辟自定义个字节的内存空间）
malloc的返回值是指针
**malloc需要强制类型转换成要存储的数据的类型（需要转换成指针型，如int*，float*，用int则malloc的返回值会丢失指针的属性）**
用法：
将malloc赋给一个指针
```c
数据类型*指针变量名=（数据类型*）malloc（字节大小）
```
