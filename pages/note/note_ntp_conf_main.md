---
title: NTP配置文件 ntp.conf
keywords: sample homepage
tags: [linux_time]
sidebar: note_sidebar
permalink: note_ntp_conf_main.html
summary: NTP 程序的配置文件介绍 
---

配置文件路径：`/etc/ntp.conf`

配置格式：关键字(如server) 参数(如prefer)

以换行为结束，所以一个配置不能占多行。  

ntp.conf包括两类配置命令集，一类叫配置命令(configuration commands)。另一类叫辅助命令(auxiliary commands)   

## [配置文件命令](http://doc.ntp.org/4.2.6/confopt.html)

|参数|描述|
|:---:|---|
|autokey|end and receive packets authenticated by the Autokey scheme described in the Authentication Options page. This option is mutually exclusive with the key option|
|burst|When the server is reachable, send a burst of eight packets instead of the usual one. The packet spacing is normally 2 s; however, the spacing between the first and second packets can be changed with the calldelay command to allow additional time for a modem or ISDN call to complete. This option is valid only with the server command and type s addressesa. It is a reco    mmended option when the maxpoll option is greater than 10 (1024 s)|
|iburst|当ntp server不可达时，发送发个8数据包，而不是通常的1个。包之间的发送间隔是2秒；然而, the spacing between the first and second packets canbe changed with the calldelay command to allow additional time for a modem or ISDN call to complete. This option is valid only with the server command and type s addresses.这个命令是推荐的操作.|
|key *key*|Send and receive packets authenticated by the symmetric key scheme described in the Authentication Options page. The key specifies the key identifier with values from 1 to 65534, inclusive. This option is mutually exclusive with the autokey option.|
|minpoll *minpoll*|-|
|axpoll *maxpoll*| 指定最大和最小的时间同步轮训(poll intervals)间隔，这两个参数一般同时存在。最大值默认是10(转换成秒就是2的10次方，1024秒)，可以修改该值上线是17(即36小时)。最小值默认是6(即64秒)，可修改的下限是3(即8秒)|
|mode *option*|Pass the option to a reference clock driver, where option is an integer in the range from 0 to 255, inclusive. This option is valid only with type r addresses|
|noselect|Marks the server or peer to be ignored by the selection algorithm but visible to the monitoring program. This option is ignored with the broadcast command.|
|preempt|Specifies the association as preemptable rather than the default persistent. This option is ignored with the broadcast command and is most useful with the manycastclient and pool commands|
|prefer|标记这个服务为首选的。 All other things being equal, this host will be chosen for synchronization among a set of correctly operating hosts. See the Mitigation Rules and the prefer Keyword page for further information. This option is valid only with the server and peer commands|
|true|Mark the association to assume truechimer status; that is, always survive the selection and clustering algorithms. This option can be used with any association, but is most useful for reference clocks with large jitter on the serial port and precision pulse-per-second (PPS) signals. Caution: this option defeats the algorithms designed to cast out falsetickers and can    allow these sources to set the system clock. This option is valid only with the server and peer commands.|
|ttl *ttl*|This option specifies the time-to-live ttl for the broadcast command and the maximum ttl for the expanding ring search used by the manycastclient command. Selection of the proper value,     which defaults to 127, is something of a black art and should be coordinated with the network administrator. This option is invalid with type r addresses.|
|version *version*|Specifies the version number to be used f or outgoing NTP packets. Versions 1-4 are the choices, with version 4 the default|
|xleave|Operate in interleaved mode (symmetric and broadcast modes only). (see NTP Interleaved Modes)|

## driftfile 偏差文件路径

系统时间与BIOS时间的偏差记录; 将自己主机的bios芯片震荡频率与上层的Time server频率比较，将误差记录在这个文件里   

```
driftfile /etc/ntp/drift 
```

## restrict 控制相关权限

```
restrict address [mask mask] [flag][...]
```

address地址参数可以是IP地址或者能够解析的域名。mask是子网掩码。默认的是(address 0.0.0.0,mask 0.0.0.) Note that the text string default, with no mask option, may be used to indicate the default entry.

Some flags have the effect to deny service, some have the effect to enable service and some are conditioned by other flags. The flags. are not orthogonal, in that more restrictive flags will often make less restrictive ones redundant. The flags that deny service are classed in two categories, those that restrict time service and those that restrict informational queries and attempts to do run-time reconfiguration of the server. One or more of the following flags may be specified:

flake
Discard received NTP packets with probability 0.1; that is, on average drop one packet in ten. This is for testing and amusement. The name comes from Bob Braden's flakeway, which once did a similar thing for early Internet testing.

| 参数     | 　　　　 功能  |
| :----:   | :---- |
| ignore   |拒绝所有种类的请求。包括ntpq和ntpdc请求|
| kod      |访问违规时发送 KoD 包。Send a kiss-o'-death (KoD) packet if the limited flag is present and a packet violates the rate limits established by the discard command. KoD packets are themselves rate limited for ea    ch source address separately. If this flag is not present, packets that violate the rate limits are discarded.|
|limited|Deny time service if the packet violates the rate limits established by the discard command. This does not apply to ntpq and ntpdc queries|
|lowpriotrap|Declare traps set by matching hosts to be low priority. The number of traps a server can maintain is limited (the current limit is 3). Traps are usually assigned on a first come, first    served basis, with later trap requestors being denied service. This flag modifies the assignment algorithm by allowing low priority traps to be overridden by later requests for normal p    riority traps.|
|mssntp|Enable Microsoft Windows MS-SNTP authentication using Active Directory services. Note: Potential users should be aware that these services involve a TCP connection to another process th    at could potentially block, denying services to other users. Therefore, this flag should be used only for a dedicated server with no clients other than MS-SNTP|
| nomodify |客户端不能更改服务端的时间参数，但是客户端可以通过服务端进行网络校时。  Deny ntpq and ntpdc queries which attempt to modify the state of the server (i.e., run time reconfiguration). Queries which return information are permitted| 
| noquery  |不提供客户端的时间查询，用户端不能使用ntpq，ntpc等命令来查询ntp服务器，也就是拒绝和ntp server进行时间同步,Deny ntpq and ntpdc queries. Time service is not affected.|
| nopeer   |用于阻止主机尝试与服务器对等，并允许欺诈性服务器控制时钟,Deny packets that might mobilize an association unless authenticated. This includes broadcast, symmetric-active and manycast server packets when a configured association does not exist.     Note that this flag does not apply to packets that do not attempt to mobilize an association.|
|noserve|Deny all packets except ntpq and ntpdc queries.|
| notrap   |不提供trap远端登陆，拒绝为匹配的主机提供模式 6 控制消息陷阱服务。陷阱服务是 ntpdq 控制消息协议的子系统，用于远程事件日志记录程序。   Decline to provide mode 6 control message trap service to matching hosts. The trap service is a subsystem of the ntpdc control message protocol which is intended for use by remote event     logging programs.|
| notrust  |客户端除非通过认证，否则该客户端来源将被视为不信任子 ,Deny packets that are not cryptographically authenticated. Note carefully how this flag interacts with the auth option of the enable and disable commands. If auth is enabled, which is t    he default, authentication is required for all packets that might mobilize an association. If auth is disabled, but the notrust flag is not present, an association can be mobilized whet    her or not authenticated. If auth is disabled, but the notrust flag is present, authentication is required only for the specified address/mask range.|
|ntpport|-|   
|non-ntpport|This is actually a match algorithm modifier, rather than a restriction flag. Its presence causes the restriction entry to be matched only if the source port in the packet is the standar    d NTP UDP port (123). Both ntpport and non-ntpport may be specified. The ntpport is considered more specific and is sorted later in the list|   
|version|Deny packets that do not match the current NTP version.|   

Default restriction list entries with the flags ignore, ntpport, for each of the local host's interface addresses are inserted into the table at startup to prevent the server from attempting to synchronize to its own time. A default entry is also always present, though if it is otherwise unconfigured; no flags are associated with the default entry (i.e., everything besides your own NTP server is unrestricted).


语法为： restrict IP地址 mask 子网掩码 参数   

其中IP地址也可以是default ，default 就是指所有的IP   

参数有以下几个：   

```
restrict    default nomodify notrap nopeer noquery
restrict -6 default nomodify notrap nopeer noquery
或者
restrict    default ignore
restrict -6 default ignore
```

默认权限配置是先禁止所有的权限，然后再开放指定的权限

```
restrict 127.0.0.1 
restrict ::1
```

一般会开放本地环回接口所有权限，例如可以通过本地时间作为时间源

## [server 时间源服务器](http://doc.ntp.org/4.2.6/clockopt.html#server)

For type s and r addresses (only), this command mobilizes a persistent client mode association with the specified remote server or local reference clock. If the preempt flag is specified, a preemptable client mode association is mobilized instead.

语法为：server 时间源IP/域名 参数   

server 127.127.t.u [prefer] [mode int] [minpoll int] [maxpoll int]
This command can be used to configure reference clocks in special ways. The options are interpreted as follows:

|参数|描述|
|:---:|---|
|prefer|Marks the reference clock as preferred. All other things being equal, this host will be chosen for synchronization among a set of correctly operating hosts. See the Mitigation Rules and     the prefer Keyword page for further information.|
|mode int|Specifies a mode number which is interpreted in a device-specific fashion. For instance, it selects a dialing protocol in the ACTS driver and a device subtype in the parse drivers|
|minpoll int|-|
|axpoll *maxpoll*| 指定最大和最小的时间同步轮训(poll intervals)间隔，这两个参数一般同时存在。最大值默认是10(转换成秒就是2的10次方，1024秒)，可以修改该值上线是17(即36小时)。最小值默认是6(即64秒)，可修改的下限是3(即8秒)|


## [fudge 服务器层次](http://doc.ntp.org/4.2.6/clockopt.html#server)

这行是时间服务器的层次。stratum 0 表示1级primary reference，为顶级；如果要向别的NTP服务器更新时间，请不要把它设为0   

```
server 127.127.1.0   
fudge 127.127.1.0 stratum 0  
```
fudge 127.127.t.u [time1 sec] [time2 sec] [stratum int] [refid string] [flag1 0|1] [flag2 0|1] [flag3 0|1] [flag4 0|1]
This command can be used to configure reference clocks in special ways. It must immediately follow the server command which configures the driver. Note that the same capability is possible at run time using the ntpdc program. The options are interpreted as follows:
time1 sec
Specifies a constant to be added to the time offset produced by the driver, a fixed-point decimal number in seconds. This is used as a calibration constant to adjust the nominal time offset of a particular clock to agree with an external standard, such as a precision PPS signal. It also provides a way to correct a systematic error or bias due to serial port or operating system latencies, different cable lengths or receiver internal delay. The specified offset is in addition to the propagation delay provided by other means, such as internal DIPswitches. Where a calibration for an individual system and driver is available, an approximate correction is noted in the driver documentation pages.
Note: in order to facilitate calibration when more than one radio clock or PPS signal is supported, a special calibration feature is available. It takes the form of an argument to the enable command described in the Miscellaneous Options page and operates as described in the Reference Clock Drivers page.
time2 secs
Specifies a fixed-point decimal number in seconds, which is interpreted in a driver-dependent way. See the descriptions of specific drivers in the reference clock drivers page.
stratum int
Specifies the stratum number assigned to the driver, an integer between 0 and 15. This number overrides the default stratum number ordinarily assigned by the driver itself, usually zero.
refid string
Specifies an ASCII string of from one to four characters which defines the reference identifier used by the driver. This string overrides the default identifier ordinarily assigned by the driver itself.
flag1 flag2 flag3 flag4
These four flags are used for customizing the clock driver. The interpretation of these values, and whether they are used at all, is a function of the particular clock driver. However, by convention flag4 is used to enable recording monitoring data to the clockstats file configured with the filegen command. Further information on the filegen command can be found in the Monitoring Options page.



## [tinker](http://doc.ntp.org/4.2.6/miscopt.html#tinker) 

```
tinker [ allan allan | dispersion dispersion | freq freq | huffpuff huffpuff | panic panic | step step | stepout stepout ]
```

该命令改变当前系统给定的钟驯化算法(the clock discipline algorithm)，该默认值已经优化过了。很少需要改变该默认值；但是有些人非要改变该值得话，每个值得解释如下:

|参数|描述|
|:--:|--|
|allan *allan*|Spedifies the Allan intercept, which is a parameter of the PLL/FLL clock discipline algorithm, in seconds with default 1500 s|
|dispersion *dispersion*|Specifies the dispersion increase rate in parts-per-million (PPM) with default 15 PPM|
|freq *freq*|Spedifies the frequency offset in parts-per-million (PPM) with default the value in the frequency file|
|huffpuff *huffpuff*|Spedifies the huff-n'-puff filter span, which determines the most recent interval the algorithm will search for a minimum delay. The lower limit is 900 s (15 m), but a more reasonable value is 7200 (2 hours)|
|panic *panic*| 指定一个时间偏移跃变的阈值，默认是1000秒。如果设置为0，改功能将会关闭，任意一个时钟偏移同步都将会被接受。就是说默认情况下如果时间偏移超过1000秒，将会判断为异常时间，不会进行同步，但是如果设置成0就会禁用这一个功能，当ntp server时间异常波动大于1000秒时，会导致本地的时间发生突变，这可能会导致某些应用异常。 | 
|step *step*| 指定时间同步步长，单位是秒，默认是0.128秒。如果设置为0，该进步式时间调整功能将会关闭。注意：如果改值设置为0或者大于0.5秒时，操作系统内核的时间discipline也会被禁用。|
|stepout *stepout*|Specifies the stepout threshold in seconds. The default without this command is 900 s. If set to zero, popcorn spikes will not be suppressed|


## [peer 时间互相同步]()

仅对于NTP服务器有效，这个命令指定了多台NTP服务器之间时间同步模式

```
peer 172.31.1.1 iburst minpoll 4 maxpoll 6  perfer   
peer 172.31.1.2 iburst minpoll 4 maxpoll 6
```

## includefile 允许包含其他的配置文件

includefile includefile     允许包含其他的配置文件。 


## Links

[http://doc.ntp.org/4.2.6/comdex.html](http://doc.ntp.org/4.2.6/comdex.html)

[http://doc.ntp.org/4.2.6/miscopt.html](http://doc.ntp.org/4.2.6/miscopt.html)
