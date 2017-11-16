##### 组合数组


#* 组合数组
''''''
import numpy as np

arr01 = np.arange(9).reshape(3,3)
print(arr01)

print("---------------")
arr02 = arr01 * 2
print(arr02)
print("---------------")

print(np.hstack((arr01, arr02)))#这个是进行水平组合
print(np.vstack((arr01, arr02)))#这个是进行垂直组合
print(np.concatenate((arr01, arr02), axis=1)) #axis为1时候为水平组合，非1的时候为垂直组合
print("深度组合---deep stack")
print(np.dstack((arr01, arr02)))#原来的行编程列，然后进行两个数组的水平组合

print("-------------")
arr03 = np.arange(3)
print(arr03)
arr04 = arr03*2
print(arr04)
#下面这两个和水平组合和垂直组合结果相同
print(np.column_stack((arr03, arr04)))#按列进行组合
print(np.row_stack((arr03, arr04)))#按列进行组合

''''''

#* 分割数组
''''''
print("分割数组")
arr05 = np.arange(9).reshape(3,3)
print(arr05)
print(np.hsplit(arr05,3))#水平分割
print(np.vsplit(arr05,3))#垂直分割
print("-----")
print(np.split(arr05, 3, axis=0))#1是水平
print(np.split(arr05, 3, axis=1))#0是垂直
print("------")
print("深度分割")
arr06 = np.arange(27).reshape(3,3,3)
print(arr06)
print(np.dsplit(arr06, 3))#对于深度分割的规则还不是很清晰
''''''

#* 数组的属性
''''''
arr07 = np.arange(24).reshape(2,12)
print(arr07.ndim)#维度属性
print(arr07.size)#元素个数，也就是Item的个数
print(arr07.itemsize)#每个元素的字节数？
print(arr07.nbytes)#itemsize*size
#还有一些其他几个属性，感觉不是很有用，先过
''''''

#* 数组转换成python对象
''''''
arr08 = np.arange(12).reshape(2,2,3)
print(arr08)
print(arr08.tolist())#转换python的list
print(arr08.tostring())#转换成python的string

''''''