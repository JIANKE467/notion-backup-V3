---
{
  "id": "2c45a2dd-8276-8021-b686-d5d09f2abcfd",
  "url": "https://www.notion.so/12-2c45a2dd82768021b686d5d09f2abcfd",
  "created_time": "2025-12-09T03:10:00.000Z",
  "last_edited_time": "2025-12-10T06:33:00.000Z"
}
---

#  12. 存储引擎

# 体系结构（分四个层）
连接层：授权，认证，校验权限
服务层：sql接口，sql解析，sql优化
引擎层：（索引在引擎层实现）说明存储策略：存储，获取，更新方式
存储层：磁盘文件
# 存储引擎(不同表可以使用不同存储引擎)
**查询当前存储引擎：**
```sql
SHOW ENGINES;
```
**选择存储引擎：**
```sql
CREATE TABLE XXXXXX ENGINE=INNODB;
```
## 常见的存储引擎
| 引擎 | 事务 | 外键 | 行级锁 |
| --- | --- | --- | --- |
| INNODB | √ | √ | √ |
| MyISAM | x | x | 表锁 |
## 应用
INNODB：重要数据，数据完整性要求高的
MyISAM：不重要的数据
