---
title: Tengine支持PHP
keywords: tengine 
last_updated: June 12, 2017
tags: [php,tengine]
summary: aa 
sidebar: note_sidebar
permalink: note_nginx_tengine_php.html
folder: note 
---

Tengine部署PHP

```
yum install php-fpm
php-fpm start
```


修改配置文件


```
location ~ \.php$ {
    root           /usr/local/tengine/html;
    fastcgi_pass   127.0.0.1:9000;
    fastcgi_index  index.php;
    fastcgi_param  SCRIPT_FILENAME  /usr/local/tengine/html$fastcgi_script_name;
    include        fastcgi_params;
}
```


{% include links.html %}
