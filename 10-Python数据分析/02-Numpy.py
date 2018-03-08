import numpy as np


# 创建n维数组
# '使用普通一维数组生成NumPy一维数组'
data = [1,2,3,4,5,6]
arr = np.array(data)
print(arr)
print(arr.dtype)

# '使用普通二维数组生成NumPy二维数组'
data = [[1,2,3,4,], [5,6,7,8]]
arr = np.array(data)
print(arr)
print(arr.dtype)

# 使用zeros/empty'
print(np.zeros(10))
print(np.zeros((3,6)))
print(np.empty((2,3,2)))

# '使用arrange生成连续元素'
print(np.arange(15))



# n维数组的数据类型
# '生成数组时指定数据类型'
arr = np.array([1,2,3], dtype=np.float64)
print(arr.dtype)
arr = np.array([1,2,3], dtype=np.int32)
print(arr.dtype)

# '使用astype复制数组并转换数据类型'
int_arr = np.array([1,2,3,4,5])
float_arr = int_arr.astype(np.float)
print(int_arr.dtype)
print(float_arr.dtype)

# '使用astype将float转换为int时小数部分被舍弃'
float_arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 102.1])
int_arr = float_arr.astype(dtype=np.int)
print(float_arr)
print(int_arr)

# '使用astype把字符串转换为数组，如果失败抛出异常。'
# 好像不会抛出异常
str_arr = np.array(['1.24', '-9.6', '432'], dtype=np.string_)
print(str_arr)
float_arr = str_arr.astype(dtype=np.float)
print(float_arr)

# 'astype使用其它数组的数据类型作为参数'
int_arr = np.arange(10)
print(int_arr)
float_arr = np.array([.33, .234, .34, 1.22, .5], dtype=np.float64)
print(float_arr)
print(int_arr.astype(float_arr.dtype))
print(int_arr) #数组本身还是不变的



# n维数组的运算
arr = np.array([[1.0, 2.0, 3.0], [4, 5, 7]])
print(arr*arr)
print(arr-arr)
print(1/arr)
print(arr*0.5)




















