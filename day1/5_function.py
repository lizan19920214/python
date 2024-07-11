#!usr/bin/python
# -*- coding: UTF-8 -*-

# 在Python中可以使用def关键字来定义函数
import sys
def add(a, b):
    return a + b

print(add(1, 2))
print(add(2, 3))
print("==========================")

#函数为值传递
def numAdd(a):
    a += 1

num = 10
numAdd(num)
print(num)
print("==========================")

#在Python中，函数的参数可以有默认值，也支持使用可变参数
def addVallue(a = 0, b = 0, c = 0):
    print(a, b, c)
    return a + b + c
print(addVallue())
print(addVallue(1, 2))
# 传递参数时可以不按照设定的顺序进行传递
print(addVallue(c = 50, a = 100, b = 200))
print("==========================")

#可变参数
def addArgs(*args):
    total = 0
    for val in args:
        total += val
    return total

print(addArgs())
print(addArgs(1, 2))
print(addArgs(1, 2, 3, 4, 5))
print("==========================")

# python没有函数重载的概念
# 如果定义了两个同名函数，则后一个函数会覆盖前一个函数，如下输出foo2
def foo():
    print("foo1")

def foo():
    print("foo2")

foo()