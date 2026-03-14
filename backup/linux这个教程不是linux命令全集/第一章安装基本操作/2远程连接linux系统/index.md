---
{
  "id": "3155a2dd-8276-8121-ad49-cbbba634fbc4",
  "url": "https://www.notion.so/2-linux-3155a2dd82768121ad49cbbba634fbc4",
  "created_time": "2026-02-28T12:47:00.000Z",
  "last_edited_time": "2026-02-28T12:47:00.000Z"
}
---

#  2.远程连接linux系统

# 通过FinalShell远程连接
Final shell：更方便的命令行工具
### 连接方法
现在虚拟机里登录CentOS
桌面右键打开命令行
输入  ifconfig
找到IP地址
回到final shell，点文件夹图标→最左侧的白色文件夹→ssh连接→输入相应内容即可
PS：
连接不上大概率是因为IP地址不对，注意不能使用127.0.0.1（那是本地回环）和192.168.122.1（那是vmware虚拟网桥）

小概率是因为vmware程序损坏，重新安装即可
