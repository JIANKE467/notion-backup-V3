---
{
  "id": "3155a2dd-8276-81fc-9589-d42f7153e528",
  "url": "https://www.notion.so/3155a2dd827681fc9589d42f7153e528",
  "created_time": "2026-02-28T12:47:00.000Z",
  "last_edited_time": "2026-02-28T12:47:00.000Z"
}
---

#  第一章：安装/基本操作

[1.认识/安装linux系统](1认识安装linux系统/index.md)
  linux系统=linux发行版=linux内核+系统级程序
  自己编译系统=自己集成系统级程序
  ### 安装
  安装有简易安装和正常安装，简易安装全过程自动，正常安装需设置账户和配置
  安装过程：
  下载ISO镜像
  安装到vmware
  结束
[2.远程连接linux系统](2远程连接linux系统/index.md)
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
[3.配置wsl（Windows10+）](3配置wslwindows10/index.md)
  ### WSL是Windows下的linux子系统
  在设置→应用和功能→程序和功能→启用和关闭Windows功能→勾选Linux的Windows子系统
  ### 然后再微软商店直接搜索Ubuntu下载即可
  ### 建议一并下载Windows terminal
  Windows terminal：更好用的cmd
  ### 在Windows terminal中使用Ubuntu
  打开Windows terminal
  点加号旁边的折叠按钮
  选择Ubuntu
[4.虚拟机快照](4虚拟机快照/index.md)
  Vmware虚拟机支持为虚拟机制作快照
  快照可以将当前虚拟机状态保存，在日后出现故障，可以重新恢复到当前状态。
  拍快照：VMware左侧栏找到相应虚拟机右键→快照→拍摄快照
  恢复快照：…相应虚拟机右键→快照→快照管理器→点击相应快照→点下面“转到”（恢复）
  建议关机恢复和拍快照
