# -*- coding: utf-8 -*-
#定义一个函数，包含两个参数，奶酪数量，薄脆饼干数量
#在打印字符串过程中，将函数中参数作为变量引用
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n" #毯子，毛毯


#打印，调用已赋值的函数
print "We can just give the function number directoly:"
cheese_and_crackers(20, 30)


#定义两个变量并赋值，奶酪数量和薄脆饼干数量
print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

#再一次为自定义变量传递参数值，参数值为之前定义的两个变量，并自动打印结果
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


#也可以在函数中进行数学计算，再一次为函数传递参数值，并自动打印结果
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#函数的参数部分，既可以包含变量，也可以包含数学计算，并再一次自动打印结果
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 10000)

#函数一共被调用了4次，因此函数中的打印部分，将出现4次
#第一次，20，30
#第二次，10，50
#第三次，30，11
#第四次，110，10050