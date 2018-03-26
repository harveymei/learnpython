# -*- coding: utf-8 -*-
from sys import argv

#把argv解包，将所有参数依次赋值给左边的变量
script, filename = argv

#定义变量，使用open函数打开文件，并使用用户输入文件名，而不是写死（hardcode）
txt = open(filename)

#打印字符串，引用显示文件名变量，
print "Here's your file %r:" % filename
#使用read命令读取文件内容，并使用print打印输出
print txt.read()

#再一次在提示符中输入文件名，并使用open函数打开并读取文件
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()