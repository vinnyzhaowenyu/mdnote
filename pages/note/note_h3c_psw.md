---
title: H3C汇聚层交换机
keywords: aa 
last_updated: June 28, 2017
tags: [getting_started]
summary: aa 
sidebar: note_sidebar
permalink: note_h3c_psw.html
folder: note 
---

显示汇聚层交换机接口配置的IP地址信息

display ip interface brief

```
[PSW1]display ip interface brief 
*down: administratively down
(s): spoofing
Interface                     Physical Protocol IP Address      Description 
FGE1/1/0/1                    up       up       172.31.1.1     CSW-1-For...
FGE1/1/0/3                    up       up       172.31.1.5     LSW-1-For...
FGE1/1/0/5                    down     down     172.31.1.9     LSW-2-For...
FGE1/2/0/1                    down     down     172.31.1.13    CSW-1-For...
FGE1/2/0/3                    down     down     172.31.1.17    LSW-1-For...
FGE1/2/0/5                    down     down     172.31.1.21    LSW-2-For...
FGE1/3/0/1                    up       up       172.31.1.25    ISW-1-For...
FGE1/3/0/3                    up       up       172.31.1.29    LSW-VPC-1...
```

查看路由表

```
[PSW1]display ip routing-table 

Destinations : 252	Routes : 314

Destination/Mask    Proto  Pre  Cost         NextHop         Interface
0.0.0.0/0           BGP    20   0            172.31.51.26    FGE1/3/0/1
0.0.0.0/32          Direct 0    0            127.0.0.1       InLoop0
8.8.8.8/32          BGP    20   0            172.31.51.86    FGE2/4/0/1
```

查看当前系统配置

```
[PSW1]display current-configuration 
#
 version 7.1.045, Release 2116
#
mdc Admin id 1
#
 sysname PSW-VM-G1-P1.AM24
#
```

{% include links.html %}
