#!usr/bin/python
# -*- coding: UTF-8 -*-
"""
python3 control.py
分支控制
"""
import sys

username = input("请输入用户名:")
userpwd = input("请输入密码:")
if username == "lz" and userpwd == "123":
    print("登录成功")
else:
    print("用户名或密码错误")

"""
和C/C++、Java等语言不同，Python中没有用花括号来构造代码块而是使用了缩进的方式来表示代码的层次结构，
如果if条件成立的情况下需要执行多条语句，只要保持多条语句具有相同的缩进就可以了。
换句话说连续的代码如果又保持了相同的缩进那么它们属于同一个代码块，相当于是一个执行的整体。
缩进可以使用任意数量的空格，但通常使用4个空格，
建议大家不要使用制表键或者设置你的代码编辑工具自动将制表键变成4个空格。
"""
#多层if嵌套
value = int(input("请输入一个整数:"))
if value > 100:
    print("该数大于100,是%d" % value)
elif value < 50:
    print("该数小于50,是%d" % value)
else:
    print("该数在50和100之间,是%d" % value)

#另一种嵌套
if value > 100:
    print("该数大于100,是%d" % value)
else:
    if value < 50:
        print("该数小于50,是%d" % value)
    else:
        print("该数在50和100之间,是%d" % value)
