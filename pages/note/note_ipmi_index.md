---
title: IPMI介绍
keywords: impi 
last_updated: June 15, 2017
tags: [getting_started]
summary: aa 
sidebar: note_sidebar
permalink: note_ipmi_index.html
folder: note 
---

管理带外

http://www.chenshake.com/summary-of-ipmi/


IPMI访问
国产服务器的IPMI访问的用户和密码，基本就是这些。这个和主板有关。我见过的两种主板的IPMI就是超微和泰安的。他们间功能上有点区别，默认的密码也是不一样。

联想：用户名：albert  pass:admin

超微：用户名：ADMIN  pass：ADMIN

泰安的主板：user:root  pass:superuser

浪潮服务器：user:root  pass:superuser

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
