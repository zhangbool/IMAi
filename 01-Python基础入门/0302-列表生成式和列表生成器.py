
###### ------------------------这种是列表生成式-----------------------------
#* 这里直接把结果返回
#* 列表生成式
''''''
a = [x for x in range(10)]
print(a)
b = [x*2 for x in range(0,20,2)]
print(b)

def ivanl(x):
    return  x*2+1
c = [ivanl(x) for x in range(10)]
print(c)
''''''

###### -------------------这种是生成器，并不会把结果返回，在next的时候才会返回--------------------
#* 生成器,第一种方式，小括号的方式
''''''
d = (x for x in range(20))
print(d.__next__())#这种好像是内置方法，忘记啦
print(d.__next__())
print(next(d))#这个是叫什么来着，也忘记啦哈哈
for i in d:
    print(i)
''''''

#* 生成器到第二种方式，yeild,每next一次执行一个yield
''''''
def foo():
    yield 0
    yield 1
    yield 2
    yield 3
    yield 4

print(foo())
g = foo()
print(next(g))
print(next(g))
print("zhangdanfeng---")
for i in g:
    print(i)


for i in [0,2,4,6]:
    print(i)
''''''


