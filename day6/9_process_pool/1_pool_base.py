"""
 Pool类可以提供指定数量的进程供用户调用，当有新的请求提交到Pool中时，如果池还没有满，就会创建一个新的进程来执行请求。
    如果池满，请求就会告知先等待，直到池中有进程结束，才会创建新的进程来执行这些请求
下面介绍一下multiprocessing 模块下的Pool类下的几个方法：
1.apply()
    函数原型：apply(func[, args=()[, kwds={}]])
    该函数用于传递不定参数，同python中的apply函数一致，主进程会被阻塞直到函数执行结束（不建议使用，并且3.x以后不再出现）

2.apply_async
    函数原型：apply_async(func[, args=()[, kwds={}[, callback=None]]])
    与apply用法一致，但它是非阻塞的且支持结果返回后进行回调

3.map()
    函数原型：map(func, iterable[, chunksize=None])
    Pool类中的map方法，与内置的map函数用法行为基本一致，它会使进程阻塞直到结果返回
    注意：虽然第二个参数是一个迭代器，但在实际使用中，必须在整个队列都就绪后，程序才会运行子进程

4.map_async()
    函数原型：map_async(func, iterable[, chunksize[, callback]])
    与map用法一致，但是它是非阻塞的

5.close()
    关闭进程池（pool），使其不再接受新的任务

6.terminal()
    结束工作进程，不再处理未处理的任务

7.join()
    主进程阻塞等待子进程的退出， join方法要在close或terminate之后使用
"""
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
    pool.map(run, testFL)
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出
    t2 = time.time()
    print("并行执行时间：", int(t2 - t1))

    print('concurrent:')  # 创建多个进程，并行执行
    t1 = time.time()
    pool = Pool(3)  # 创建拥有3个进程数量的进程池
    # testFL:要处理的数据列表，run：处理testFL列表中数据的函数
    pool.map_async(run, testFL)
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出
    t2 = time.time()
    print("并行执行时间：", int(t2 - t1))

# 1、map函数中testFL为可迭代对象--列表
# 2、如果使用Pool()，不传入参数，可以创建一个动态控制大小的进程池
# 3、从结果可以看出，map_async()和map()用时相同，目前还没有看出两者的区别
# 顺序执行:
# 1
# 2
# 3
# 4
# 5
# 6
# 顺序执行时间： 6
# concurrent:
# 2
# 1
# 3
# 5
# 6
# 4
# 并行执行时间： 2
# concurrent:
# 2
# 3
# 1
# 4
# 6
# 5
# 并行执行时间： 2