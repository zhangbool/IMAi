##### 面向对象高级

###### 1，使用__slots__限制动态添加的属性或者方法
#* 注意slots只对当前类起作用，对子类是不起作用的
''''''
import traceback

from types import MethodType

class MyClass(object):
    __slots__ = ["name", "set_name"]#这里是为了限制可以动态添加的属性或者方法，如果没有，表明可以动态的添加任意属性和方法

def set_name(self, name):
    self.name = name

cls = MyClass()
#在python里面，居然不需要任何的提前指定就可以进行赋值某个位置的属性或者说变量
cls.name = "Ivanl"
print(cls.name)
#这里动态的进行添加某个方法给指定的对象
cls.set_name = MethodType(set_name, cls)
cls.set_name("zhangdanfeng")
print(cls.name)

# 因为上面用slots进行限制，所以下面会抛出异常
# try:
#     cls.age = 20
#     print(cls.age)
# except AttributeError:
#     print("该属性不能被添加，因为用了__slots__")
#     traceback.print_exc()
''''''

###### 2，property
''''''
class Student:

    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("not int")
        elif(value < 0 or value > 100):
            raise ValueError("not between 0~100")
        self._score = value

    @property
    def num(self):
        return self.num

stu01 = Student()
stu01.score = 75
print(stu01.score)
#stu01.score = "zhangdangfeng" #这里会抛出异常，因为我们在setter方法中进行了限制
#stu01.num = 100 #这里会直接报错的，因为没有设置setter，所以只能读，不能写入
''''''




