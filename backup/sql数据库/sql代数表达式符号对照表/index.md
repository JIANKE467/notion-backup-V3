---
{
  "id": "2ce5a2dd-8276-8125-91ec-fdd2eeb6706b",
  "url": "https://www.notion.so/SQL-2ce5a2dd8276812591ecfdd2eeb6706b",
  "created_time": "2025-12-19T08:18:00.000Z",
  "last_edited_time": "2025-12-19T08:19:00.000Z"
}
---

#  SQL代数表达式符号对照表

对照表：
| **关系代数操作** | **SQL语句** | **符号表示** | **说明** |
| --- | --- | --- | --- |
| 选择(Selection) | WHERE | σ (sigma) | 根据条件筛选行 |
| 投影(Projection) | SELECT | π (pi) | 选择特定的列 |
| 并(Union) | UNION | ∪ | 合并两个关系的所有元组 |
| 交(Intersection) | INTERSECT | ∩ | 两个关系的公共元组 |
| 差(Difference) | EXCEPT / MINUS | − | 在第一个关系但不在第二个关系中的元组 |
| 笛卡尔积(Cartesian Product) | CROSS JOIN | × | 两个关系的所有可能组合 |
| 连接(Join) | JOIN | ⋈ | 根据条件组合两个关系 |
| 自然连接(Natural Join) | NATURAL JOIN | ⋈ | 基于相同属性的连接 |
| 除(Division) | (复杂查询) | ÷ | 找出满足所有条件的元组 |
| 重命名(Rename) | AS | ρ (rho) | 重命名关系或属性 |
