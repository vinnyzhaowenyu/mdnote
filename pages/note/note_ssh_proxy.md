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

### 原理分析

SSH本地端口转发是一种正向隧道技术,是一种将本地端口通过代理服务器映射到远程服务器的某个端口技术。

```
ssh -L [listen_Host:]listen_port:DST_Host:DST_port user@Tunnel_Host
```

* listen_Host : 可选，监听的机器IP，默认是本地接口。如果指定为IP地址，并且选项加-g时，其他能够访问该机器的机器也可通过该代理来访问远程的的服务。
* listen_port : 必选，监听的端口，如果是非root用户，指定的端口需要大于1024.
* DST_Host : 必选，远程提供服务器的机器
* DST_port : 必选，远程提供服务的端口


### 示例环境

#### 环境描述

> 现在有3台机器A1/B1/B2   
> A1是访问的发起者。IP为20.20.20.20    
> B网络是一个私网(192.168.1.0/24)    
> B1是B网络的公网跳板机，能够访问公网和内网。公网IP为30.30.30.30,内网IP为192.168.1.1   
> B2是B网络内网的一台服务器，只能内网(192.168.1.0/24)机器访问。内网IP是192.168.1.2   

#### 访问需求

要求在A1机器上能够访问B2机器上的80端口

#### 需求分析

A1机器是访问的发起者，可以是公网上的一台机器，也可以是某个内网的机器，只需要该机器能够访问公网B1机器即可。B1机器是B网络的一个跳板机，能够同时访问公网和内部网络。B2机器是B网络的内网一台机器，公网是不能直接访问的，但是B1机器却可以访问。

对于这样的环境，可以在A1机器上配置SSH本地端口转发功能，将请求通过B1转发到B2机器上。

#### 需求实现

在A1机器上执行配置命令

```
ssh -g -N -f -o ServerAliveInterval=60 -L 20.20.20.20:8888:192.168.1.2:80  root@30.30.30.30
```
通过访问20.20.20.20(A1机器)的8888端口，就可以转发请求到192.168.1.2的80端口。执行命令时需要输入30.30.30.30的root密码。

* -g : 允许其他机器访问该端口
* -N : 不执行命令，仅作为端口转发功能
* -f : 后台运行,不占用shell终端
* -o : 发送ssh存活请求
* -L : 配置本地端口转发功能

## SSH远程端口转发(R)

SSH远程端口转发是一种反向隧道技术，通过


### 示例环境

> 现在有3台机器C1/C2/D1
> C1是服务提供机器，只能内部网络访问。ip地址为:172.16.1.1
> C2也是内部服务器，但C2可以访问公网。ip地址为:172.16.1.2
> D1是公网上一台机器。ip地址为:40.40.40.40

### 访问需求

通过D1来访问C1的服务

### 需求分析

在C网络中没有公网跳板机，但是C2可以访问外网的情况，同时D1是C2可以访问的一台公网服务器，这时可用通过C2配置远程端口转发功能，就可以通过D1来访问C1的服务

### 需求实现

修改D1的SSHD配置`/etc/ssh/sshd_config`

```
GatewayPorts yes
```

在C2机器执行
```
ssh -g -N -f -o ServerAliveInterval=60 -R  40.40.40.40:8888:172.16.1.1:80  root@40.40.40.40
```

* -R 配置远程端口准发

在D1机器上访问8888端口就是访问C1的80端口


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
