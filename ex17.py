# -*- coding: utf-8 -*-
from sys import argv
#引入新的命令exists,以文件名字符串作为参数，返回true或false
from os.path import exists

#把argv解包，将所有参数依次赋值给左边的变量
#用户输入参数依次为，从哪个文件（源），到哪个文件（目的）
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#打开源文件，使用read()命令读取文件内容，并赋值给变量indata
# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()
#indata= 

#len()函数以数的形式返回传递字符串的长度，函数作用于文件正文内容
print "The input file is %d bytes long" % len(indata)

#使用exists()函数判断，目的文件是否存在，然后按照提示继续或者退出程序
print "Dose the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
#接收用户输入或动作
raw_input()

#以open函数和写入模式打开用户参数中指定的目的文件，执行写入命令，内容为源文件正文
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

#关闭目的文件，关闭源文件
out_file.close()
in_file.close()
