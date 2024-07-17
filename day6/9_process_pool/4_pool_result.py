import multiprocessing
import time


def func(msg):
    print('hello :', msg, time.ctime())
    time.sleep(2)
    print('end', time.ctime())
    return 'done' + msg


if __name__ == '__main__':
    pool = multiprocessing.Pool(2)
    result = []
    for i in range(3):
        msg = 'hello %s' % i
        result.append(pool.apply_async(func=func, args=(msg,)))

    pool.close()
    pool.join()

    for res in result:
        print('***:', res.get())             # get()函数得出每个返回结果的值

    print('All end--')

# get函数可以获得到进程池中各个进程的返回值


# hello : hello 0 Wed Jul 17 12:13:31 2024
# hello : hello 1 Wed Jul 17 12:13:31 2024
# end Wed Jul 17 12:13:33 2024
# hello : hello 2 Wed Jul 17 12:13:33 2024
# end Wed Jul 17 12:13:33 2024
# end Wed Jul 17 12:13:35 2024
# ***: donehello 0
# ***: donehello 1
# ***: donehello 2
# All end--