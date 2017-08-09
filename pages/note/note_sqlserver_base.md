---
title: SqlServer基础
keywords: sqlserver
last_updated: August 9, 2017
tags: [sqlserver]
summary: sqlserver 
sidebar: note_sidebar
permalink: note_sqlserver_base.html
folder: note 
---

## 数据库

#### 查看系统所有数据库
```
1> select * from sys.databases;
2> go
```

## 数据表

#### 查看数据库中的表

```
1> use fsdafds;
2> go
(0 rows affected)
1> select * from sys.tables;
2> go
```

{% include links.html %}
