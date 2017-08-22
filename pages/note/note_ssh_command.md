---
title: SSH代理转发
keywords: aa 
last_updated: August 22, 2017
tags: [ssh]
summary: SSH Command 
sidebar: note_sidebar
permalink: note_ssh_command.html
folder: note 
---

```
SSH 命令参数 配置
-1：强制使用ssh协议版本1
-2：强制使用ssh协议版本2
-4：强制使用IPv4地址 
-6：强制使用IPv6地址 
-A：开启认证代理连接转发功能
-a：关闭认证代理连接转发功能
-b：使用本机指定地址作为对应连接的源ip地址
-C：请求压缩所有数据 
-F：指定ssh指令的配置文件
-f：后台执行ssh指令
-g：允许远程主机连接主机的转发端口
-i：指定身份文件 
-l：指定连接远程服务器登录用户名
-N：不执行远程指令
-o：指定配置选项
-p：指定远程服务器上的端口
-q：静默模式
-X：开启X11转发功能
-x：关闭X11转发功能
-y：开启信任X11转发功

-q表示该命令进入安静模式
-T是指该命令不占用shell
-N是指该命令不执行远程命令
-f是指该命令在后台运行
-D是该命令重要参数，他的后面跟着socks5服务器的地址与端口

-L port:host:hostport #建立本地SSH隧道(本地客户端建立监听端口)
将本地机(客户机)的某个端口转发到远端指定机器的指定端口. 

-R port:host:hostport #建立远程SSH隧道(隧道服务端建立监听端口)
将远程主机(服务器)的某个端口转发到本地端指定机器的指定端口. 
# 有本地映射肯定有远程映射，就是把-L换成-R，这样我们访问远程主机的端口就相当于访问本地的端口，但感觉作用不大。

-D port 
指定一个本地机器 “动态的’’ 应用程序端口转发. 

-C 压缩数据传输。

-N Do not execute a shell or command. 
不执行脚本或命令，仅仅做端口转发。通常与-f连用。
-f Fork into background after authentication. 
后台认证用户/密码，不用登录到远程主机。
```

{% include links.html %}
