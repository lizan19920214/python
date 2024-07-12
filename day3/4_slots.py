# Python是一门动态语言。通常，动态语言允许我们在程序运行时给对象绑定新的属性或方法，
#       当然也可以对已经绑定的属性和方法进行解绑定。但是如果我们需要限定自定义类型的对象只能绑定某些属性，
#       可以通过在类中定义__slots__变量来进行限定。需要注意的是__slots__的限定只对当前类的对象生效，对子类并不起任何作用
class Student(object):
    pass

s = Student()
s.name = 'Michael' # 动态给实例绑定一个属性
print(s.name)

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
print(s.age) # 测试结果

# 给A对象绑定的方法，对同类的B对象是不生效的
s2 = Student() # 创建新的实例
# s2.set_age(25) # 尝试调用方法 error

# 给所有类对象绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score
#所有对象都可以使用
s.set_score(100)
print(s.score)
s2.set_score(99)
print(s2.score)

# 而如果我们不想类对象随便绑定方法的话，可以使用__slots__加以限制
class Person(object):
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 22)
    person.play()
    person._gender = '男'
    # 这里给对象添加新绑定一个属性就会报错
    # person._is_gay = True

main()