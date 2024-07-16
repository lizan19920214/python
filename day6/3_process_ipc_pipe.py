"""
管道：

"""
from multiprocessing import Process, Pipe
 
def pipe_frontend(p: Pipe, l: list):
    """
    餐厅前台通过管道发送/接收数据
    前台负责 发送制作任务,接收 制作完成通知
    :param l:
    :return:
    """
    for item in l:
        print(f'开始发送制作:{item} 任务')
        # 发送
        p.send(item)
    while True:
        # 接收
        item = p.recv()
        print(item, '可以端给食客享用')
 
 
def pipe_backend(p: Pipe):
    """
    餐厅后台通过管道接收,进行处理后,发送数据
    后台负责 接收制作任务,并在制作完成后,发送制作完成通知
    :param p:
    :return:
    """
    while True:
        # 接收
        item = p.recv()
        print(f'开始接收:{item}任务,并进行制作')
        _send = f'制作{item}完成'
        # 发送
        p.send(_send)
        print(f'{_send},推送此消息到管道')
 
 
if __name__ == '__main__':
    # 参数 duplex 值为True表示 全双工模式(两头均可发送接收),False表示 单工模式(p[1]只能发送,p[0]只能接收)
    p = Pipe(True)
    p_product = Process(target=pipe_frontend, args=(p[0], ['饺子']))
    p_consumer = Process(target=pipe_backend, args=(p[1],))
    p_product.start()
    p_consumer.start()
    p_product.join()
    p_consumer.join()
    # p_consumer.terminate()