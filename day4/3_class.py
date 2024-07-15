# 依赖关系
# 关系指的是类对象执行某个动作的时候，需要其他类的对象来帮助完成这个操作的情况，其特点为：

# 将一个类的对象或者类名传到另一个类的方法中使用
# 此时的关系是最轻的，随时可以更换其他对象

class Person:
    def play(self, tools):
        print('我要打游戏了')
        tools.run()
class Computer:
    def run(self):
        print('电脑已经打开，DNF已经登陆')
class Phone:
    def run(self):
        print('王者荣耀已经登陆')

xiaoming = Person()
xmPhone = Phone()
hwComp = Computer()
xiaoming.play(xmPhone)
xiaoming.play(hwComp)
