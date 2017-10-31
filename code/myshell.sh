#!/bin/bash
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Script Name     : $0
# Script Author   : Vinny
# Script Descript : Script Function Lib
# Author Email    : admin@zhaowenyu.com
# Charset         : utf8
#-----------------------------------------------

#LOG_OFFON设置将日志保存到文件还是输出到命令，配置文件路径则会输出到文件，不配置则输出到终端
LOG_FILE="test.log"
# 日志级别
# ERROR  错误  红色  echo -e "\033[31m 红色字 \033[0m"
# WARN   告警  黄色  echo -e "\033[33m 黄色字 \033[0m"
# INFO   提示  绿色  echo -e "\033[32m 绿色字 \033[0m"
LOG() {
    level=$1
    msg=$2
    if [ -z "$LOG_FILE" ] ;then
        [ ! -f $LOG_FILE ] && echo "`date`" > $LOG_FILE
        if [ "$level" = "ERROR" ] ;then
            echo -e "\033[31m $msg \033[0m" >> $LOG_FILE
        elif [ "$level" = "WARN" ] ;then
            echo -e "\033[33m $msg \033[0m" >> $LOG_FILE
        elif [ "$level" = "INFO" ] ;then
            echo -e "\033[32m $msg \033[0m" >> $LOG_FILE
        else
           echo "未知日志级别" >> $LOG_FILE
           echo "LOG函数引用方式: LOG (ERROR|WARN|INFO) \$msg" >> $LOG_FILE
        fi
    else
        if [ "$level" = "ERROR" ] ;then
            echo -e "\033[31m $msg \033[0m"
        elif [ "$level" = "WARN" ] ;then
            echo -e "\033[33m $msg \033[0m"
        elif [ "$level" = "INFO" ] ;then
            echo -e "\033[32m $msg \033[0m"
        else
           echo "未知日志级别"
           echo "LOG函数引用方式: LOG (ERROR|WARN|INFO) \$msg"
        fi
    fi
}

LOG ERROR "xxxxxxxxxxxxx"
