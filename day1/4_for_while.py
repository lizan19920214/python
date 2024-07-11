#!usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import random

#for循环 0-4
for i in range(5):
    print(i)
print("=======================")

#for循环 1-4
for i in range(1, 5):
    print(i)
print("=======================")

#for 1-4，每次递增2
for i in range(1, 5, 2):
    print(i)
print("=======================")

#for 5-2，每次递减2
for i in range(5, 1, -2):
    print(i)
print("=======================")

#配合控制语句
sum = 0
for i in range(1, 5):
    if i % 2 == 0:
        sum += i
print(sum)
print("=======================")

#while循环
#和c++类似，break跳出当前循环，continue跳过本次循环
number = random.randint(1, 100)
print("random num %d" % number)
while True:
    input_num = int(input("input a num:"))
    if input_num == number:
        print("success")
        break
    else:
        if input_num > number:
            print("too big")
        else:
            print("too small")