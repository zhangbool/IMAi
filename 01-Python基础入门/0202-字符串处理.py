import string

# 1,去除空格
s = "  zhang  is king  !  s  "
print(s)
print(s.strip())
print(s.lstrip()+"zhang")
print(s.rstrip()+"zhang")
#字符串本身是不被修改的
print(s)

#2，连接字符串
s1 = "zhangdanfeng"
s2 = "is ivanl001"
print(s1+s2)

#3，大小写转换
s3 = "zhangdanfeng"
print(s3.upper())
#首字母大写
print(s3.capitalize())
s4 = "KING"
print(s4.lower())

#4,位置比较
s5 = "zhang is ivanl, and ivan is the king too"
print(s5.index("ivanl"))#打印出其开始位置，如果没有对应字符会报错，需要手动trycatch
print(s5.index("king"))
print(s5.index("king") > s5.index("ivanl"))#通过这种方式比较其位置, 可以直接进行比较

#5，分割和链接
s6 = '''ivan is the king !
And Jack love rose, 
and who do you think you are'''
print(s6.split("\n"))#这个是分割，根据指定的规则进行分割
print(s6.splitlines())#这个是根据分行进行分割
s7 = s6.split("\n")
print("----".join(s7))#把需要的字符串给拼接回去

#6，常用的判断，如开头匹配,结尾匹配，数字匹配，字母匹配，空格匹配等
s8 = "Ivan is a good boy "
print(s8.startswith("Ivan"))
print(s8.endswith("boy"))#注意因为后面没有空格，所以匹配后是false
s9 = "123abc"
print(s9.isalnum())#只要是阿拉伯数字或者字母都可以
s10 = "123"
s11 = "zhangdanfeng"
print(s10.isdigit())#注意这里是判断字符串里面的是否是数字，非字符串型的数字是false
print(s11.isalpha())
print("  ".isspace())
print("zhang".islower())
print("zha".isupper())
print("Hello World".istitle())

#7, 数字和字符串相互转换
print(str(1000))
print(float("324"))
print(int("2342.4"))
#还可以进行进制转换，这里不再探究











