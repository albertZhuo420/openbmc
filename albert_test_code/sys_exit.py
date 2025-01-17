#!/bin/env python3

import sys

print("+++++++++++++++++++++++++")
# sys.exit()
# sys.exit(0)
sys.exit(1)
sys.exit("测试一下异常") # 会在终端打印这句话

"""
关于python退出程序的方法, 本篇讨论的是sys.exit(), 这也是大家使用最多的方法之一。
下面我们就sys.exit()的概念、异常捕获两种结果进行分析, 最后带来sys.exit()退出程序的实例代码。

1. 概念:
	sys.exit()函数是通过抛出异常的方式来终止进程的, 也就是说如果它抛出来的异常被捕捉到了的话程序就不会退出了。

2. 异常捕获分析:
	2.1 如果这个异常没有被捕获, 那么python编译器将会退出, 后面的程序将不会执行;
	2.2 如果这个异常被捕获(try...except...finally), 捕获这个异常可以做一些额外的清理工作, 
		后面的程序还会继续执行。
	注: 0为正常退出, 其他数值(1-127)为不正常, 可抛异常事件供捕获;

3. 实例: 
	import sys
	sys.exit()
	sys.exit(0)
	sys.exit(1)

	该方法引发的是一个SystemExit异常(这是唯一一个不会被认为是错误的异常), 
	当没有设置捕获这个异常将会直接退出程序执行, 当然也可以捕获这个异常进行一些其他操作。

	sys.exit()这个函数, 只有认为退出码为0是正常退出, 而其他退出码则会认为是异常退出, 
	系统自动抛出SystemExit的异常, 方便开发人员在外层捕获并处理。
	如果需要返回退出码, 而不抛出异常的话, 可以使用os._exit()函数。

	以上就是python使用sys.exit()退出程序的方法, sys.exit()是通过没有捕获异常来判断退出程序了.
"""
