#!usr/bin/python
# -*- coding: UTF-8 -*-
# 元组
# Python中的元组与列表类似也是一种容器数据类型，可以用一个变量（对象）来存储多个数据，
# ！！！！！！不同之处在于元组的元素不能修改
# ！！！！元组使用()
"""
有list的情况下我们为什么还需要元组：
    1、在多线程环境下，为了防止某些共享变量被修改，我们可以使用元组定义
    2、元组在创建时间和占用的空间上面都优于列表
"""
# 定义元组
t = ('骆昊', 38, True, '四川成都')
print(type(t))
print(t)
# 获取元组中的元素
print(t[0])
print(t[3])
# 遍历元组中的值
for member in t:
    print(member)
# 重新给元组赋值
# t[0] = '王大锤'  # TypeError
# 变量t重新引用了新的元组原来的元组将被垃圾回收
t = ('王大锤', 20, True, '云南昆明')
print(t)
# 将元组转换成列表
person = list(t)
print(person)
# 列表是可以修改它的元素的
person[0] = '李小龙'
person[1] = 25
print(person)
# 将列表转换成元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)
