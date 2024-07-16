"""
队列
"""
from multiprocessing import Process, Queue
 
def queue_insert(q: Queue, l: list):
    """
    队列插入数据
    :param l:
    :return:
    """
    for item in l:
        print(f'开始制作:{item}')
        q.put(item)
 
 
def queue_pop(q: Queue):
    """
    队列弹出数据,并进行处理
    :param q:
    :return:
    """
    while True:
        item = q.get(True)
        print(f'开始吃:{item}')
 
 
if __name__ == '__main__':
    q = Queue()
    p_product = Process(target=queue_insert, args=(q, ['饺子', '稀饭', '面皮']))
    p_product1 = Process(target=queue_insert, args=(q, ['苹果', '车厘子', '香蕉']))
    p_consumer = Process(target=queue_pop, args=(q,))
    p_consumer1 = Process(target=queue_pop, args=(q,))
    p_product.start()
    p_consumer.start()
    p_product1.start()
    p_consumer1.start()
    p_product.join()
    p_product1.join()
    p_consumer.join()
    p_consumer1.join()
    # p_consumer.terminate()
    # p_consumer1.terminate()