---
title: ipmitool使用
keywords: impi 
last_updated: June 15, 2017
tags: [ipmi,ipmitool]
summary: ipmi 
sidebar: note_sidebar
permalink: note_ipmi_usage.html
folder: note 
---

ipmitool这个程序能够使你通过一个kernel设备驱动或者一个远程系统，利用IPMI v1.5或IPMIv2.0来管理本地系统的任何一个智能平台管理接口（IPMI)功能。
这些功能包括打印FRU（现场可替换装置）信息、LAN配置、传感器读数、以及远程机架电源控制。 
一个本地系统接口的IPMI管理功能需要一个兼容IPMI的kernel驱动程序被安装以及配置。在linux中，这个驱动叫做OpenIPMI，他被包括在了标准化分配中。在Solaris系统中，这个驱动叫做BMC，他被包括在了Solaris 10中。远程控制的管理需要授权以及配置IPMI-over-LAN接口。根据每个系统独特的需要，它可以通过系统接口来使LAN接口使用 ipmitool。

## 获取帮助信息
```
#ipmitool chassis help
Chassis Commands:  status, power, identify, policy, restart_cause, poh, bootdev, bootparam, selftest
```

## 带外接口

访问带外时需要指定访问接口类型，默认是本地openIPMI接口。
常用的主要有open/lan/lanplus这三种

|接口种类|
|--|--|
|open             |Linux OpenIPMI 接口 [默认的接口]|
|imb              |Intel IMB 接口|
|lan              |IPMI v1.5 LAN 接口,最大密码长度为16个字符。超过16字符的密码部分将被去掉|
|lanplus          |IPMI v2.0 RMCP+ LAN 接口,最大密码长度为20个字符;较长的密码将被截断|
|serial-terminal  |串行接口, 终端模式|
|serial-basic     |串行接口, 基础模式|
|usb              |IPMI USB 接口(OEM 接口 for AMI 设备) |


## 传感器信息(sensor)

### 获取传感器所有数据
```
Ipmitool sensor list
```
获取传感器中的各种监测值和该值的监测阈值，包括（CPU温度，电压，风扇转速，电源调制模块温度，电源电压等信息）

### 获取传感器指定值
```
Ipmitool sensor get "CPU0Temp"
```
获取ID为CPU0Temp监测值，CPU0Temp是sensor的ID，服务器不同，ID表示也不同

### 传感器阀值
```
Ipmitool –I open sensor thresh 
```
设置ID值等于id的监测项的各种限制值


## 系统事件日志管理 (sel)

### 系统事件日志列表
```
ipmitool sel list
ipmitool sel elist
```

### 清除系统事件日志
```
ipmitool sel clear
```
如果系统事件日志量较大，会导致带外存储不足，在获取信息时会卡住。如果确认日志不需要可以清除系统日志

## 电源管理

```
ipmitool power reset/on/off/status
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

## 用户管理

## 远程登录
```
ipmitool -I lanplus -H $host -U $username -P $pwd chassis status
```
远程登录带外并执行命令


## 磁盘管理 

查看底盘状态，其中包括了底盘电源信息，底盘工作状态等
```
Ipmitool chassis [options]
```
|参数|描述|
|--|--|
|status| 查看底盘状态，其中包括了底盘电源信息，底盘工作状态等|
|restart_cause|查看上次系统重启的原因|
|policy list|查看支持的底盘电源相关策略|


### 设置下次开机引导方式
```
ipmitool chassis bootdev pxe/disk/cdrom
```

| bootdev 引导方式设置 |
| -- | -- |
|pxe | 设置下次启动为 网络pxe引导|
|disk | 设置下次启动为 本地磁盘引导|
|cdrom | 设置下次启动为 为光盘引导|


## MC芯片管理

### 查看BMC硬件信息
```
ipmitool mc info 
```

### 重启芯片
```
/usr/bin/ipmitool bmc reset cold
```

### BMC选项
####  列出BMC所有允许的选项
```
Ipmitool  mc getenables 
```
列出BMC所有允许的选项

#### 设置BMC选项
```
Ipmitool  mc setenables =[on|off] 
```
设置bmc相应的允许/禁止选项




## 带外网络管理

### 查看带外网络

```python
ipmitool lan print
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

## ipmitool帮助信息

```
#ipmitool  -h   
ipmitool version 1.8.11

usage: ipmitool [options...] <command>

       -h             This help
       -V             Show version information
       -v             Verbose (can use multiple times)
       -c             Display output in comma separated format
       -d N           Specify a /dev/ipmiN device to use (default=0)
       -I intf        Interface to use
       -H hostname    Remote host name for LAN interface
       -p port        Remote RMCP port [default=623]
       -U username    Remote session username
       -f file        Read remote session password from file
       -S sdr         Use local file for remote SDR cache
       -a             Prompt for remote password
       -Y             Prompt for the Kg key for IPMIv2 authentication
       -e char        Set SOL escape character
       -C ciphersuite Cipher suite to be used by lanplus interface
       -k key         Use Kg key for IPMIv2 authentication
       -y hex_key     Use hexadecimal-encoded Kg key for IPMIv2 authentication
       -L level       Remote session privilege level [default=ADMINISTRATOR]
                      Append a '+' to use name/privilege lookup in RAKP1
       -A authtype    Force use of auth type NONE, PASSWORD, MD2, MD5 or OEM
       -P password    Remote session password
       -E             Read password from IPMI_PASSWORD environment variable
       -K             Read kgkey from IPMI_KGKEY environment variable
       -m address     Set local IPMB address
       -b channel     Set destination channel for bridged request
       -t address     Bridge request to remote target address
       -B channel     Set transit channel for bridged request (dual bridge)
       -T address     Set transit address for bridge request (dual bridge)
       -l lun         Set destination lun for raw commands
       -o oemtype     Setup for OEM (use 'list' to see available OEM types)
       -O seloem      Use file for OEM SEL event descriptions

Interfaces:
	open          Linux OpenIPMI Interface [default]
	imb           Intel IMB Interface 
	lan           IPMI v1.5 LAN Interface 
	lanplus       IPMI v2.0 RMCP+ LAN Interface 

Commands:
	raw           Send a RAW IPMI request and print response
	raw           发送一个原始的IPMI请求，并且打印回复信息 
	i2c           Send an I2C Master Write-Read command and print response
	spd           Print SPD info from remote I2C device
	lan           Configure LAN Channels
	lan           配置网络（lan）信道(channel) 
	chassis       Get chassis status and set power state
	chassis       查看磁盘的状态和设置电源 
	power         Shortcut to chassis power commands
	event         Send pre-defined events to MC
	event         向BMC发送一个已经定义的事件（event），可用于测试配置的SNMP是否成功 
	mc            Management Controller status and global enables
	mc            查看MC（Management Contollor）状态和各种允许的项 
	sdr           Print Sensor Data Repository entries and readings
	sdr           打印传感器仓库中的所有监控项和从传感器读取到的值
	sensor        Print detailed sensor information
	sensor        打印详细的传感器信息 
	fru           Print built-in FRU and scan SDR for FRU locators
	fru           输出内嵌的FRU（现场可替换装置）和扫描FRU 定位器的SDR（系统定义记录） 
	gendev        Read/Write Device associated with Generic Device locators sdr
	sel           Print System Event Log (SEL)
	sel           打印 System Event Log (SEL) 
	pef           Configure Platform Event Filtering (PEF)
	pef           设置PEF，事件过滤平台用于在监控系统发现有event时候，用PEF中的策略进行事件过滤，然后看是否需要报警 
	sol           Configure and connect IPMIv2.0 Serial-over-LAN
	sol           用于配置通过串口的Lan进行监控,配置IPMIv2.0 Serial-over-LAN 
	tsol          Configure and connect with Tyan IPMIv1.5 Serial-over-LAN
	isol          Configure IPMIv1.5 Serial-over-LAN
	isol          用于配置通过串口的Lan进行监控 ,配置IPMIv1.5 Serial-over-LAN
	user          Configure Management Controller users
	user          设置BMC中用户的信息 
	channel       Configure Management Controller channels
	channel       配置管理控制器通道
	session       Print session information
	session       打印session信息 
	sunoem        OEM Commands for Sun servers
	kontronoem    OEM Commands for Kontron devices
	picmg         Run a PICMG/ATCA extended cmd
	fwum          Update IPMC using Kontron OEM Firmware Update Manager
	firewall      Configure Firmware Firewall
	delloem       OEM Commands for Dell systems
	shell         Launch interactive IPMI shell
	exec          Run list of commands from file
	exec          从文件中运行一系列的命令 
	set           Set runtime variable for shell and exec
	set           为shell和exec设置运行变量 
	hpm           Update HPM components using PICMG HPM.1 file
	ekanalyzer    run FRU-Ekeying analyzer using FRU files
```


{% include links.html %}
