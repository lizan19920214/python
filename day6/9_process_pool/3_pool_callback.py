from multiprocessing import Pool
import time


def fun_01(i):
    time.sleep(2)
    print('start_time:', time.ctime())
    return i + 100


def fun_02(arg):
    print('end_time:', arg, time.ctime())


if __name__ == '__main__':
    pool = Pool(3)
    for i in range(4):
        pool.apply_async(func=fun_01, args=(i,), callback=fun_02)  # fun_02的入参为fun_01的返回值
        # pool.apply_async(func=fun_01, args=(i,))
    pool.close()
    pool.join()
    print('done')
    
# map_async()方法callback参数的用法与apply_async()相同
# start_time: Wed Jul 17 12:05:33 2024
# start_time: Wed Jul 17 12:05:33 2024
# start_time: Wed Jul 17 12:05:33 2024
# end_time: 100 Wed Jul 17 12:05:33 2024
# end_time: 101 Wed Jul 17 12:05:33 2024
# end_time: 102 Wed Jul 17 12:05:33 2024
# start_time: Wed Jul 17 12:05:36 2024
# end_time: 103 Wed Jul 17 12:05:36 2024
# done