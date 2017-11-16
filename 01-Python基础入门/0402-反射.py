###### 反射
''''''
class Foo:
    def __init__(self, name, age, num):
        print("ivanl001-------")
        self.name = name
        self.age = age
        self.num = num
    def showName(self):
        return self.name

foo = Foo("ivanl001", 24, 100)
print(foo.__dict__)
print(foo.__dict__["name"])

name = foo.showName()
print(name)

#1,首先用反射获取方法
name01 = getattr(foo, "showName")
#然后执行方法即可
print(name01())

#好像在模块开发中才能这么使用
# cls = getattr(foo, "Foo ")
# print(cls)


#2,反射判断是否有某方法
print(hasattr(foo, "showName"))
print(hasattr(foo, "zhang"))

#3,反射设置，反正也搞不明白具体是字段还是属性了
setattr(foo, "item01", "Ivan is the king of world!")
print(getattr(foo,"item01"))

#4，反射删除「」「」
delattr(foo, "showName")
#foo.showName()#前面一旦删除后面如果调用就会报错

''''''
