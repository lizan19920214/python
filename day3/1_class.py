# 在Python中可以使用class关键字定义类，然后在类中通过之前学习过的函数来定义方法，这样就可以将对象的动态特征描述出来，代码如下所示。
# 类定义
# ！！！！注意 python中只有公有和私用两种访问权限
# 如果希望属性或者函数是私有的，在给属性或者函数命名时可以用两个下划线作为开头
# 私有属性：__属性名
# 不过python并没有从语法上严格保证私有属性或方法的私密性，它只是给私有的属性和方法换了一个名字来妨碍对它们的访问，
#       事实上如果你知道更换名字的规则仍然可以访问到它们


class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        # name是私用属性
        self.__name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.__name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.__name)
        else:
            print('%s正在观看大电影.' % self.__name)
    # bar是私有方法
    def __bar(self):
        print('这是一个私有方法')

def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('骆昊', 38)
    # 给对象发study消息
    stu1.study('Python程序设计')
    # 给对象发watch_av消息
    stu1.watch_movie()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_movie()
    # 访问私用属性和方法会报错
    # print(stu2.__name)
    # stu2.__bar()
    # 不严格的私有限制，在知道名字的情况下依然可以强制访问
    print(stu2._Student__name)
    stu2._Student__bar()



if __name__ == '__main__':
    main()