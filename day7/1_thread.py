"""
在 Python 中，threading 模块提供了多线程编程的基础。你可以通过创建 threading.Thread 对象来创建新的线程，
并将目标函数和参数传递给线程。在创建和启动线程后，可以通过 join() 方法等待线程完成执行。
"""
from random import randint
from threading import Thread
from time import time, sleep


def download(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(1, 3)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    t1 = Thread(target=download, args=('Python从入门到住院.pdf',))
    t2 = Thread(target=download, args=('vedio.avi',))

    # 启动线程
    t1.start()
    t2.start()
    # 等待线程完成
    t1.join()
    t2.join()
    
    end = time()
    print('总共耗费了%.3f秒' % (end - start))


if __name__ == '__main__':
    main()