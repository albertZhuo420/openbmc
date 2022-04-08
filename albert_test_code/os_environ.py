#!/bin/env python3

import os

#
# 参考链接: https://blog.csdn.net/junweifan/article/details/7615591
# 

print("keys=================================================")
print(os.environ.keys()) # 在wsl打印出来的是键值对
print("HOME=================================================")
print(os.environ["HOME"])
print("WSL_DISTRO_NAME=================================================")
print(os.environ["WSL_DISTRO_NAME"])
# print("BBDEBUG=================================================")
# print(os.environ["DEBUG"])
# wsl终端没有 BBDEBUG, HOME  BBDEBUG 要在keys中存在才可以使用
