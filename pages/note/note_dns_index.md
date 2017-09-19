---
title: DNS介绍
keywords: dns,service 
last_updated: August 10, 2017
tags: [dns,service]
summary: dns 
sidebar: note_sidebar
permalink: note_dns_index.html
folder: note 
---

## DNS功能
DNS的功能是提供**域名**<-->**IP**的解析。类似ARP表，MAC，IP路由表，提供一种转换对应方式。

### 正向解析
根据域名或主机名查找对应的IP地址

### 反向解析
根据IP地址查找对应的域名或主机名

### 缓存域名服务器
将从其他域名服务器查询的解析缓存，并提供DNS高速解析功能

### 主域名服务器
特定DNS区域的官方服务器，具有唯一性。负责该区域内所有的域名解析记录

### 从域名服务器
辅助域名服务器，维护的解析记录来源于主域名服务器

## DNS解析原理



## 搭建DNS服务软件

DNS服务普遍使用：BIND（Berkeley Internet Name Daemon）

官方站点：https://www.isc.org/

相关软件包：
```
bind-9.3.3-7.el5.i386.rpm
bind-utils-9.3.3-7.el5.i386.rpm
bind-chroot-9.3.3-7.el5.i386.rpm
caching-nameserver-9.3.3-7.el5.i386.rpm
```
- bind : 提供了域名服务的主要程序及相关文件   
- bind-utils : 提供了对DNS服务器的测试工具程序（如nslookup、dig等）   
- bind-chroot : 为bind提供一个伪装的根目录以增强安全性（将“/var/named/chroot/”文件夹作为BIND的根目录)，不安装该软件会以/var/named/为根目录
- caching-nameserver : 为配置BIND作为缓存域名服务器提供必要的默认配置文件，这些文件在配置主、从域名服务器时也可以作为参考   
 
named作为标准的系统服务脚本，通过`service named start/stop/restart`的形式可以实现对服务器程序的控制

named默认监听TCP、UDP协议的53端口，以及TCP的953端口：

其中UDP 53端口一般对所有客户机开放，以提供解析服务;TCP 53端口一般只对特定从域名服务器开放，提高解析记录传输通道；TCP 953端口默认只对本机（127.0.0.1）开放，用于为rndc远程管理工具提供控制通道

如果没有安装bind-chroot软件包，则主配置文件默认位于 /etc/named.conf，数据文件默认保存在 /var/named/ 目录


### 

{% include links.html %}
