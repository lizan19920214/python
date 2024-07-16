"""
信号量
    Lock只允许同一时刻有一个进程访问锁住的代码段，而Semaphore则是允许一定数量的进程访问。
    Semaphore在实现时会维护一个计数器，每调用一个acquire()，计数器减1，调用一次release()则计数器加1。当计数器为0时，调用acquire()则会阻塞。
"""
import multiprocessing
import time

def worker(s, i):
    s.acquire()
    print(multiprocessing.current_process().name + " acquire")
    time.sleep(i)
    print(multiprocessing.current_process().name + " release")
    s.release()

if __name__ == "__main__":
    s = multiprocessing.Semaphore(2)  # 最多允许2个进程进入，否则阻塞
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(s, i * 2))
        p.start()

