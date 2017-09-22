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

DNS服务器分为：
（1)master（主DNS服务器）：拥有区域数据的文件，并对整个区域数据进行管理。
（2）slave(从服务器或叫辅助服务器）：拥有主DNS服力器的区域文件的副 本，辅助主DNS服务器对客户端进行解析，当主DNS服务器坏了后，可以完全接替主服务器的工作。
（3）forward:将任何查询请求都转发给其他服务器。起到一个代理的作用。
（4）cache:缓存服务器。
（4）hint：根DNS internet服务器集。


{% include links.html %}
