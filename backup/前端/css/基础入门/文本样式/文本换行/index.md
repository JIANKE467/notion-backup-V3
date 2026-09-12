---
{
  "id": "3615a2dd-8276-8035-b27c-ddaef24ffdd2",
  "url": "https://app.notion.com/p/3615a2dd82768035b27cddaef24ffdd2",
  "created_time": "2026-05-15T07:50:00.000Z",
  "last_edited_time": "2026-05-15T08:03:00.000Z"
}
---

#  文本换行

## 属性
word-break：控制文本换行策略
overflow-wrap：控制长度超过一行的单词是否被拆分换行（该属性要与word-break属性配合使用）
text-wrap：新版控制文本换行策略（部分浏览器未支持）
## 值
word-break属性↓
- normal – 使用默认换行规则，禁止出现单词分割。
- break-all – 只要到达本行末尾，就强制对单词进行拆分。

overflow-wrap属性↓
- break-word

text-wrap属性↓
- wrap：自动换行
- nowrap：禁止换行
- balance – 平衡每行的字符数，让每一行看起来都舒适。
- pretty – 和默认换行相同，只是用户代理将使用较慢的算法，该算法更倾向于更好的布局而不是速度。
- stable – 和默认换行相同，只是当用户编辑内容时，他们正在编辑的行之前的行保持不变，这对于文本框来说很实用。
