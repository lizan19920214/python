"""
事件：
    Event是主线程控制其他线程的方式。在Event机制中，会设置一个"Flag"，如果"Flag"为False时，
    那么调用event.wait()的进程就会阻塞。当"Flag"为True时，那些阻塞了的进程就不再阻塞。
    其中, set()方法用于设置"Flag"为True，clear()则是设置"Flag"为False。
"""
import multiprocessing
import time

def wait_for_event(e):
    """等待event对象被设置为True"""
    print('process %s starting' % multiprocessing.current_process().name)
    e.wait()  # 如果主线程不设置event对象，那么该进程会一直阻塞
    print('process %s ' % multiprocessing.current_process().name + 'event: e.is_set()->' + str(e.is_set()))

def wait_for_event_timeout(e, t):
    """Wait t seconds and then timeout"""
    print('process %s starting' % multiprocessing.current_process().name)
    e.wait(t)  # 如果主线程不设置event对象，那么该进程会一直阻塞直至超时
    print('process %s ' % multiprocessing.current_process().name + 'event_timeout: e.is_set()->' + str(e.is_set()))

if __name__ == '__main__':
    e = multiprocessing.Event()
    print(e.is_set())  # Event的初始状态为False。此时，任何调用该Event对象的wait()方法都会阻塞
    #name 设置进程别名
    w1 = multiprocessing.Process(name='block',
                                 target=wait_for_event,
                                 args=(e,))
    w1.start()

    w2 = multiprocessing.Process(name='non-block',
                                 target=wait_for_event_timeout,
                                 args=(e, 2))
    w2.start()

    time.sleep(5)
    # 将event的Flag改为true
    e.set()
    w1.join()
    w2.join()
    print('main: event is set')