---
{
  "id": "3155a2dd-8276-815f-9dff-d3c6a15495e4",
  "url": "https://www.notion.so/2-9-grep-wc-3155a2dd8276815f9dffd3c6a15495e4",
  "created_time": "2026-02-28T12:47:00.000Z",
  "last_edited_time": "2026-02-28T12:47:00.000Z"
}
---

#  2.9 grep，wc和管道符

# grep命令（通过关键字过滤出文件的行）
全名：global regular expression print 全局 正则表达式 打印
### 语法
```shell
grep [-n] 关键字 文件路径
```
PS：
- -n：number的意思，表示在结果中显示匹配的行号
- 关键字：目标行的关键字，当关键字含特殊符号和空格时用“”括起来
- 文件路径可以作为<u>标准输入</u>（注意⚠️：不能直接在这里写文本内容，因为用户的输入对命令来说不是标准输入，用户的输入是给shell看的，不是给grep命令看的 [ 前面提到过shell≠命令，所有命令都是一个单独的程序 ]）
# wc命令（文件内容统计）
全名：word count 数字数（统计）
但功能可不止数字数
### 语法
```shell
wc [-c -m -l -w] 文件路径
```
### 选项
| 选项 | 说明 |
| --- | --- |
| -c | 统计字节数（bytes） |
| -m | 统计字符数（characters） |
| -l | 统计行数（lines） |
| -w | 统计单词数（words） |
**不加选项默认输出格式：行数 字符数 字节数 文件名**
# 管道符 “|”
管道符的作用：将管道符左边命令的输出作为右边命令的输入
所以要使用grep命令PS的第三条要使用管道符
例子：将查看test.txt的命令输出作为查找ssbn所在行命令的输入（查找test.txt中ssbn所在行）
```shell
cat test.txt | grep ssbn
```
