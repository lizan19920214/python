"""
在python中，方法分为实例方法、类方法、静态方法
"""

# 实例方法
# ！！！！！实例方法第一个参数为self
# 当使用ik1.printd()调用实例方法时，实例ik1会传递给self参数，这样self参数就可以引用当前正在调用实例方法的实例。
class Kls1(object):
    def __init__(self, data):
        self.data = data

    def printd(self):
        print(self.data)


ik1 = Kls1('leo')
ik2 = Kls1('lee')

ik1.printd()
ik2.printd()
print("#" * 40)

#类方法 采用装饰器@classmethod来定义
# ！！！！！类方法的第一个参数约定名为cls，
# 它代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方也称之为类的元数据对象），
# 通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象
# 调用方式：
# “类名.方法名”
# “对象.方法名”

"""
我们需要统计类Kls实例的个数，因此定义了一个类变量num_inst来存放实例个数。通过装饰器@classmethod的使用，
方法get_no_of_instance被定义成一个类方法。在调用类方法时，Python 会将类（class Kls）传递给cls，
这样在get_no_of_instance内部就可以引用类变量num_inst。
"""
class Kls2(object):
    num_inst = 0

    def __init__(self):
        Kls2.num_inst = Kls2.num_inst + 1

    @classmethod
    def get_no_of_instance(cls):
        return cls.num_inst


ik3 = Kls2()
ik4 = Kls2()

print(ik3.get_no_of_instance()) #2
print(Kls2.get_no_of_instance()) #2
print("#" * 40)

# ！！！！！！类方法和实例方法区别
# 类方法第一个形参是cls，实例方法第一个形参是self
# 类方法调用不需要创建对象，实例方法调用必须要创建对象
# 类方法可以访问类中的类属性但不可以访问实例属性，访问类属性也是使用 “cls.” 的形式
# 实例方法可以访问类中的类属性和实例属性，使用 “self.” 的形式



# 在开发中，我们常常需要定义一些方法，这些方法跟类有关，但在实现时并不需要引用类或者实例，
# 例如，我们使用三条边来构建三角形，并求其周长和面积，但是传入的三条边不一定能构建成三角形
# 这个校验函数和三角形对象无关，因为是属于前置校验，因此我们可以将其定义为静态方法
# Python 使用装饰器@staticmethod来定义一个静态方法。
from math import sqrt

class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))


def main():
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
        # print(Triangle.perimeter(t))
        print(t.area())
        # print(Triangle.area(t))
    else:
        print('无法构成三角形.')

if __name__ == '__main__':
    main()