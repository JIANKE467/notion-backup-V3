---
{
  "id": "3625a2dd-8276-8087-a010-eb4a876d0c08",
  "url": "https://app.notion.com/p/3625a2dd82768087a010eb4a876d0c08",
  "created_time": "2026-05-16T08:01:00.000Z",
  "last_edited_time": "2026-05-23T08:29:00.000Z"
}
---

#  背景设置

## 属性
background-color：背景颜色
background-image：背景图片
background-size：背景大小（搭配背景图片使用）
background-repeat：是否重复显示（搭配背景大小使用）
background-position：控制背景图片在盒子中的位置（搭配背景图片使用）
background-attachment：背景图片是否随着页面滚动
## 值
背景颜色
- 预设值：red，blue…
- rgb值

背景图片
- url(”地址”)

背景大小
- auto：默认，按图片固有尺寸显示，如果图片没有固有尺寸，则根据容器尺寸来显示。
- cover ：缩放背景图，保持比例，使其完全覆盖（优先窄边缩放）
- contain ：缩放背景图，保持比例，使其完全覆盖（优先宽边缩放，可能出现重复展示）
- 10px 10px：像素，破坏了原有比例
- 100% 100%：占父盒子百分比

是否重复显示
- no-repeat：不重复
- repeat：重复
- repeat x：重复x方向
- repeat y：重复y方向

图片位置
| 水平关键字 (X) | 垂直关键字 (Y) | 描述 |
| --- | --- | --- |
| left | top | 将图片左上角对齐容器的左上角。 |
| center | center | 将图片中心点对齐容器的中心点。 |
| right | bottom | 将图片右下角对齐容器的右下角。 |
例： `background-position: left center; `

- 也可以用百分比定义图片的中心相对于盒子的中心的偏移量
例：`background-position: 50% 50%`;
background-attachment：
- scroll：默认，背景跟着元素滚动

- fixed：背景固定，不跟页面滚动

- local：背景会跟随元素内部内容滚动
## 注意⚠️
background是前5个属性的简写属性，
background下的属性可以写到一起
（适当部分要加`/`分割避免歧义）
```css
.test {
  background: red no-repeat url("https://img2.baidu.com/it/u=4082245214,2139971588&fm=253&fmt=auto&app=120&f=JPEG?w=889&h=500") 10px 20px / contain;
  }
```
等于
```css
.test {  
background-color: red;	
background-image: url("https://img2.baidu.com/it/u=4082245214,2139971588&fm=253&fmt=auto&app=120&f=JPEG?w=889&h=500");	
background-repeat: no-repeat;	
background-position: 10px 20px;	
background-size: contain;}
```
