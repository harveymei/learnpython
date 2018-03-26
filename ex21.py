# -*- coding: utf-8 -*-
#定义函数
#定义一个add()函数，包含两个参数，执行加法运算
def add(a, b):
#玄机在于，此处的自定义函数，打印字符串部分，在第一次调用及赋值变量时并未显示
#在智力游戏部分，确将此打印内容输出了
	print "ADDING %d + %d" % (a, b)
	return a + b

#定义一个subtract()函数，包含两个参数，执行减法运算
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

#定义一个multiply()函数，包含两个参数，执行乘法运算
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

#定义一个divide()函数，包含两个参数，执行除法运算
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b


print "Let's do some math with just functions!"

#调用函数进行计算，并将函数return结果赋值给变量
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

#打印字符串及变量，格式化输出，35，74，180，50
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

#函数内嵌套函数，将一个函数的返回值作为另一个函数的参数处理
#从内到外依次为除法，乘法，减法，加法，且不包含已赋值变量部分的运算
#35+[74-180*(50/2)]
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do ti by hand?"


#MacBookAir:~ harveymei$ python ex21.py
#Let's do some math with just functions!
#ADDING 30 + 5
#SUBTRACTING 78 - 4
#MULTIPLYING 90 * 2
#DIVIDING 100 / 2
#Age: 35, Height: 74, Weight: 180, IQ: 50
#Here is a puzzle.
#DIVIDING 50 / 2
#MULTIPLYING 180 * 25
#SUBTRACTING 74 - 4500
#ADDING 35 + -4426
#That becomes:  -4391 Can you do ti by hand?
#MacBookAir:~ harveymei$