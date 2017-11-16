#换了老师，讲的很烂，所以就不练习了， 后面反射的东西是从之前的学习笔记中拷贝过来的


class Dog():
    def __init__(self, name, age):
        self.age = age
        self.name = name


dog = Dog("ivanl001", 20)
print(dog.name)
print(dog.age)

dog.name = "zhangdanfeng"
print(dog.name)