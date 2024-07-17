import time
from multiprocessing import Pool


def run(fn):
    # fn: 函数参数是数据列表的一个元素
    time.sleep(1)
    print(fn)


if __name__ == "__main__":
    testFL = [1, 2, 3, 4, 5, 6]
    print('顺序执行:')  # 顺序执行(也就是串行执行，单进程)
    s = time.time()
    for fn in testFL:
        run(fn)
    t1 = time.time()
    print("顺序执行时间：", int(t1 - s))

    print('concurrent:')  # 创建多个进程，并行执行
    pool = Pool(3)  # 创建拥有3个进程数量的进程池
    # testFL:要处理的数据列表，run：处理testFL列表中数据的函数
    for fn in testFL:
        pool.apply(run, (fn,))
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出
    t2 = time.time()
    print("并行执行时间：", int(t2 - t1))

    print('concurrent_sync:')  # 创建多个进程，并行执行
    t1 = time.time()
    pool = Pool(3)  # 创建拥有3个进程数量的进程池
    # testFL:要处理的数据列表，run：处理testFL列表中数据的函数
    for fn in testFL:
        pool.apply_async(run, (fn,))
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出
    t2 = time.time()
    print("并行执行时间：", int(t2 - t1))


# 可见，使用apply()方法，并行执行和顺序执行用时相同，经过试验，进程数目增大也不会减少并行执行的时间
# 原因：以阻塞的形式产生进程任务，生成1个任务进程并等它执行完出池，第2个进程才会进池，主进程一直阻塞等待，每次只执行1个进程任务
# 使用apply_async()方法，并行执行时间与使用map()、map_async()方法相同
# ！！！！！使用apply()和apply_async()方法时，第2个参数只能传入元祖，传入列表进程不会被执行

# 顺序执行:
# 1
# 2
# 3
# 4
# 5
# 6
# 顺序执行时间： 6
# concurrent:
# 1
# 2
# 3
# 4
# 5
# 6
# 并行执行时间： 6
# concurrent_sync:
# 2
# 3
# 1
# 5
# 4
# 6
# 并行执行时间： 2