---
title: rsync配置
keywords: rsync 
last_updated: June 20, 2017
tags: [getting_started]
summary: aa 
sidebar: note_sidebar
permalink: note_rsync_config.html
folder: note 
---




## /etc/rsyncd.secrets

配置rsync.secrets认证文件

```
rsync:123456
root:FDAS32^*fdfdsaFDSA
```

修改rsync.secrets认证文件权限

```
chmod 600 /etc/rsyncd.secrets
```



{% include links.html %}
