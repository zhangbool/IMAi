
##### Numpy的一个简单的例子

#* 1， 首先用python的range代码实现一下
#* 这是什么玩意儿，为啥numpy比元python代码还要慢！！！！！！
#* 为啥一会又好了，到底什么毛病嘛
''''''
import sys
from datetime import datetime
import numpy as np

size = 10000

startTime = datetime.now()
def sum01(n):
    a = range(n)
    b = range(n)
    c = []
    for i in range(len(a)):
        x = i**2
        y = i**3
        c.append(x+y)
    return c
sum01(size)
endTime = datetime.now()
print("python默认执行时间差是："+str((endTime-startTime).microseconds))
''''''

#* 2, 然后用Numpy来实现一下
''''''
startTime = datetime.now()
def numpySum(n):
    a = np.arange(n)**2
    b = np.arange(n)**3
    c = a+b
    return c
numpySum(size)
endTime = datetime.now()
print("numpy执行时间差是："+str((endTime-startTime).microseconds))

''''''

#* 3, numpy创建一维数组
''''''
arr01 = np.arange(5)
print(arr01)
print(arr01.dtype)
print(arr01.shape)

''''''


#* 4, numpy创建多维数组
''''''
mArr = np.array([np.arange(3), np.arange(3)])
print(mArr)
print(mArr.dtype)
print(mArr.shape)
''''''

#* 5, numpy创建多维数组快捷方式
''''''
print(np.zeros(4))
print(np.zeros((3,6)))#注意括号个数
print(np.empty((2,3,2)))#注意括号个数
''''''

#* 6，多维数组的操作
''''''
mArr01 = np.array([[1,2],[3,4]])
print(mArr01)
print(mArr01[0,0])
print(mArr01[1,1])

''''''

#* 6,numpy的数据类型
''''''
print(np.float64(23))
print(np.int8(34.3))
print(np.bool(23))
print(np.arange(3, dtype=np.float64))
''''''

#* 7,numpy的数据类型转换
''''''
arr02 = np.array([1,2,3,4,5,6,7,8])
print(arr02.dtype)
floatArr02 = arr02.astype(np.float64)
print(floatArr02.dtype)
''''''


#* 8, 创建自定义数据类型
''''''
t = np.dtype([("name", np.str_, 40), ("numitems", np.int32), ("price", np.float32)])
print(t)
print(t["name"])
item = np.array([("Meaning of life DVD", 42, 3.14), ("Butter", 13, 2.72)], dtype=t)
print(item)
''''''


