
###### 1, 函数默认参数
''''''
def func(x, y=200):
    # print(x+y)
    return x+y
print(func(100,100))#如果赋值，则会覆盖
print(func(100))#如果没有进行赋值，那么会使用默认参数
''''''

###### 2,可变参数，可能会传递不固定个数的参数
#* 2.1, 参数为元组
''''''
def func01(name, *num):
    print(type(num))#这里可以看到其实是传递的一个元组类型
    return num
print(func01("zhangdanfeng", 1, 2, 3, 4, 5))
''''''
#* 2.2,参数为字典
''''''
def func02(name, **params):
    print(type(params))
    if params['keyword'] == "good":
        print("wakawaka, wakawaka")
    return params
print(func02("ivanl001", num=100, keyword="good"))
''''''

###### 3,加和举例和斐波那契举例
#* 3.1, 加和
''''''
def sum(n):
    if n<0:
        raise ValueError
    elif n <= 1:
        return 1
    else:
        return n + sum(n-1)

# sum(100)
print(sum(100))
''''''

#* 3.2, 斐波那契数列
''''''
def fib(n):
    if n<1:
        raise ValueError
    elif n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(10))

''''''



