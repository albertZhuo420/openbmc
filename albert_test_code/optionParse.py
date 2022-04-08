#!/usr/bin/python3

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", 
				  dest="filename__",
    			  help="write report to FILE", 
				  metavar="FILE")
parser.add_option("-q", "--quiet",
    			  action="store_false", 
				  dest="verbose__", 
				  default=True,
				  help="don't print status messages to stdout")

(options, args) = parser.parse_args()
print ("==========")
print(options.filename__)
print(options.verbose__) 

#
# zhuo@winHost:/mnt/d/code/source_code_分析/openbmc_src/albert_test_code$ ls
# 01_setup脚本相关  optionParse.py  sys_argv.py  sys_exit.py
# zhuo@winHost:/mnt/d/code/source_code_分析/openbmc_src/albert_test_code$ ./optionParse.py -f sys_argv.py
# ==========
# sys_argv.py
# True
# zhuo@winHost:/mnt/d/code/source_code_分析/openbmc_src/albert_test_code$ ./optionParse.py -f sys_argv.py
# ==========
# sys_argv.py
# True
# zhuo@winHost:/mnt/d/code/source_code_分析/openbmc_src/albert_test_code$ ./optionParse.py -f sys_argv.py
# ==========
# sys_argv.py
# True
# zhuo@winHost:/mnt/d/code/source_code_分析/openbmc_src/albert_test_code$ ./optionParse.py -f sys_argv.py -q
# ==========
# sys_argv.py
# False
# zhuo@winHost:/mnt/d/code/source_code_分析/openbmc_src/albert_test_code$ ./optionParse.py -f
# Usage: optionParse.py [options]
# 
# optionParse.py: error: -f option requires 1 argument
# zhuo@winHost:/mnt/d/code/source_code_分析/openbmc_src/albert_test_code$ ./optionParse.py
# ==========
# None
# True
# zhuo@winHost:/mnt/d/code/source_code_分析/openbmc_src/albert_test_code$ ./optionParse.py -q
# ==========
# None
# False
# zhuo@winHost:/mnt/d/code/source_code_分析/openbmc_src/albert_test_code$
#