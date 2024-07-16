"""
共享内存
使用 multiprocessing.Manager中的list,dict实现
"""
from multiprocessing import Process, Manager
 
 
def insert(d, l):
    """
    共享数据新增 进程
    :param d:
    :param l:
    :return:
    """
    for item in range(1, 10):
        print('新增 list,dict', item)
        d[item] = item
        l.append(item)
 
 
def pop(d: dict, l: list):
    """
    共享数据删除 进程
    :param d:
    :param l:
    :return:
    """
    while True:
        if len(d.keys()):
            for k in list(d.keys()):
                print('删除_dict的', k, d[k])
                del d[k]
        if len(l):
            rs = l.pop()
            print('删除list', rs)
 
 
if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list()
 
        p = Process(target=insert, args=(d, l))
        p1 = Process(target=pop, args=(d, l))
        p.start()
        p1.start()
        p.join()
        p1.join()
        # p1.terminate()