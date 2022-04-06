#!/bin/env bash 

name=$(basename $0) 		# 变量赋值时不能有空格: name = $(basename $0)  是错的
echo $name 					

name1=$(basename -- $0)
echo $name1					

# 
# 当执行的命令是: ./basename.sh 时, 两个echo打印出来的结果都是: basename.sh
# 
# 当执行的命令是: . basename.sh 时, 两个echo打印出来的结果都是: bash
# 

# basename: 
#  从文件名中去掉路径信息, 只打印出文件名. 结构 basename $0 可以让脚本知道它自己的名字, 也就是, 它被调用的名字. 可以用来显示用法信息, 比如如果你调用脚本的时候缺少参数, 可以使用如下语句：
#  echo "Usage: `basename $0` arg1 arg2 ... argn"
# 
# $0: $0显示会包括当前脚本或命令的路径
# 
# dirname: 
#  从带路径的文件名中去掉文件名, 只打印出路径信息.
# 
# basename 和 dirname 可以操作任意字符串. 参数可以不是一个真正存在的文件, 甚至可以不是一个文件名