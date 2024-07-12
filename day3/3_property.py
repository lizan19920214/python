# 使用property进行托管
# 以下对property的应用进行详细的描述。事实上，通过查看property函数的定义，可以发现其输入变量一共有四个属性：
# 
# class property(fget=None, fset=None, fdel=None, doc=None)
# fget —— 获取属性值的函数。
# fset —— 设置属性值的函数。
# fdel —— 删除属性值函数。
# doc —— property 属性的文档字符串，如果没有给出 doc，则该 property 将拷贝 fget 的文档字符串（如果存在）。
# 返回值：
# property 属性。


class C:
    def __init__(self):
        self._x = None
 
    def getx(self):          # 定义一个方法 getx() 用来访问 _x
        return self._x
 
    def setx(self, value):   # 定义一个方法 setx() 用来设置 _x
        self._x = value
 
    def delx(self):          # 定义一个方法 delx() 用来删除 _x
        del self._x
        print("完成 _x 或 x 的删除！")
 
    x = property(
    getx, 
    setx, 
    delx, 
    "doc：\nx 是一个托管属性"
    )  # 根据 property() 函数的特点创建一个托管属性 x

c = C()                # 创建一个实例对象 c
c.x = "testName"       # 实例调用托管属性 x，对 x 赋值就是调用 setx() 方法
print(c.x)             # 实例调用托管属性 x，打印 x 就是调用 getx() 方法
print(C.x.__doc__)     # 类调用托管属性 x，调用 __doc__ 打印 x 的文档字符串
del c.x                # 删除托管属性 x，就是调用 delx() 方法

print("======================================")

class D:
    def __init__(self):
        self.score = 85
  
    def get_score(self):
        if self.score < 60:
            return "不及格！"
        else:
            return self.score
  
    def set_score(self, value):
        if 0 <= value <= 100:
            self.score = value
        else:
            print(f"输入的值 {value} 超出范围 0~100 ！")
  
    def del_score(self):
        del self.score
        print("完成 score 属性的删除！")
  
    score_x = property(fget=get_score, fset=set_score, fdel=del_score, doc="score_x 是 score 的托管属性。")
  
  
d = D()
d.score_x = 45          # 直接使用实例对象调用 score_x 进行赋值，背后还是调用了方法实现了过滤
print(d.score_x)        # 获取 score_x 的值
del d.score_x           # 删除 score