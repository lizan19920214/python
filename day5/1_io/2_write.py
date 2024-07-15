# 要将文本信息写入文件文件也非常简单，在使用open函数时指定好文件名并将文件模式设置为'w'即可。注意如果需要对文件内容进行追加式写入，
# 应该将模式设置为'a'。如果要写入的文件不存在会自动创建文件而不是引发异常。

# 覆盖写 w
def write1():
    f = open('a.txt', 'w', encoding='utf-8')
    f.write("hello world")
    f.close()

# 追加写 a
def write2():
    f = open('b.txt', 'a', encoding='utf-8')
    f.write("hello world\n")
    f.close()

# 二进制文件，下面的代码实现了复制图片文件的功能。
def write3():
    try:
        # 按照二进制读取图片
        with open('item1.png', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        # 按照二进制打开文件，用上面的二进制数据重新写入
        with open('item2.png', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开.')
    except IOError as e:
        print('读写文件时出现错误.')
    print('程序执行结束.')

if __name__ == '__main__':
    write1()
    print("write1")
    write2()
    print("write2")
    write3()
    print("write3")