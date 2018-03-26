# -*- coding: utf-8 -*-
#引用模块
from sys import argv

#把argv解包，将所有参数依次赋值给左边的变量
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third