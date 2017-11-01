---
title: MegaCli工具使用 
keywords: 
last_updated: June 13, 2017
tags: [getting_started]
summary: MegaCli/MegaCli32/MegaCli64 
sidebar: note_sidebar
permalink: note_raid_megacli.html
folder: note 
---

MegaCli是一款管理维护硬件RAID软件，可以通过它来了解当前raid卡的所有信息。最新版是storcli。适合LSI公司的Raid卡。



## MegaCli下载安装

http://tenderrain.blog.51cto.com/9202912/1639865/



## 判断系统Raid卡类型

```
[root@localhost ~]# lspci |grep -i "raid"
05:00.0 RAID bus controller: LSI Logic / Symbios Logic MegaRAID SAS 1078 (rev 04)
```

## Apapter Raid 卡控制器管理

```
[root@localhost /]# MegaCli64 -adpAllinfo -aALL
```



## 逻辑盘管理

### 查看逻辑盘状态信息

```
MegaCli64 -Ldinfo -Lall -Aall -NoLog
```

* -NoLog 不保存日志，没有该选项每次执行命令会在当前目录下生成一个日志文件。例如SAS盘`MegaSAS.log`

```
Adapter 0 -- Virtual Drive Information:
Virtual Drive: 0 (Target Id: 0)
Name                :
RAID Level          : Primary-5, Secondary-0, RAID Level Qualifier-3
Size                : 2.618 TB
Parity Size         : 893.75 GB
State               : Optimal
Strip Size          : 256 KB
Number Of Drives    : 4
Span Depth          : 1
Default Cache Policy: WriteBack, ReadAheadNone, Direct, Write Cache OK if Bad BBU
Current Cache Policy: WriteBack, ReadAheadNone, Direct, Write Cache OK if Bad BBU
Default Access Policy: Read/Write
Current Access Policy: Read/Write
Disk Cache Policy   : Enabled
Encryption Type     : None
PI type: No PI
```

逻辑盘是物理磁盘通过Raid虚拟出来的磁盘，对应系统中的/dev/sda、/dev/sdb等

* State : 显示当前的逻辑盘的状态

* Disk Cache Policy : 该逻辑盘是否启动了Cache缓存，在Default Cache Policy和Current Cache Policy行可以看到信息


### 查看Raid Cache缓存策略

```
MegaCli64 -LDGetProp -Cache -LALL -aALL
MegaCli64 -LDGetProp -DskCache -LALL -aALL
```

* -L : 指定逻辑盘。[-L0/-L1/-LALL]

* -a : 指定控制器Adapter，即Raid卡 [-a0/-a1/-all]

### 设置缓存策略

```
MegaCli64 -LDSetProp WB -L0 -a0
```

### 设置即使电池坏了还是保持WB功能

```
MegaCli -LDSetProp CachedBadBBU -L0 -a0
```





## BBU 电池管理

### `MegaCli -h`帮助信息

```
MegaCli -AdpBbuCmd -aN|-a0,1,2|-aALL  
MegaCli -AdpBbuCmd -GetBbuStatus -aN|-a0,1,2|-aALL  
MegaCli -AdpBbuCmd -GetBbuCapacityInfo -aN|-a0,1,2|-aALL  
MegaCli -AdpBbuCmd -GetBbuDesignInfo -aN|-a0,1,2|-aALL  
MegaCli -AdpBbuCmd -GetBbuProperties -aN|-a0,1,2|-aALL  
MegaCli -AdpBbuCmd -BbuLearn -aN|-a0,1,2|-aALL  
MegaCli -AdpBbuCmd -BbuMfgSleep -aN|-a0,1,2|-aALL  
MegaCli -AdpBbuCmd -BbuMfgSeal -aN|-a0,1,2|-aALL  
MegaCli -AdpBbuCmd -SetBbuProperties -f <fileName> -aN|-a0,1,2|-aALL 
MegaCli -AdpBbuCmd -GetGGEEPData offset [Hexaddress] NumBytes n -aN|-a0,1,2|-aALL 
```

### 查看BBU全局信息
```
MegaCli -AdpBbuCmd -aALL  
```

### 查看BBU状态信息

```
MegaCli64 -AdpBbuCmd -GetBbuStatus -aall
```

```
BBU status for Adapter: 0

BatteryType: CVPM02
Voltage: 10952 mV
Current: 110 mA
Temperature: 20 C

BBU Firmware Status:

  Charging Status              : None
  Voltage                                 : OK
  Temperature                             : OK
  Learn Cycle Requested	                  : Yes
  Learn Cycle Active                      : Yes
  Learn Cycle Status                      : OK
  Learn Cycle Timeout                     : No
  I2c Errors Detected                     : No
  Battery Pack Missing                    : No
  Battery Replacement required            : No
  Remaining Capacity Low                  : No
  Periodic Learn Required                 : No
  Transparent Learn                       : Yes
  No space to cache offload               : No
  Pack is about to fail & should be replaced : No
  Cache Offload premium feature required  : No
  Module microcode update required        : No

GasGuageStatus:
  Fully Discharged        : Yes
  Fully Charged           : No
  Discharging             : No
  Initialized             : Yes
  Remaining Time Alarm    : No
  Remaining Capacity Alarm: No
  Discharge Terminated    : No
  Over Temperature        : No
  Charging Terminated     : Yes
  Over Charged            : No

  Pack energy             : 157 J 
  Capacitance             : 100 
  Remaining reserve space : 96 


Exit Code: 0x00
```

在BBU状态信息中，主要关注的内容是

### BBU配置信息

```
MegaCli64  -AdpBbuCmd -GetBbuProperties -Aall
```

```
BBU Properties for Adapter: 0

Auto Learn Period: 2419200 Sec
Next Learn time: 553184124 Sec 
Learn Delay Interval:0 Hours
Auto-Learn Mode: Enabled
```

* Auto Learn Period : 电池充放电周期

* Auto-Learn Mode : 电池充放电配置

### 查看电磁电池电量

当前电量，当电量低于15%，或者电池坏掉时，默认都会将写策略从WB改成WT，除非设定为FORCE WB策略

### 电池是否有错误信息

### 电池充放电时间

注意这是美国时间。另外，新的阵列卡电池很多改成电容式的了，也就不需要重复充放电了











			
## 物理磁盘管理

### 查看所有硬盘的详细信息

该命令显示所有物理磁盘的详细信息，按照Solt Number物理插槽位显示。
可以对输出的信息进行grep的过滤处理获取想要的信息。

```
MegaCli64 -PDList -aALL
```

```
PD: 7 Information
Enclosure Device ID: 8
Slot Number: 11
Drive's postion: DiskGroup: 1, Span: 0, Arm: 7
Enclosure position: 0
Device Id: 20
WWN: 
Sequence Number: 2
Media Error Count: 0
Other Error Count: 0
Predictive Failure Count: 0
Last Predictive Failure Event Seq Number: 0
PD Type: SATA
Raw Size: 894.252 GB [0x6fc81ab0 Sectors]
Non Coerced Size: 893.752 GB [0x6fb81ab0 Sectors]
Coerced Size: 893.75 GB [0x6fb80000 Sectors]
Firmware state: Online, Spun Up
Is Commissioned Spare : NO
Device Firmware Level: C03Q
Shield Counter: 0
Successful diagnostics completion on :  N/A
SAS Address(0): 0x500605b000027277
Connected Port Number: 0(path0) 
Inquiry Data: S1E4NYAG318441      SAMSUNG MZ7WD960HMHP-00003              DXV8C03Q
FDE Enable: Disable
Secured: Unsecured
Locked: Unlocked
Needs EKM Attention: No
Foreign State: None 
Device Speed: 6.0Gb/s 
Link Speed: 6.0Gb/s 
Media Type: Solid State Device
Drive Temperature : N/A
PI Eligibility:  No 
Drive is formatted for PI information:  No
PI: No PI
Drive's write cache : Enabled
Drive's NCQ setting : Disabled
Port-0 :
Port status: Active
Port's Linkspeed: 6.0Gb/s 
Drive has flagged a S.M.A.R.T alert : No
```

对于每块物理磁盘的描述信息，主要关注一下几项：

* Slot Number : 表示磁盘的插槽位置，可以根据Slot Number序列值推断是否有磁盘离线

* Medai Error Count : 表示磁盘可能错误，可能是磁盘有坏道，这个值不为0值得注意，数值越大，危险系数越高

* Other Error Count : 表示磁盘可能存在松动，可能需要重新再插入

* Predictive Failure Count : ( 预测性失败统计)

* Firmware state : 表示磁盘的状态，可以判断磁盘是否损坏。正常状态是`Online, Spun Up`

* Media Type : 磁盘类型，SSD/HDD等

* PD Type : 磁盘接口类型, SATA/SAS


### 查看rebuild进度

硬盘更换后会进行rebuild，rebuild时Cache的缓存策略是WT


```
MegaCli64 -PDRbld -ShowProg -physdrv[20:2] -aALL
```











| 各种设备和磁盘的不同状态：
| --             | -- |
| Device         |Normal/Damage/Rebuild/Normal                 |
| Virtual Drive  |Optimal/Degraded/Degraded/Optimal            |
| Physical Drive |Online/Failed –> Unconfigured/Rebuild/Online |




{% include links.html %}
