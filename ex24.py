# -*- coding: utf-8 -*-
#打印，使用转义字符\‘转义单引号，\\转义一个斜线，\n换行，\t制表符
print "Let's practice everything."
print 'You\'d need to know \'about escapes with \\ that do \n newlines and \t tabs.'

#定义一个变量，使用三引号中的内容进行赋值
poem = """
\tThe lovely world
with logic so firmly palanted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explannation
\n\t\twhere there is none.
"""

#打印变量内容
print "--------------"
print poem
print "--------------"

#定义一个变量，赋值为运算结果5
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

#定义一个函数，包含一个参数
#函数内进行变量定义和运算赋值，使用return返回运算结果
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates


#定义一个变量，赋值
start_point = 10000
#调用函数secret_furmula()，参数为10000，将返回结果依次赋值给三个变量
beans, jars, crates = secret_formula(start_point)

#打印字符串及输出格式化字符变量
print "With a starting poin of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

#定义并赋值变量，将原start_point的1/10即1000赋值给变量
start_point = start_point / 10

#再次直接调用函数并将运算结果作为变量返回给字符串值中的格式化字符
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)


#MacBookAir:~ harveymei$ python Documents/GitHub/learnpython/ex24.py
#Let's practice everything.
#You'd need to know 'about escapes with \ that do
# newlines and 	 tabs.
#--------------
#
#	The lovely world
#with logic so firmly palanted
#cannot discern
# the needs of love
#nor comprehend passion from intuition
#and requires an explannation
#
#		where there is none.
#
#--------------
#This should be five: 5
#With a starting poin of: 10000
#We'd have 5000000 beans, 5000 jars, and 50 crates.
#We can also do that this way:
#We'd have 500000 beans, 500 jars, and 5 crates.
#MacBookAir:~ harveymei$