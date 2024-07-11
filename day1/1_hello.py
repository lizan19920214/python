#!usr/bin/python
# -*- coding: UTF-8 -*-
#单行注释

"""
多行注释
python “Non-ASCII character 'xe5' in file”报错问题
    Python默认是以ASCII作为编码方式的，如果在自己的Python源码中包含了中文（或者其他非英语系的语言），
此时即使你把自己编写的Python源文件以UTF-8格式保存了，但实际上，这依然是不行的。

解决办法很简单，只要在文件开头加入下面代码就行了
# -*- coding: UTF-8 -*-

一定要加在源代码的 第一行！！！！
"""
import sys
print("hello world")