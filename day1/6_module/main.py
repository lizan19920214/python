#!usr/bin/python
# -*- coding: UTF-8 -*-

#上节我们说到，python中没有函数重载的概念，同个文件中同名的函数，则后一个函数会覆盖前一个函数
#我们在多人开发中如何避免这个问题呢
#其实很简单，Python中每个文件就代表了一个模块（module），
# 我们在不同的模块中可以有同名的函数，在使用函数的时候我们通过import关键字导入指定的模块就可以区分到底要使用的是哪个模块中的foo函数

#指定从muodule2中导入foo函数
from module2 import foo
foo()
print("=============================")

from module1 import foo
foo()
print("=============================")

# 也可以按照如下所示的方式来区分到底要使用哪一个foo函数。
import module1 as m1
import module2 as m2

m1.foo()
m2.foo()
print("=============================")

# 如果写成如下方式，同样是后g一个函数覆盖前一个函数
from module1 import foo
from module2 import foo
foo()
print("=============================")

def func():
    print("this is func()")

# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
# 相当于c++的main函数
if __name__ == '__main__':
    func()