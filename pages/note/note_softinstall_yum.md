---
title: YUM 
keywords: yum 
last_updated: June 26, 2017
tags: [getting_started]
summary: yum是一款rpm软件管理工具
sidebar: note_sidebar
permalink: note_softinstall_yum.html
folder: note 
---

前言：以下内容以CentOS平台为例

## yum介绍

YUM是RPM族(CentOS/Redhat/Fedora/SuSE...)Linux系统软件包的管理工具。该工具以rpm软件包的包头(header)写入的依赖信息为依据，分析软件之间依赖关系，在安装软件时如果有依赖软件能够自动安装。

yum在得到正确的参数后，会首先从`/etc/yum.repo.d/*.repo`路径下的repo文件中取得软件仓库的地址并下载"元数据"(metadata)，metadata含注册于该软件仓库内所有软件包的包名及其所需的依赖环境等信息，yum得到这些信息后会和本地已有环境做对比，进而列出确认需要安装哪些包，并在用户确认后开始安装。

metadata由位于yum源服务器相关路径的repodata目录下的repomd.xml做索引。获取的metadata文件默认会保存在`/var/cache/yum/`目录中。

由yum下载的rpm包的存放位置，以及这些包是否会被系统自动清理，可通过修改yum配置文件（默认路径为/etc/yum.conf）中`cachedir`和`keepcache`两个属性来指定。cachedir后可用`=`连接目标路径，而keepcache值为0时，不长期保留下载的rpm包，值为1时则会保留。

## yum.conf配置

```
[main]
cachedir=/var/cache/yum/$basearch/$releasever
keepcache=0
debuglevel=2
logfile=/var/log/yum.log
exactarch=1
obsoletes=1
gpgcheck=1
plugins=1
installonly_limit=5
bugtracker_url=http://bugs.centos.org/set_project.php?project_id=23&ref=http://bugs.centos.org/bug_report_page.php?category=yum
distroverpkg=centos-release
```

```
cachedir=/var/cache/yum/$basearch/$releasever
```

yum缓存的目录，yum在此存储下载的rpm包和数据库，一般是/var/cache/yum

```
keepcache=0
```

是否保留缓存，及已经安装过的软件。0/不保留，1/保留。

```
debuglevel=2
```

除错级别，0──10,默认是2

```
logfile=/var/log/yum.log
```
yum的日志文件，默认是/var/log/yum.log

```
pkgpolicy
```

包的策略。一共有两个选项，newest和last，这个作用是如果你设置了多个repository，而同一软件在不同的repository中同时存在，yum应该安装哪一个，如果是newest，则yum会安装最新的那个版本。如果是last，则yum会将服务器id以字母表排序，并选择最后的那个服务器上的软件安装。一般都是选newest。

```
distroverpkg
```

指定一个软件包，yum会根据这个包判断你的发行版本，默认是redhat-release，也可以是安装的任何针对自己发行版的rpm包。

```
exactarch
```
有两个选项1和0,代表是否只升级和你安装软件包cpu体系一致的包，如果设为1，则如你安装了一个i386的rpm，则yum不会用1686的包来升级

```
retries
```
网络连接发生错误后的重试次数，如果设为0，则会无限重试

```
tolerent
```
也有1和0两个选项，表示yum是否容忍命令行发生与软件包有关的错误，比如你要安装1,2,3三个包，而其中3此前已经安装了，如果你设为1,则yum不会出现错误信息。默认是0。

```
exclude=
```
排除某些软件在升级名单之外，可以用通配符，列表中各个项目要用空格隔开，这个对于安装了诸如美化包，中文补丁的朋友特别有用

```
gpgchkeck=
```
有1和0两个选择，分别代表是否是否进行gpg校验，如果没有这一项，默认好像也是检查的


## yum客户端repo配置使用

yum客户端的配置主要是配置repo文件。当repo配置好了之后，用户可以使用配置文件中的yum源来安装一个软件或一组软件。

### yum客户端配置文件

repo文件是yum源（软件仓库）的配置文件，通常一个repo文件定义了一个或者多个软件仓库的细节内容，例如我们将从哪里下载需要安装或者升级的软件包，repo文件中的设置内容将被yum读取和应用。

通常默认的repo文件会保存在`/etc/yum.repo.d/`目录中，以`.repo`为后缀。

```
[os]
name=Qcloud centos os - $basearch
baseurl=http://mirrors.tencentyun.com/centos1/$releasever/os/$basearch/
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
```

### repo文件常用属性详解

```
[serverid]
```

serverid是用于区别各个不同的repository，必须有一个独一无二的名称。

```
name=Some name for this server
```

name，是对repository的描述，支持像$releasever $basearch这样的变量。

```
mirrorlist=url://
```

mirrorlist指定了一个URL地址，该地址是一个包含有众多源镜像地址的列表，当用户通过yum安装或升级软件时，yum会试图依次从列表中所示的镜像源中进行下载，如果从一个镜像源下载失败，则会自动尝试列表中的下一个。若列表遍历完成依然没有成功下载到目标软件包，则向用户抛错。

```
baseurl=url://server1/path/to/repository/
url://server2/path/to/repository/
url://server3/path/to/repository/
```

baseurl后可以跟多个url，你可以自己改为速度比较快的镜像站，但baseurl只能有一个。

baseurl是服务器设置中最重要的部分，只有设置正确，才能从上面获取软件。其中url支持的协议有`http://`、`ftp://`、`file://`三种。

其中url指向的目录必须是这个repository header目录的上一级，它也支持$releasever $basearch这样的变量。

url之后可以加上多个选项，如gpgcheck、exclude、failovermethod等，




```
gpgcheck=[1 or 0]
gpgkey=url://
```

`gpgchkeck=` 有1和0两个选择，分别代表是否是否进行gpg校验，如果没有这一项，默认是检查的。gpgkey则用来指明KEY文件的地址，同样支持`http、ftp和file`三种协议。

```
exclude=
```

exclude指明将哪些软件排除在升级名单之外，可以用通配符，列表中各个项目需用空格隔开。

```
failovermethod=priority   
priority=
```

failovermethode在yum有多个源可供选择时，决定其选择的顺序。该属性有两个选项：roundrobin和priority。roundrobin是随机选择，如果连接失败，则使用下一个，依次循环。priority则根据url的次序从第一个开始，如果不指明，默认是roundrobin。

```
enabled=[1 or 0]
```

当某个软件仓库被配置成 `enabled=0` 时，yum 在安装或升级软件包时不会将该仓库做为软件包提供源。使用这个选项，可以启用或禁用软件仓库。

### repo文件常用变量

* `$releasever`：发行版的版本，从[main]部分的distroverpkg获取，如果没有，则根据redhat-release包进行判断。   
* `$arch`：cpu体系，如i386、x86_64等。   
* `$basearch`：cpu的基本体系组，如i686和athlon同属i386，alpha和alphaev6同属alpha。   

### gpg校验

那就是导入每个reposity的GPG key，前面说过，yum可以使用gpg对包进行校验，确保下载包的完整性，所以我们先要到各个repository站点找到gpg key，一般都会放在首页的醒目位置，一些名字诸如 RPM-GPG-KEY.txt之类的纯文本文件，把它们下载，然后用rpm --import xxx.txt命令将它们导入，最好把发行版自带GPG-KEY也导入，rpm --import /usr/share/doc/redhat-release-*/RPM-GPG-KEY 官方软件升级用的上

### yum安装软件

yum自动判断依赖后，安装依赖的软件后会安装指定的软件。

yum命令格式：

```
yum [options] [command] [package ...]
```

* [options]是可选的，选项包括-h（帮助），-y（当安装过程提示选择全部为"yes"），-q（不显示安装的过程）等等。

* [command]为所要进行的操作，[package ...]是操作的对象。

#### yum参数[optios]

|参数|描述|
|:--:|--|
|-h|显示帮助信息|
|-y|对所有的提问都回答“yes”|
|-c|指定配置文件|
|-q|安静模式 |
|-v|详细模式|
|-d|设置调试等级（0-10）|
|-e|设置错误等级（0-10）|
|-R|设置yum处理一个命令的最大等待时间|
|-C|完全从缓存中运行，而不去下载或者更新任何头文件|

#### yum命令[command]

|命令|描述|
|:---:|---|
|install       |安装rpm软件包|
|update        |更新rpm软件包|
|check-update  |检查是否有可用的更新rpm软件包|
|remove        |删除指定的rpm软件包|
|list          |显示软件包的信息|
|search        |检查软件包的信息|
|info          |显示指定的rpm软件包的描述信息和概要信息|
|clean         |清理yum过期的缓存|
|shell         |进入yum的shell提示符|
|resolvedep    |显示rpm软件包的依赖关系|
|localinstall  |安装本地的rpm软件包|
|localupdate   |显示本地rpm软件包进行更新|
|deplist       |显示rpm软件包的所有依赖关系|
|groupCOMMAND  |安装一组软件，可以使用grouplist/groupinstall/等|

##### 安装软件/组

|安装命令|描述|
|:---:|--|
|yum install            | 全部安装 |
|yum install package1   | 安装指定的安装包package1 |
|yum groupinsall group1 |安装程序组group1|

##### 更新和升级

|更新升级命令|描述|
|:--:|--|
|yum update             |全部更新 |
|yum update package1    |更新指定程序包package1 |
|yum check-update       |检查可更新的程序| 
|yum upgrade package1   |升级指定程序包package1 |
|yum groupupdate group1 |升级程序组group1|

##### 查找和显示

|查找命令|描述|
|:---:|---|
|yum info package1     |显示安装包信息package1 |
|yum list              |显示所有已经安装和可以安装的程序包 |
|yum list package1     |显示指定程序包安装情况package1|
| yum groupinfo group1 |显示程序组group1信息|
|yum search string     |根据关键字string查找安装包|

##### 删除程序

|删除程序命令|描述|
|:---:|---|
|yum remove/erase package1 |删除程序包package1 |
|yum groupremove group1    |删除程序组group1   |
|yum deplist package1      |查看程序package1依赖情况|

##### 缓存删除

|缓存命令|描述|
|:--:|---|
|yum clean packages    |清除缓存目录下的软件包|
|yum clean headers     |清除缓存目录下的 headers|
|yum clean oldheaders |清除缓存目录下旧的 headers|
|yum clean all         |清楚所有缓存packages/headers/oldheaders|


## yum服务端配置

### createrepo创建yum源仓库

将准备好的软件复制到目录中，指定group的说明信息xml文件。使用如下命令可以分析软件之间依赖关系。

#### createrepo简介
createrepo用以创建yum源（软件仓库），即为存放于本地特定位置的众多rpm包建立索引，描述各包所需依赖信息，并形成元数据。

#### createrepo语法

基本语法：

```
createrepo [option] <directory>
```

通常情况下需要依次指定两个路径（directory）：第一个是放置即将生成的元数据目录的位置，第二个则是存放rpm包用来提供下载的位置。

常用参数（option）详解见下文描述。

#### createrepo常用参数详解

|参数|描述|
|---|---|
|-u --baseurl <url>         |指定Base URL的地址|
|-o --outputdir <url>       |指定元数据的输出位置|
|-x --excludes <packages>   |指定在形成元数据时需要排除的包|
|-i --pkglist <filename>    |指定一个文件，该文件内的包信息将被包含在即将生成的元数据中，格式为每个包信息独占一行，不含通配符、正则，以及范围表达式|
|-n --includepkg            |通过命令行指定要纳入本地库中的包信息，需要提供URL或本地路径|
|-q --quiet                 |安静模式执行操作，不输出任何信息|
|-g --groupfile <groupfile> |指定本地软件仓库的组划分，范例如下：createrepo -g comps.xml /path/to/rpms。注意：组文件需要和rpm包放置于同一路径下。|
|-v --verbose               |输出详细信息|
|-c --cachedir <path>       |指定一个目录，用作存放软件仓库中软件包的校验和信息。当createrepo在未发生明显改变的相同仓库文件上持续多次运行时，指定cachedir会明显提高其性能|
|--update                   |如果元数据已经存在，且软件仓库中只有部分软件发生了改变或增减，则可用update参数直接对原有元数据进行升级，效率比重新分析rpm包依赖并生成新的元数据要高很多|
|-p --pretty                |以整洁的格式输出xml文件|
|-d --database              |该选项指定使用SQLite来存储生成的元数据，默认项|
|-s                         |指定文件校验算法。sha1|
|--update                   |增加新rpm包是更新元数据|

#### createrepo示例

创建新的yum源

```
createrepo -s sha1 .
```

当添加新软件时，在原有yum源基础上更新metadata数据

```
createrepo -s sha1 --update .
```


### yum源服务的搭建

#### file本地yum源

file本地yum源使用file文件传输协议，在createrepo创建好metadata之后就可以使用。客户端使用`file:///`

#### http yum源

http yum源使用http的协议来进行文件传输，将createrepo完成的yum源路径配置到web服务器的目录配置上，启动web服务后。客户端使用`baseurl=http://`

web服务器可以根据情况自行选择，常见的有：Nginx/Tengine、Apache/httpd等。

至于这些web服务器的具体用法，可以参考该类型下的文章。

#### ftp yum源

ftp yum就是使用ftp协议来传输文件，将createrepo完成的yum源路劲配置到ftp服务器的目录配置上，常用的软件是vsftp，安装配置启动后，客户端使用`baseurl=ftp://`



## yum错误收集

### yum源中有软件但是安装时却找不到

#### 错误信息

清空本地缓存，使用wget能够下载，但是不能使用yum安装。yum报错说找不到改文件

#### 错误原因

yum源增加了新文件，但是没有更新yum源的metadata

#### 处理方法

更新yum的的metadata

```
cd /yum/
createrepo -t sha1 .
```

### Metadata file does not match checksum

#### 错误信息

```
http://autoinstall-stable.plesk.com/PSA_11.5.30/dist-rpm-CentOS-5-i386/repodata/filelists.xml.gz:(http://autoinstall-stable.plesk.com/PSA_11.5.30/dist-rpm-CentOS-5-i386/repodata/filelists.xml.gz:)
[Errno -1]Metadata file does not match checksum
Trying other mirror.
NoMoreMirrorsRepoError: failure: repodata/filelists.xml.gz from PSA_11_5_30-dist:[Errno 256]No more mirrors to try.
```

#### 错误原因

yum源的校验文件发生了改变，但是yum使用了自己缓存的数据

#### 处理方法

* 修改配置文件

在/etc/yum.conf文件中添加如下行

```
http_caching=none
```

* 删除缓存文件

```
rm -rf /var/cache/yum/*
```

* 清空缓存

```
yum clean all
```



{% include links.html %}
