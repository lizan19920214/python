"""
条件变量：
    condition能够实现在某些条件下才会释放锁。其常用方法包含：
        wait()：挂起进程，收到notify()通知后继续运行；
        notify()：通知其他线程，解除其他线程中的一个线程的阻塞状态；
        notifyall()：通知其他线程，解除其他所有线程的阻塞装；
        acquire()：获得锁；
        release()：释放锁；
"""
from multiprocessing import Process, Condition, Value
import time

def product(num, con):
    con.acquire()
    while True:
        print("开始生产.")
        num.value += 1
        print("产品数量：{}".format(str(num.value)))
        time.sleep(1)
        if num.value >= 5:
            print("产生数量已达到5个，无法继续生产")
            con.notify()  # 唤醒消费者
            con.wait()  # 阻塞，等待唤醒
    con.release()

def consume(num, con):
    con.acquire()
    while True:
        print("开始消费.")
        num.value -= 1
        print("产品剩余数量：{}".format(num.value))
        time.sleep(1)
        if num.value <= 0:
            print("产品已被消费完.")
            con.notify()  # 唤醒生产者
            con.wait()  # 阻塞，等待唤醒
    con.release()

if __name__ == '__main__':
    num = Value('i', 0)  # 进程间共享内存
    con = Condition()
    producer = Process(target=product, args=(num, con))
    consumer = Process(target=consume, args=(num, con))
    producer.start()
    consumer.start()
