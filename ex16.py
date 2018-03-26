# -*- coding: utf-8 -*-
from sys import argv

#把argv解包，将所有参数依次赋值给左边的变量
script, filename = argv

#打印字符串，引用文件名称变量，提示退出操作或继续操作
#CTRL-C退出的方法，实际有异常提示
print "We're going to erase %r." % filename
print "If you dong't want that, hint CTRL-C (^C)."
print "If you do want that, hit RETURN."

#接受用户输入
#回车或输入什么内容都可以继续，并没有将用户输入赋值给任何变量做引用或判断
raw_input("?")

#打印正在打开文件，使用open函数打开文件并使用写入模式
#w表示文件访问模式，w写入，r读取，a追加
print "Opening the file..."
target = open(filename, 'w')

#使用truncate命令清空文件
print "Truncation the file. Goodbye!"
target.truncate()

#开始新任务，提示用户输入三行内容
print "Now I'm goding to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

#提示将用户输入内容，写入文件
print "I'm going to write these to  the file."

#使用write命令写入文件，引用变量，并使用\n换行
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#提示已经关闭文件操作，使用close命令关闭当前操作的文件
print "And finally, we close it."
target.close()

#MacBookAir:~ harveymei$ python ex16.py ex16.txt
#We're going to erase 'ex16.txt'.
#If you dong't want that, hint CTRL-C (^C).
#If you do want that, hit RETURN.
#?yes
#Opening the file...
#Truncation the file. Goodbye!
#Now I'm goding to ask you for three lines.
#line 1: 1,what's your name?
#line 2: 2,what are you doing?
#line 3: 3,How old are you?
#I'm going to write these to  the file.
#And finally, we close it.
#MacBookAir:~ harveymei$ cat ex16.txt
#1,what's your name?
#2,what are you doing?
#3,How old are you?
#MacBookAir:~ harveymei$