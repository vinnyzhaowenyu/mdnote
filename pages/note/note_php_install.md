---
title: PHP安装
keywords: php 
last_updated: September 19, 2017
tags: [php]
summary: PHP安装
sidebar: note_sidebar
permalink: note_php_install.html
folder: note 
---

## yum安装

### Enterprise Linux 7 (with EPEL) x86_64
```
wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
wget https://rpms.remirepo.net/enterprise/remi-release-7.rpm
rpm -Uvh remi-release-7.rpm epel-release-latest-7.noarch.rpm
# for RHEL only
subscription-manager repos --enable=rhel-7-server-optional-rpms
```


## Enterprise Linux 6 (with EPEL) i386 or x86_64
```
wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm
wget https://rpms.remirepo.net/enterprise/remi-release-6.rpm
rpm -Uvh remi-release-6.rpm epel-release-latest-6.noarch.rpm
# for RHEL only
rhn-channel --add --channel=rhel-$(uname -i)-server-optional-6
```

配置
Enterprise Linux (RHEL, CentOS) :
```
su -
cd /etc/yum.repos.d
wget https://rpms.remirepo.net/enterprise/remi.repo
```



[remi官方网站](http://rpms.famillecollet.com/)
[remi 清华镜像](https://mirrors.tuna.tsinghua.edu.cn/remi/)
[yum获取列表](https://blog.remirepo.net/pages/Config-en)


{% include links.html %}
