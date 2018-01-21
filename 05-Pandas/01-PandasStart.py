import pandas as pd
import numpy as np
import matplotlib as plt

print("pandas的Series类型")
s = pd.Series([1, 3, 4, 5, np.nan, 7, 8])
print(s)

print("pandas的date序列类型")
dates = pd.date_range('20180101', periods=6)
print(dates)

print("pandas的DateFrame类型")
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

# print(np.random.rand(100))

# list = np.random.rand(100)
# for i in list:
#     print("00000000------------------------0000000")
#     print(i)

print("---从字典转成np类型---")
df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' }, index=list("2222"), columns=list("AADAAF"))
print(df2)
print("---df2的类型---")
print(df2.dtypes)
print("---df数据---")
print(df)
print("---df的头部数据---")
print(df.head(1))
print("---df的尾部数据---")
print(df.tail(2))
print("---df的索引---")
print(df.index)
print("---df的列名---")
print(df.columns)
print("---df的值---")
print(df.values)
print("---df的描述信息---")
print(df.describe())
print("---df的转置---")
print(df.T)
df03 = df.T
print("---df转置后的列名---")
print(df03.columns)

# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
# ts = ts.cumsum()
# print(ts.plot())



