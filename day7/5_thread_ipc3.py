"""
比较遗憾的一件事情是Python的多线程并不能发挥CPU的多核特性，这一点只要启动几个执行死循环的线程就可以得到证实了。
        之所以如此，是因为Python的解释器有一个“全局解释器锁”（GIL）的东西，任何线程执行前必须先获得GIL锁，然后每执行100条字节码，
        解释器就自动释放GIL锁，让别的线程有机会执行

因为GIL的存在，每次只能有一个线程可以对变量进行操作，那么是不是python就不需要互斥锁了呢
"""

import time
import threading

def increase(var):
    global total_increase_times
    for i in range(1000000):
        var[0] += 1
        total_increase_times += 1


def decrease(var):
    global total_decrease_times
    for i in range(1000000):
        var[0] -= 1
        total_decrease_times += 1
        
        
if __name__ == '__main__':
    print('main thread is {}'.format(threading.current_thread().name))
    start_time = time.time()
    var = [5]
    total_increase_times = 0
    total_decrease_times = 0
    t1 = threading.Thread(target=increase, args=(var,))
    t2 = threading.Thread(target=decrease, args=(var,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(var)
    print('total increase times: {}'.format(str(total_increase_times)))
    print('total decrease times: {}'.format(str(total_decrease_times)))
    end_time = time.time()
    print('total time is {}'.format(str(end_time - start_time)))

# 结果如下：
# main thread is MainThread
# [-59309]
# total increase times: 1000000
# total decrease times: 1000000
# total time is 0.18932723999023438
# 可以看到我们对变量进行相同次数的增加和减少，最后的结果却和原值不一样。
# 原因在于某些在我们看来是原子操作的，比如+和-，在python看来不是，例如执行a+=1操作，在python看来其实是三步：获取a的值，将值加1，将新的值赋给a。
# 在这三步中的任意位置，该线程都有可能被暂停，然后让别的线程先运行。这时候就有可能出现如下的局面:
"""
线程1获取了a的值为10，被暂停
线程2获取了a的值为10
线程2将a的值赋值为9，被暂停
线程1将a的值赋值为11，被暂停
线程2获取了a的值为11
...
"""
# 所以，在python中，如果想要实现原子操作，必须使用锁。