---
title: Linux系统时间 
keywords: sample homepage
tags: [linux_time]
sidebar: note_sidebar
permalink: note_linux_time.html
summary: Linux系统的相关时间管理；时间、时区、时钟的相关信息的查看与配置；时间相关的软件与工具的了解与使用；
---

## 时间和时区
时间是一个瞬间的概念，体现在计算机中可以理解成**UNIX时间戳**，目前精确的时间源是参考原子钟的震荡频率，然后进行全球同步。常用ntp来进行时间的同步。

由于地球旋转导致不同地域的人看到的日出日落的时间不同，根据地球的地理位置，人为将地球划分成24个不同的**时区**。   

计算机中经常看到的是UTC时间标准(UTC: Coordinated Universal Time)，他是0时时区标准。中国时区(CST: Chinese Standard Time)相对于0时时区是**东八区**。   

例如某一时刻

*  Unix时间戳：   

```
[root@VM_11_7_centos ~]# date +%s    
1496217462   
```

* UTC时区时间:   

```
[root@VM_11_7_centos ~]# date -u   
Wed May 31 07:57:42 UTC 2017    
```

* CST时区时间:   

```
[root@VM_11_7_centos ~]# date      
Wed May 31 15:57:42 CST 2017      
```

## NTP服务管理
```shell
yum install ntp -y
service ntpd start
chkconfig ntpd on
```

## NTP配置文件：/etc/ntp.conf
配置文件路径：`/etc/ntp.conf`

配置格式：关键字（如server）    参数（如prefer） 

以换行为结束，所以一个配置不能占多行。  

ntp.conf包括两类配置命令集，一类叫配置命令（configuration commands）。另一类叫辅助命令（auxiliary commands ）。    

* **driftfile 文件路径**   

系统时间与BIOS事件的偏差记录，将自己主机的bios芯片震荡频率与上层的Time server频率比较，将误差记录在这个文件里   

```
driftfile /etc/ntp/drift   
```

* **restrict 控制相关权限**

语法为： restrict IP地址 mask 子网掩码 参数   
其中IP地址也可以是default ，default 就是指所有的IP   
参数有以下几个：   
    - **ignore**  ：关闭所有的 NTP 联机服务   
    - **nomodify** ：客户端不能更改服务端的时间参数，但是客户端可以通过服务端进行网络校时。   
    - **notrust** ：客户端除非通过认证，否则该客户端来源将被视为不信任子网   
    - **noquery** ：不提供客户端的时间查询，用户端不能使用ntpq，ntpc等命令来查询ntp服务器，也就是拒绝和ntp server进行时间同步      
    - **notrap** ：不提供trap远端登陆，拒绝为匹配的主机提供模式 6 控制消息陷阱服务。陷阱服务是 ntpdq 控制消息协议的子系统，用于远程事件日志记录程序。   
    - **nopeer** ：用于阻止主机尝试与服务器对等，并允许欺诈性服务器控制时钟   
    - **kod** ： 访问违规时发送 KoD 包。   
```
restrict -6 表示IPV6地址的权限设置。   
restrict default ignore #默认策略   
```

* **server 时间源服务器**   
语法为：server 时间源IP/域名 参数   
参数：   
    - prefer : 优先级，配置该参数优先作为时间源   
    - iburst :    

* **fudge 服务器层次**   
这行是时间服务器的层次。stratum 0 表示1级primary reference，为顶级；如果要向别的NTP服务器更新时间，请不要把它设为0   
```
server 127.127.1.0   
fudge 127.127.1.0 stratum 0  
```

* **includefile 允许包含其他的配置文件***   
includefile includefile     允许包含其他的配置文件。 



## 配置文件：/etc/ntp/stpe-tickers   
当ntpd服务启动时，会自动与该文件中记录的上层NTP服务进行时间校对    


## 配置文件： /etc/sysconfig/ntpd   

ntp服务默认只会同步系统时间。如果想要让ntp同时同步硬件时间，可以设置`/etc/sysconfig/ntpd`文件，在`/etc/sysconfig/ntpd`文件中，添加如下行，就可以让硬件时间与系统时间一起同步。   

```
SYNC_HWCLOCK=yes
```

允许BIOS与系统时间同步，也可以通过hwclock -w 命令   

## ntpq
ntpq 依据/etc/ntp.conf配置文件进行查询   

```
[root@localhost ~]#ntpq -np 127.0.0.1
     remote           refid      st t when poll reach   delay   offset  jitter
==============================================================================
*172.31.57.3     LOCAL(0)         4 u   19   32  377    0.123   -0.016   0.003
 172.31.57.4     172.31.57.3      5 u    1   32  377    0.121   -0.017   0.006
 127.127.1.0     .LOCL.           5 l    3   64  377    0.000    0.000   0.001
```

* remote   - ntp时间源。
* refid    - remote时间源的上一层时间源
* st       - stratum时间源阶层
* when     - 多少秒前曾经同步过时间,当达到poll时会进行一次同步，然后重新计时
* poll     - 时间更新周期，时间单位秒 
* reach    - 已经向上层ntp服务器要求更新的次数，是一个八进制数字，指出源的可存取性。值 377 表示源已应答了前八个连续轮询。
* delay    - 网络延迟
* offset   - 时间补偿,时间偏移
* jitter   - 系统时间与bios时间差

每一行前面标记:

\*  : 它告诉我们远端的服务器已经被确认为我们的主NTP Server,我们系统的时间将由这台机器所提供

\+  : 它将作为辅助的NTP Server和带有\*号的服务器一起为我们提供同步服务， 当\*号服务器不可用时它就可以接管

\- : 远程服务器被clustering algorithm认为是不合格的NTP Server

x  : 远程服务器不可用

\空格 : 远程服务器不可用


## ntpdate

ntpdate 进行时间的查询和时间同步

使用ntpdate同步时ntpd服务不能运行，否则会报错

指定时间源进行查询

```
ntpdate -q 0.centos.pool.ntp.org 
```

如果想定时进行时间校准，可以使用crond服务来定时执行。

```
30 8 * * * root /usr/sbin/ntpdate 0.centos.pool.ntp.org; /sbin/hwclock -w
```

ntpdate默认不能修改硬件时间，需要使用hwclock进行同步

## date

查看和设置系统时间

* 设置系统时间

```
date -s "2017-05-31 12:00:00"
```

* 当前unix时间戳

```
date +%s
```

* 转换指定日期为Unix时间戳

```
date -d '2013-2-22 22:14' +%s
```

* 将时间戳转换成系统时区时间

```
date -d @1361542596    
date -d @1361542596 +"%Y-%m-%d %H:%M:%S"
```

## ntpd、ntpdate作为客户端的区别

ntpd不仅仅是时间同步服务器，它还可以做客户端与标准时间服务器进行同步时间，而且是平滑同步   

ntpdate立即同步，在生产环境中慎用ntpdate，也正如此两者不可同时运行   

时钟的跃变，对于某些程序会导致很严重的问题。许多应用程序依赖连续的时钟。毕竟，这是一项常见的假定，即取得的时间是线性的，一些操作，例如数据库事务，通常会地依赖这样的事实：时间不会往回跳跃。不幸的是，ntpdate调整时间的方式就是我们所说的”跃变“：在获得一个时间之后，ntpdate使用settimeofday(2)设置系统时间，这有几个非常明显的问题：

* 第一，这样做不安全。ntpdate的设置依赖于ntp服务器的安全性，攻击者可以利用一些软件设计上的缺陷，拿下ntp服务器并令与其同步的服务器执行某些消耗性的任务。由于ntpdate采用的方式是跳变，跟随它的服务器无法知道是否发生了异常（时间不一样的时候，唯一的办法是以服务器为准）。

* 第二，这样做不精确。一旦ntp服务器宕机，跟随它的服务器也就会无法同步时间。与此不同，ntpd不仅能够校准计算机的时间，而且能够校准计算机的时钟。

* 第三，这样做不够优雅。由于是跳变，而不是使时间变快或变慢，依赖时序的程序会出错（例如，如果ntpdate发现你的时间快了，则可能会经历两个相同的时刻，对某些应用而言，这是致命的）。因而，唯一一个可以令时间发生跳变的点，是计算机刚刚启动，但还没有启动很多服务的那个时候。其余的时候，理想的做法是使用ntpd来校准时钟，而不是调整计算机时钟上的时间。

NTPD 在和时间服务器的同步过程中，会把 BIOS 计时器的振荡频率偏差——或者说 Local Clock 的自然漂移(drift)——记录下来。这样即使网络有问题，本机仍然能维持一个相当精确的走时。

## 硬件时间与系统时间

在计算机系统中有硬件时间(RTC: Real Time Clock)，和系统时间(System Clock)之分。

硬件时钟是指嵌在主板上的特殊的电路,相当于一个独立是时钟，维持该时间需要一个独立的电池，关机状态下也能记录时间。

系统时钟就是操作系统的kernel所用来计算时间的时钟。它从1970年1月1日00:00:00 UTC时间到目前为止秒数总和的值,在Linux下系统时间在开机的时候会和硬件时间同步(synchronization),之后也就各自独立运行了

* `hwclock` 就是系统时间和硬件时间同步的工具

查看硬件时间，一般系统运行一段时间后系统时间会和硬件时间有一定的误差

```
hwclock --show
```

* 硬件时间设置成系统时间

```
hwclock --hctosys
```

* 系统时间设置成硬件时间

```
hwclock --systohc
```

* 设置硬件时间和系统时间

设置硬件时间可以在BIOS中设置，也可以开机后使用命令设置

```
hwclock --set --date="mm/dd/yy hh:mm:ss"    
date -s "dd/mm/yyyy hh:mm:ss"
```

## 设置系统时区
在Linux下glibc提供了我们事先编译好的许多timezone文件, 他们就放在`/usr/share/zoneinfo`这个目录下,这里基本涵盖了大部分的国家和城市

Unix时间戳根据时区转换成不同时区的时间

查看对于每个time zone当前的时间我们可以用zdump命令

```
zdump Hongkong
```

配置系统时区

- 1.修改时区文件`/etc/localtime`,将`/usr/share/zoneinfo`中的文件复制为该文件，或者localtime文件链接到zoneinfo中的某个文件

- 2.修改TZ环境变量

```
tzselect
```

当TZ变量没有定义的时候系统才使用`/etc/localtime`来确定time zone. 所以你想永久修改time zone的话那么可以把TZ变量的设置写入`/etc/profile`里

## 其他问题
- 1、客户端的日期必须要设置正确，不能超出正常时间24小时，不然会因为安全原因被拒绝更新。其次客户端的时区必须要设置好，以确保不会更新成其它时区的时间。

- 2、fudge 127.127.1.0 stratum 10 如果是LINUX做为NTP服务器，stratum(层级)的值不能太大，如果要向上级NTP更新可以设成2

- 3、可以运行命令 ntpstat 查看每次更新间隔如：

```
[root@ESXI ~]# ntpstat
```
