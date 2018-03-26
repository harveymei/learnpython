# -*- coding: utf-8 -*-
# this one is like your scripts with argv
#函数命名以字母，数字，下划线组成，且不以数字开始
#使用def定义define一个函数，函数名后紧跟括号，括号中包含参数，以冒号结尾
#*args告诉python把函数的所有参数接收进来，放到名字叫args的列表中，asterisk args,
def print_two(*args):
#使用4个空格缩进表示行属于这个函数
#解包参数，并打印参数
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
#跳过参数解包，直接使用括号里的参数名称作为变量名的示例
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
#函数接收单个参数的示例
def print_one(arg1):
	print "arg1: %r" % arg1
	
# this one takes no arguments
#函数不接收任何参数的示例
def print_none():
	print "I got nothing."


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
