# -*- coding: utf-8 -*-
from sys import argv

#把argv解包，将所有参数依次赋值给左边的变量
script, user_name = argv
#定义一个命令提示符的变量
prompt = '> '

#打印字符串，引用变量
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd linke to ask you a few questions."
print "Do you like me %s?" % user_name
#将用户提示符设置为变量，不需要在每次用到raw_input时重复输入
#将用户输入赋值给变量，在最后一段引用变量
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
