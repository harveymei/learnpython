# -*- coding: utf-8 -*-
from sys import argv

script, input_file = argv

#定义一个函数，指定一个参数f，将以参数形式传入的内容用read()命令读取并打印输出
def print_all(f):
	print f.read()

#定义一个函数，使用seek()方法/命令，移动文件读取指针到指定位置
def rewind(f): #回退，倒带
	f.seek(0)

#定义一个函数，指定两个参数，打印参数中传递的行号，并使用redline()方法/命令读取一行内容
def print_a_line(line_count, f):
	print line_count, f.readline()

#赋值一个变量，内容为打开用户传递参数的文件，作为未来函数调用的参数
current_file = open(input_file)

print "First let's print the whole file:\n"

#调用函数print_all()，参数f为用户传递参数赋值变量的已打开文件，执行打印读取命令
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#调用rewind()函数，参数f为用户传递参数赋值变量的已打开文件，执行移动文件读取指针到0字节位置
rewind(current_file)

print "Let's print three lines:"

#赋值变量，当前行为第1行
current_line = 1
#调用print_a_line()函数，打印行号1，将用户传递参数已open文件使用readline()方法/命令读取到的内容
print_a_line(current_line, current_file)

#定义变量并赋值，在变量中进行数学计算，当前行为1+1即第2行
current_line = current_line + 1
#调用print_a_line()函数，打印行号2，将用户传递参数已open文件使用readline()方法/命令读取到的内容
print_a_line(current_line, current_file)

#当前行为2+1即第3行
current_line = current_line + 1
print_a_line(current_line, current_file)

#readline()函数返回的内容中包含文件中已有的\n换行，print在打印时也会添加一个\n
#多出一个空行的的解决方法是在print语句结尾加一个,逗号
#MacBookAir:~ harveymei$ python ex20.py ex20_test.txt
#First let's print the whole file:#
#
#This is line 1
#This is line 2
#This is line 3
#Now let's rewind, kind of like a tape.
#Let's print three lines:
#1 This is line 1
#
#2 This is line 2
#
#3 This is line 3
#MacBookAir:~ harveymei$ cat ex20_test.txt
#This is line 1
#This is line 2
#This is line 3MacBookAir:~ harveymei$