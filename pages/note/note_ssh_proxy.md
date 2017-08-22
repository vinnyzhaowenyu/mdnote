---
title: SSH代理转发
keywords: aa 
last_updated: August 22, 2017
tags: [ssh]
summary: SSH Proxy 
sidebar: note_sidebar
permalink: note_ssh_proxy.html
folder: note 
---

## SSH本地端口转发(L)


正向隧道技术,将本地端口通过代理服务器映射到远程服务器的某个端口技术。

```
ssh -L [listen_Host:]listen_port:DST_Host:DST_port user@Tunnel_Host
```


推荐命令:
在SSH Client机器上执行
```
ssh -g -N -f -o ServerAliveInterval=60 \
-L <local port>:<remote host>:<remote port> username@<ssh server>
```

### 示例环境

#### 环境描述

> 现在有3台机器A/B1/B2   
> A是访问的发起者。IP为20.20.20.20    
> B1是B网络的公网跳板机，能够访问公网和内网。公网IP为30.30.30.30,内网IP为192.168.1.1   
> B2是B网络内网的一台服务器，只能内网机器访问。内网IP是192.168.1.2   

#### 访问需求

要求在A机器上能够访问B2机器上的80端口

#### 需求分析

A机器是访问的发起者，可以是公网上的一台机器，也可以是某个内网的机器，只需要该机器能够访问公网B1机器即可。B1机器是B网络的一个跳板机，能够同时访问公网和内部网络。B2机器是B网络的内网一台机器，公网是不能直接访问的，但是B1机器却可以访问。

对于这样的环境，可以在A机器上配置SSH本地端口转发功能，将请求通过B1转发到B2机器上。

#### 需求实现

在A机器上执行配置命令

```
ssh -g -N -f -o ServerAliveInterval=60 -L 20.20.20.20:8888:192.168.1.2:80  root@30.30.30.30
```
通过访问20.20.20.20(A机器)的8888端口，就可以转发请求到192.168.1.2的80端口。执行命令时需要输入30.30.30.30的root密码。

* -g : 允许其他机器访问该端口
* -N : 不执行命令，仅作为端口转发功能
* -f : 后台运行,不占用shell终端
* -o : 发送ssh存活请求
* -L : 配置本地端口转发功能






## SSH远程端口转发(R)

-R port:host:hostport #建立远程SSH隧道(隧道服务端建立监听端口)
将远程主机(服务器)的某个端口转发到本地端指定机器的指定端口. 
# 有本地映射肯定有远程映射，就是把-L换成-R，这样我们访问远程主机的端口就相当于访问本地的端口，但感觉作用不大。


## SSH动态端口转发(D)

-D port 
指定一个本地机器 “动态的’’ 应用程序端口转发. 
-D是该命令重要参数，他的后面跟着socks5服务器的地址与端口

## SSH图形转发(X)



ssh -C -f -N -L listen_port:DST_Host:DST_port user@Tunnel_Host 
ssh -C -f -N -R listen_port:DST_Host:DST_port user@Tunnel_Host 
ssh -C -f -N -D listen_port user@Tunnel_Host

## 参考

[http://hetaoo.iteye.com/blog/2299123](http://hetaoo.iteye.com/blog/2299123)

[http://www.linuxidc.com/Linux/2016-01/127868.htm](http://www.linuxidc.com/Linux/2016-01/127868.htm)

{% include links.html %}
