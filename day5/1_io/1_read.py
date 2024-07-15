#在Python中实现文件的读写操作其实非常简单，通过Python内置的open函数，
# 我们可以指定文件名、操作模式、编码信息等来获得操作文件的对象，接下来就可以对文件进行读写操作了
# 操作模式	具体含义
# 'r'	读取 （默认）
# 'w'	写入（会先截断之前的内容）
# 'x'	写入，如果文件已经存在会产生异常
# 'a'	追加，将内容写入到已有文件的末尾
# 'b'	二进制模式
# 't'	文本模式（默认）
# '+'	更新（既可以读又可以写）

# 在Python中，我们可以将那些在运行时可能会出现状况的代码放在try代码块中，
# 在try代码块的后面可以跟上一个或多个except来捕获可能出现的异常状况。
def read1():
    f = None
    try:
        f = open('test.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()

# 除了使用文件对象的read方法读取文件之外，还可以使用for-in循环逐行读取或者用readlines方法将文件按行读取到一个列表容器中
import time
def read2():
    # 一次性读取整个文件内容
    with open('test.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    print("\n")
    # 通过for-in循环逐行读取
    with open('test.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print("\n")

    # 读取文件按行读取到列表中
    with open('test.txt') as f:
        lines = f.readlines()
    print(lines)



if __name__ == '__main__':
    read1()
    print("===================================")
    read2()
    print("===================================")