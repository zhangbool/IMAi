#python中任何类型都是一个类, 包括函数

print(type(12))
print(type(12.))
print(type("zhangdanfeng"))

print(type([1, 2, 3, 4]))
print(type((1, "zhang")))
print(type(set([1, "zhang"])))
print(type({"01":"zhangdanfeng", "02":"ivanl"}))

def printFunc(str):
    print(str)
print(type(printFunc))

#模块都有类型
import string
print(type(string))

#自定义的类也是
class Myclass(object):
    pass
#在创建实例之前，其type是type类型
print(type(Myclass))
myClass = Myclass()
#创建实例之后，其type是实际类型，也就是Myclass类型
print(type(myClass))








