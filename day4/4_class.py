# 组合关系
# 将一个类的对象封装到另一个类的对象的属性中，就叫组合
#     一对一关系
#     一对多关系

# 一对一
class BigB:
    # girl_friend默认为空
    def __init__(self, name, girl_friend=None):
        self.name = name
        self.girl_friend = girl_friend
    def eat(self):
        if self.girl_friend:
            print(f'{self.name}带着他的女朋友{self.girl_friend.name}去吃饭')
        else:
            print('单身狗，吃狗粮！')
    def movie(self):
        if self.girl_friend:
            print(f'{self.name}带着他的女朋友{self.girl_friend.name}去看电影')
        else:
            print('单身狗不配看电影！')
            
class Girl:
    def __init__(self, name):
        self.name = name
    
bao = BigB('宝元')
friend = Girl('唐艺昕')
bao.eat()
bao.movie()
# 将friend对象封装到bao对象的girl_friend属性中
bao.girl_friend = friend
bao.eat()
bao.movie()

print("==============================================")
# 一对多组合
# 有一个男孩类和一个女孩类，男孩类中包含多个女孩类的对象
class Boy:
    def __init__(self, name):
        self.name = name
        self.girl_f = []
    def ba_mei(self, girl):
        self.girl_f.append(girl)
    def happy(self):
        for i in self.girl_f:
            i.play()
class Girl:
    def __init__(self, name):
        self.name = name
    def play(self):
        print(f'{self.name}陪你一起玩~o(=•ェ•=)m')
        
xiaoqiang = Boy('小强')

xiaohong = Girl('小红')
xiaoli = Girl('小丽')
xiaofei = Girl('小菲')

xiaoqiang.ba_mei(xiaohong)
xiaoqiang.ba_mei(xiaoli)
xiaoqiang.ba_mei(xiaofei)

xiaoqiang.happy()
