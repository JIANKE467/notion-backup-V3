---
{
  "id": "35f5a2dd-8276-802a-a181-ca97f8df0dfb",
  "url": "https://app.notion.com/p/35f5a2dd8276802aa181ca97f8df0dfb",
  "created_time": "2026-05-13T08:18:00.000Z",
  "last_edited_time": "2026-05-15T08:28:00.000Z"
}
---

#  字体样式


[文本字体](文本字体/index.md)
  # 指定字体
  CSS使用`font-family`属性来指定字体
  - 可以同时设置多种字体来增强兼容性（优先级从左向右）
  ```css
p {  font-family: 'Microsoft YaHei', 'PingFang SC';}
  ```
  - 可以不指定具体字体，而是指定字体族（更有兼容性）
  ### 字体族：
  **字体族不代表具体字体，只代表某种字体风格**
  serif（衬线字体）
  sans-serif（无衬线字体）
  monospace（等宽字体）
  cursive（手写字体）
  fantasy（奇幻字体）
  # 自定义字体
  使用`@font-face`做选择器名来创建自定义字体：
  需要指定属性↓
  `font-family`字体名称
   `src`字体地址
  ```css
@font-face {  
font-family: 'YuanShen';  
src: url("../font/yuanshen.ttf");  
/* 使用url("")函数来指定位置，注意这个不一定是本地文件，甚至可以是一个网络文件 */
}
  ```
  # 注意
  字体属性会被自动继承
[字体大小](字体大小/index.md)
  ## 相关属性
  font-size属性：控制字体大小，后面接大小和单位
  值写法：使用small等预设值，或`大小+单位`
  字体大小有相对大小和绝对大小
  ## 绝对大小
  单位：px（像素）
  **此外，small，meidum、large、x-large等预设值，都是绝对尺寸**
  注意：
  - 像素都是整数，不要写浮点像素
  - 默认文本大小：16px
  - h1等标签也可以修改字体大小
  ## 相对大小
  单位：em 或 rem
  - 1.5em表示是其父元素的大小的1.5倍
  - 2rem表示是跟元素的2倍
  - 默认文本大小：16px
[字重](字重/index.md)
  字重就是字体粗细
  ## 相关属性
  font-weight：控制字体粗细
  ## PS
  - 有些字体不支持调整粗细（部分浏览器会自动做一定兼容）
  - 默认粗细是400
  - 字体粗细范围100~900
[字体风格](字体风格/index.md)
  目前只支持斜体和正常两种风格（默认正常）
  ## 斜体
  属性：font-style
  值：italic（斜体）（就这一个）
  ## PS
  部分字体不支持斜体
[字体颜色](字体颜色/index.md)
  ## 相关属性
  color：控制颜色
  ## 预设值
  有red，blue，green…等
  ## RGB值
  需要使用 rgb() 函数
  ```css
.test{
color:rgb(r值,g值,b值);
}
  ```
  或
  用16进制表示三个值↓
  ```css
.test{
color:#FFFFFF;
}
  ```
  ### PS
  - rgb范围：0~255
  - rgb表示法也可以表示阿尔法通道（透明度）：需要使用 rgba() 函数 或直接16进制表示
  - 阿尔法通道范围：0~1（小数）
  - α通道16进制表示时范围是：0~255
