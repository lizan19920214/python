#!usr/bin/python
# -*- coding: UTF-8 -*-
# ！！！！字典使用{}
# 字典是另一种可变容器模型，Python中的字典跟我们生活中使用的字典是一样一样的，
# 它可以存储任意类型对象，与列表、集合不同的是，
# 字典的每个元素都是由一个键和一个值组成的“键值对”，键和值通过冒号分开
# 创建字典的字面量语法
"""
python字典内置函数：
    1、cmp(dict1, dict2)
        比较两个字典元素。
    2、len(dict)
        计算字典元素个数，即键的总数。
    3、str(dict)
        输出字典可打印的字符串表示。
    4、type(variable)
        返回输入的变量类型，如果变量是字典就返回字典类型。
字典内置方法：
    1、dict.clear()
        删除字典内所有元素
    2、dict.copy()
        返回一个字典的浅复制 dict1 = dict2.copy()
    3、dict.fromkeys(seq[, val])
        创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
    4、dict.get(key, default=None)
        返回指定键的值，如果值不在字典中返回default值
    5、dict.has_key(key)
        如果键在字典dict里返回true，否则返回false。Python3 不支持。
    6、dict.items()
        以列表返回可遍历的(键, 值) 元组数组
    7、dict.keys()
        以列表返回一个字典所有的键
    8、dict.setdefault(key, default=None)
        和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
    9、dict.update(dict2)
        把字典dict2的键/值对更新到dict里
    10、dict.values()
        以列表返回字典中的所有值
    11、pop(key[,default])
        删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
    12、popitem()
        返回并删除字典中的最后一对键和值。
"""

scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
print(scores)
# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)
# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))
# 创建字典的推导式语法
# key 1-9，value 1-9的平方(**)
items3 = {num: num ** 2 for num in range(1, 10)}
print(items1)
print(items2)
print(items3)
# 通过键可以获取字典中对应的值
print(scores['骆昊'])
print(scores['狄仁杰'])
# 对字典中所有键值对进行遍历
for key in scores:
    print(f'{key}: {scores[key]}')
# 更新字典中的元素
scores['白元芳'] = 65
scores['诸葛王朗'] = 71
scores.update(冷面=67, 方启鹤=85)
print(scores)
if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天'))
# get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('武则天', 60))
# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('骆昊', 100))
# 清空字典
scores.clear()
print(scores)
# 初始化一个空字典
dict1 = {}
print(type(dict1))
print(dict1)