#!usr/bin/python
# -*- coding: UTF-8 -*-
import sys
def foo():
    b = 'hello'
    #python可以在函数内部再定义函数
    # a在main中定义，属于全局变量，因此bar可以使用a
    # b在foo中定义，因为bar为foo中定义的函数，因此可以使用b，属于嵌套作用域
    # c在bar中定义，属于局部变量，因此只能bar中使用
    def bar():
        c = True
        print(a)
        print(b)
        print(c)

    print("foo")
    bar()
    #error
    # print(c)

def func1():
    a = 200
    print(a)

def func2():
    global a
    a = 200
    print(a)

def func3():
    b = 10
    def bar():
        # 同理，如果我们希望函数内部的函数能够修改嵌套作用域中的变量，可以使用nonlocal关键字来指示变量来自于嵌套作用域
        nonlocal b
        b = 20
    bar()
    print(b) #20
    
if __name__ == '__main__':
    a = 100
    foo()
    print("========================")
    #可以看到，这里的a还是100，调用func1之后，相当于在func1内部重新定义了一个局部变量a
    func1()
    print(a)
    print("========================")
    #我们可以使用global关键字来指示func2函数中的变量a来自于全局作用域，
    # 如果全局作用域中没有a，那么下面一行的代码就会定义变量a并将其置于全局作用域
    func2()
    print(a)
    print("========================")
    func3()