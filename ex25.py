# -*- coding: utf-8 -*-
#定义函数，参数为stuff
#定义变量words并将函数的参数以split()方法/命令操作后赋值给变量
#函数返回变量内容
def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

#定义函数，参数为words（上一个函数返回的结果）
#函数返回针对上一个函数返回结果以sorted()方法/命令进行排序
#在自定义函数中使用return返回调用另一个函数的结果
def sort_words(words):
	"""Sorts the words."""
	return sort(words) #书中错误为返回一个未定义的函数return sorted(words)

##定义函数，参数为words（上一个函数返回的结果）
#对words以pop()方法/命令处理并赋值变量，以打印方式输出该变量
def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word

#定义函数，参数为words（上一个函数返回的结果）
def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1) #重点
	print word

#定义函数，参数为sentence
#调用第一个自定义函数，将返回值赋值变量
#在return返回结果中调用第二个自定义函数
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence) 
	return sort_words(words) 

#定义函数，参数为sentence
#调用自定义函数break_words()，将返回结果赋值变量words
#调用自定义函数print_first_word(),使用print打印输出结果
#调用自定义函数print_last_word()，使用print打印输出结果
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

#定义函数，参数为sentence
#调用自定义函数sort_entence(),将返回结果赋值变量words
#调用自定义函数first_word(),参数为变量words
#调用自定义函数print_fisrt_last_word(),参数为变量words
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)


#使用python运行ex25.py，屏幕无输出，正常
#导入模块，手动自定义变量传递初始参数，开始调用自定义函数获取之执行结果
