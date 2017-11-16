###### 常用的数据分析库
#* 1,常用的数据分析库有Numpy， Scipy， Pandas， matplotlib

''''''
# numpy是python一个处理科学计算的包
import numpy as np
imArr = np.arange(10)
print(imArr)
print(imArr ** 2)


#scipy也是一个数学统计运算相关的包， 矩阵？
from scipy import linalg
a = np.array([[1,2], [3,4]])
print(a)
#linalg.det(a)#不知道为什么，这里并不可行


#panda, 矩阵？
import pandas as pd
s = pd.Series([1,3,5,np.nan, 6,8])
print(s)
dates = pd.date_range("20171010", periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)

print("展示第一行信息")
print(df.head(1))
print("展示后两行信息")
print(df.tail(2))
print("展示数据的一些信息")
print(df.describe())
print("行和列进行转置")
print(df.T)
print("排序进行展示")
print(df.sort_values(by="C"))
''''''


#* 2, 常用的数据分析高级库：nltk， igraph（主要是一个绘图模块）， scikit-learn(机器学习的一个模块)























