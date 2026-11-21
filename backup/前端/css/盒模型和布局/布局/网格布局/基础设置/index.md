---
{
  "id": "3655a2dd-8276-80f7-8edd-d9dfa6b1a977",
  "url": "https://app.notion.com/p/3655a2dd827680f78eddd9dfa6b1a977",
  "created_time": "2026-05-19T09:54:00.000Z",
  "last_edited_time": "2026-05-19T10:19:00.000Z"
}
---

#  基础设置

网格中添加的每一个直接子元素会被自动放入到划分出来的网格中，我们一般称其为网格项
## 网格属性（需先将该盒子display属性设置成grid）
grid-template-columns ：控制行属性
grid-template-rows：控制列属性
gap：控制网格间隙
## 值
grid-template-columns/grid-template-rows属性：
- 100px 100px 100px：表示创建3个100px的行/列
- 1fr 1fr 1fr：表示将该容器横/纵向分3部分，每部分占比为1/3（网格占满容器）
- repeat()函数：下面讲

gap属性：
- 10px：间隙大小

## repeat（）函数：
语法
```css
repeat(行｜列数,尺寸)
```
行/列数可传入参数：
- auto-fill：自动，在不换行的情况下，尽可能多地往一行里塞入行/列
- 数字：指定行/列数
尺寸可传入参数：
- 像素数（单位：px）
- 1fr：分数比例（单位：fr）
- minmax(200px, 1fr)：minmax()函数，定义最小尺寸和行/列数
## PS
gap属性会牺牲一部分格子的大小来为格子之间留出空间，从而实现间距效果
