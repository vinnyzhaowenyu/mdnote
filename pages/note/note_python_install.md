---
title: Python 安装
keywords: install 
last_updated: September 30, 2017
tags: [python]
summary: aa 
sidebar: note_sidebar
permalink: note_python_install.html
folder: note 
---

## 安装 Python3

```
wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz
tar xf Python-3.6.2.tgz
./configure  --prefix=/usr/local/python3 --enable-optimizations
make && make install
echo "export PATH=$PATH:/usr/local/python3/bin" >> /etc/profile
source /etc/profile
````



{% include links.html %}
