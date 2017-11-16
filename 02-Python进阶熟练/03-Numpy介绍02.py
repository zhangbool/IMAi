###### Numpy介绍第二课

#* 1, 数组运算
''''''
import numpy as np
from numpy.random.mtrand import randn

arr01 = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr01)
print(arr01*arr01)#相当于每个平方
print(arr01-arr01)#全部会变成零
print(1/arr01)#其实都是会把运算带进数组，对每个值进行运算
print(arr01*0.5)

''''''

#* 2，一位数组的索引与切片, 跟python本身的切片没有差别
''''''
a = np.arange(10)
# print(a)
print(a[3:6])
print(a[::-1])
print(a[::2])
''''''

#* 3,多维数组的切片与索引
''''''
print("3,多维数组的切片与索引")
mArr01 = np.arange(24).reshape(2,3,4)#这个代表是二维数组中是三维数组， 三维数组中又是四维数组
print(mArr01.shape)
print(mArr01)
print(mArr01[0,0,0]) #代表第一个二维数组中的第一个三维数组中的第一个值
print(mArr01[1,2,3])
print(mArr01[:,0,0])#第一维度任意，其他纬度都取第一个
print(mArr01[0,:,:])#只取第一维度，忽略其他纬度
print(mArr01[0,...])#同上，只取第一维度，忽略其他纬度
print(mArr01[0,0])#这里是省略第三个纬度（可以用冒号，也可以直接不写）
print(mArr01[0,0,::2])#这里是取第一维度中的第一个纬度，但不是取其中的全部，而是以步幅为2进行取
print(mArr01[...,1])#忽略第一维度和第二维度， 取第三维度中的第二列
print(mArr01[:,0])#忽略第一维度和第三维度，取第二维度的第一个中的所有
print(mArr01[0,:,1])#忽略第二维度,也就是1,5,9
print(mArr01[0,:,-1])
print(mArr01[0,::-1,-1])#反向，这个不懂为什么是两个：
# 剩下几个不行了，看不懂了，之后有需要再回来看
''''''

#* 4,布尔型索引
''''''
names = np.array(["zhangdanfeng", "ivanl", "jack", "kkkk", "wang", "yangyizhe", "zhangzhang"])
data = randn(7,4)
print(names)
print(data)
print("\n")
print(data[names=="jack"])#其实这里应该是这样，先找到ivanl对应的序号，然后用这个序号去取出data中的数据
print("-------------------")
print(data[names=="jack", 2:])#取第三个以及之后的
print(data[names=="jack", 2])#取第三个
print(data[(names=="ivanl") | (names=="jack")])#取两个的并集
''''''

#* 5,花式索引
''''''
# 这个暂时没看，跳过，之后再回来看

''''''

#* 6，数组转置
''''''
print("数组转置")
arr02 = np.arange(15).reshape(3,5)
print(arr02)
print(arr02.T)
print("改变数组的维度")
#一维数组转换成高维数组
arr03 = np.arange(24).reshape(2,3,4)
print(arr03)
#高维数组转换成低维数组, 用ravel，或者faltten
print(arr03.ravel())
print(arr03.flatten())
arr03.shape = (6,4)
print(arr03)
arr03.resize(2,12)#这个和ravel和flatten不同的是，这个会直接更改元数组
print(arr03)

''''''