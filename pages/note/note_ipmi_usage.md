---
title: IPMI使用
keywords: impi 
last_updated: June 15, 2017
tags: [getting_started]
summary: ipmi 
sidebar: note_sidebar
permalink: note_ipmi_usage.html
folder: note 
---

## 带外接口

|接口种类|
|--|--|
|open|          Linux OpenIPMI 接口 [默认的接口]|
|imb |          Intel IMB 接口|
|lan |           IPMI v1.5 LAN 接口|
|lanplus   |    IPMI v2.0 RMCP+ LAN 接口|
|serial-terminal  |  串行接口, 终端模式|
|serial-basic     |  串行接口, 基础模式|
|usb       |    IPMI USB 接口(OEM 接口 for AMI 设备) |

## 电源管理


```
ipmitool -I lanplus -H $ip -U $username -P $pwd power reset/on/off/status
```

|power电源参数|
|--|--|
|reset | 关闭电源并重启机器 |
|on | 服务器上电 |
|off | 服务器下电 |
|status | 查看电源状态 |

* -I : 接口类型
* -H : 带外IP地址
* -U : 带外登录用户名
* -P : 带外登录密码

##  设置引导方式

将下次开机引导方式进行设置

```
ipmitool -I lanplus -H $ip -U $username -P $pwd chassis bootdev pxe/disk/cdrom
```

| bootdev 引导方式设置 |
| -- | -- |
|pxe | 设置下次启动为 网络pxe引导|
|disk | 设置下次启动为 本地磁盘引导|
|cdrom | 设置下次启动为 为光盘引导|


## 网络管理

### 查看带外网络

```python
ipmitool lan print
```

```
[root@localhost ~]# ipmitool lan print
Set in Progress         : Set Complete
Auth Type Support       : 
Auth Type Enable        : Callback : 
                        : User     : 
                        : Operator : 
                        : Admin    : 
                        : OEM      : 
IP Address Source       : DHCP Address
IP Address              : 172.31.79.92
Subnet Mask             : 255.255.255.0
MAC Address             : 50:65:f3:66:ab:cc
BMC ARP Control         : ARP Responses Enabled, Gratuitous ARP Disabled
Default Gateway IP      : 172.31.79.247
802.1q VLAN ID          : Disabled
802.1q VLAN Priority    : 0
Cipher Suite Priv Max   : Not Available
```

|lan print 输出解释|
|--|--|
|IP Address Source|DHCP Address|带外IP配置的方式DHCP|
|IP Address |172.31.79.92|带外IP地址|
|Default Gateway IP |172.31.79.247|带外网关|

### 设置带外网络
```
ipmitool lan set 1 ipsrc dhcp 
ipmitool lan print 1
ipmitool lan set 1 ipsrc static
ipmitool lan set 1 ipaddress 10.1.199.211 Setting LAN IP Address to 10.1.199.211
ipmitool lan set 1 netmask 255.255.255.0 Setting LAN Subnet Mask to 255.255.255.0
ipmitool lan set 1 defgw ipaddr 10.1.199.1 Setting LAN Default Gateway IP to 10.1.199.1
ipmitool lan print 1
```
```
使用静态地址：ipmitool lan set <channel_no> ipsrc static
使用动态地址：ipmitool lan set <channel_no> ipsrc dhcp
设置IP：ipmitool lan set <channel_no> ipaddr <x.x.x.x>
设置掩码：ipmitool lan set <channel_no> netmask <x.x.x.x>
设置网关：ipmitool lan set <channel_no> defgw ipaddr <x.x.x.x>
本地操作 -I open 表示接口本地：ipmitool -I open lan print 1
操作远程机器 -I lan 表示接口远程：ipmitool -I lan -H 10.1.199.12 -U ADMIN -P ADMIN lan print 1
```


查看磁盘状态?

```
ipmitool -I lanplus -H $host -U $username -P $pwd chassis status
```


服务器温度

```
ipmitool -H 192.168.12.84 -I lanplus -U test -P 123456 sdr type Temperature
```
```
[root@localhost ~]# ipmitool chassis status
System Power         : on
Power Overload       : false
Power Interlock      : inactive
Main Power Fault     : false
Power Control Fault  : false
Power Restore Policy : always-off
Last Power Event     : 
Chassis Intrusion    : inactive
Front-Panel Lockout  : inactive
Drive Fault          : false
Cooling/Fan Fault    : false
Front Panel Control  : none
```

## 重启芯片

```
/usr/bin/ipmitool -I lanplus -H $IP -U $Username -P $PASSWD bmc reset cold
```

{% include links.html %}
