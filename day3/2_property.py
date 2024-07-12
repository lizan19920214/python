# 使用@property包装器来包装getter和setter方法，使得对属性的访问既安全又方便
# @property 的语法格式如下：
# 
# @property
# def 方法名(self)
    # 代码块
class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 12)
    person.play()
    # 直接使用 对象.函数名 = value的方式可以直接调用函数并传参
    person.age = 22
    # 因为使用了property访问器我们可以直接用 对象.函数名的方式来访问，不需要加()
    # print(person.name())
    print(person.name)
    # 普通函数还是要使用对象.函数名()来访问
    person.play()
    # person.name = '白元芳'  # AttributeError: can't set attribute


if __name__ == '__main__':
    main()