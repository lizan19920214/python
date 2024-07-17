import multiprocessing
import time
import os


def Lee():
    print('\nRun task Lee--%s******ppid:%s' % (os.getpid(), os.getppid()), '~~~~', time.ctime())
    start = time.time()
    time.sleep(5)
    end = time.time()
    print('Task Lee,runs %0.2f seconds.' % (end - start), '~~~~', time.ctime())


def Marlon():
    print("\nRun task Marlon-%s******ppid:%s" % (os.getpid(), os.getppid()), '~~~~', time.ctime())
    start = time.time()
    time.sleep(10)
    end = time.time()
    print('Task Marlon runs %0.2f seconds.' % (end - start), '~~~~', time.ctime())


def Allen():
    print("\nRun task Allen-%s******ppid:%s" % (os.getpid(), os.getppid()), '~~~~', time.ctime())
    start = time.time()
    time.sleep(15)
    end = time.time()
    print('Task Allen runs %0.2f seconds.' % (end - start), '~~~~', time.ctime())


def Frank():
    print("\nRun task Frank-%s******ppid:%s" % (os.getpid(), os.getppid()), '~~~~', time.ctime())
    start = time.time()
    time.sleep(20)
    end = time.time()
    print('Task Frank runs %0.2f seconds.' % (end - start), '~~~~', time.ctime())


if __name__ == '__main__':
    func_list = [Lee, Marlon, Allen, Frank]
    print('parent process id %s' % os.getpid())

    pool = multiprocessing.Pool(4)
    for func in func_list:
        pool.apply_async(func)

    print('Waiting for all subprocesses done...')
    pool.close()
    pool.join()
    print('All subprocesses done.')

# 进程池使用apply_async实现多进程多方法同时执行

# parent process id 32928
# Waiting for all subprocesses done...

# Run task Lee--32929******ppid:32928 ~~~~ Wed Jul 17 12:16:06 2024

# Run task Marlon-32930******ppid:32928 ~~~~ Wed Jul 17 12:16:06 2024

# Run task Allen-32931******ppid:32928 ~~~~ Wed Jul 17 12:16:06 2024

# Run task Frank-32932******ppid:32928 ~~~~ Wed Jul 17 12:16:06 2024
# Task Lee,runs 5.01 seconds. ~~~~ Wed Jul 17 12:16:11 2024
# Task Marlon runs 10.01 seconds. ~~~~ Wed Jul 17 12:16:16 2024
# Task Allen runs 15.03 seconds. ~~~~ Wed Jul 17 12:16:21 2024
# Task Frank runs 20.02 seconds. ~~~~ Wed Jul 17 12:16:26 2024
# All subprocesses done.