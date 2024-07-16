"""
多进程
Python的os模块提供了fork()函数。由于Windows系统没有fork()调用，因此要实现跨平台的多进程编程，
    可以使用multiprocessing模块的Process类来创建子进程，而且该模块还提供了更高级的封装，
    例如批量启动进程的进程池（Pool）、用于进程间通信的队列（Queue）和管道（Pipe）等。

特点：
    1、单个CPU在任一时刻只能执行单个线程，只有多核CPU还能真正做到多个线程同时运行
    2、一个进程包含多个线程，这些线程可以分布在多个CPU上
    3、多核CPU同时运行的线程可以属于单个进程或不同进程

Python是个特例！!

GIL锁
全称为Global Interpreter Lock，也就是全局解释器锁。

GIL规定，在一个进程中每次只能有一个线程在运行。这个GIL锁相当于是线程运行的资格证，某个线程想要运行，
        首先要获得GIL锁，然后遇到IO或者超时的时候释放GIL锁，给其余的线程去竞争，竞争成功的线程获得GIL锁得到下一次运行的机会。

正是因为有GIL的存在，python的多线程其实是假的，所以才有人说python的多线程非常鸡肋。但是虽然每个进程有一个GIL锁，进程和进程之前还是不受影响的。

GIL是个历史遗留问题，过去的版本迭代都是以GIL为基础来的，想要去除GIL还真不是一件容易的事，所以我们要做好和GIL长期面对的准备。


看一下Process类的构造方法：
__init__(self, group=None, target=None, name=None, args=(), kwargs={})

group：进程所属组（基本不用） 
target：表示调用对象
args：表示调用对象的位置参数元组
name：别名 
kwargs：表示调用对象的字典

"""
from multiprocessing import Process
from os import getpid
from time import time, sleep

def download_task(filename):
    print('进程id:%d 开始下载%s...' % (getpid() ,filename))
    #模拟下载耗时
    sleep(2)
    print('%s下载完成! 耗费了%d秒' % (filename, 2))

def main1():
    print('主进程id:%d' % getpid())
    start = time()
    download_task('Python从入门到住院.pdf')
    download_task('video.avi')
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))

def main2():
    print('主进程id:%d' % getpid())
    start = time()
    # target参数我们传入一个函数来表示进程启动后要执行的代码，后面的args是一个元组(最后的,不能省略)，它代表了传递给函数的参数
    p1 = Process(target = download_task, args = ('Python从入门到住院.pdf', ))
    # start方法用来启动进程
    p1.start()

    p2 = Process(target = download_task, args = ('video.avi', ))
    p2.start()
    # join方法表示等待进程执行结束
    p1.join()
    p2.join()

    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    print("单进程耗时：")
    main1()
    print("=================================")
    print("多进程耗时：")
    main2()