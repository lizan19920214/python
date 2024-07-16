"""
进程同步：
    Lock锁
    通过使用Lock来控制一段代码在同一时间只能被一个进程执行。Lock对象的两个方法，
    acquire()用来获取锁，release()用来释放锁。当一个进程调用acquire()时，
    如果锁的状态为unlocked，那么会立即修改为locked并返回，这时该进程即获得了锁。如果锁的状态为locked，那么调用acquire()的进程则阻塞。
"""
import os
import time
import random
from multiprocessing import Process

def work(n):
    print('{}: {} is running'.format(n, os.getpid()))
    time.sleep(random.random())
    print('{}: {} is done'.format(n, os.getpid()))

if __name__ == '__main__':
    for i in range(3):
        p = Process(target=work,args=(i,))
        p.start()
# 输出可能结果
# 可以看到在没有锁的情况下，running和done的结果是无序的
# 0: 12150 is running
# 1: 12151 is running
# 2: 12152 is running
# 1: 12151 is done
# 0: 12150 is done
# 2: 12152 is done
time.sleep(2)
print("============================================")
import os
import time
import random
from multiprocessing import Process, Lock

def work(lock, n):
    lock.acquire()  # 获得锁，只有一个进程可以获得
    print('{}: {} is running'.format(n, os.getpid()))
    time.sleep(random.random())
    print('{}: {} is done'.format(n, os.getpid()))
    lock.release()  # 释放锁

if __name__ == '__main__':
    lock = Lock()
    for i in range(3):
        p = Process(target=work, args=(lock,i))
        p.start()

# 输出可能结果
# 我们加入锁之后，可以看到单个进程要完整走完running和done，下一个进程才能获得锁进行执行
# 0: 14429 is running
# 0: 14429 is done
# 1: 14430 is running
# 1: 14430 is done
# 2: 14431 is running
# 2: 14431 is done