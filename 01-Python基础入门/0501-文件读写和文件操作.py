


##### 文件读写的三种方式

###### 1，read、readline、readlines
#* 1.1， read()  将文本文件所有的内容读到一个字符串中
#* 1.2， readline() 是一行一行的读
#* 1.3， readlines() 是将文本文件的所有内容读到一个list中，文本文件的每一行都是list的一个元素，优点是：readlines()可以再读行过程中跳过特定行
''''''
file01 = open("resources/file01.txt")#默认是读取权限
file02 = open("resources/file02.txt", "w")#这里打开的时候设置为写入权限
while True:
    line = file01.readline()#读取file01的一行数据
    file02.write("zhangdanfeng---line---" + line)#file02已经开启了写入权限，所以可以写入,也就是把file01的文件拼接都写入到file02中
    if not line:
        break
file01.close()
file02.close()
''''''

###### 2,文件迭代器，用for循环
''''''
file03 = open("resources/file01.txt")
for line in file03:
    print(line)
file03.close()
''''''

###### 3,文件上下文管理器，也就是with open方式
#* with opne 是自带文件关闭功能的，所以使用完毕之后不需要关闭文件
''''''
print("-----------------")
with open("resources/file02.txt") as f:
    #貌似while方法是不行的，因为你并不知道什么时候会停止
    #while True:
    #    print(f.readline())
    for line in f:
        print(line)

''''''

##### 文件操作相关
''''''
import os
print(os.name) #nt代表windows系统，posix代表nix家族

#获取当前目录
print(os.getcwd())

#改变当前工作目录
# os.chdir("/home/ivanl001/IMPython/01-基础/day19")
# print(os.getcwd())

#当前路径，也就是一个点
print(os.curdir)
#父目录路径，两个点
print(os.pardir)

#在当前工作路径生成文件夹，可递归生成
# os.makedirs("ivanl001/ivanl002/ivanl003")

#这个方法只能删除空文件夹,而且会向上递归删除空文件夹
#如果直接要删除的文件夹中有内容，会报错
# os.removedirs("ivanl001")

#生成单个文件夹,这里是不能用斜杠分割表示要生成多个文件夹,
# 除非上级文件夹已经生成
# os.mkdir("ivanl003/ivanl001")

#这里只能删除指定到文件夹，不能向上递归删除其他空的文件夹
# os.rmdir("ivanl003")

#列出所有文件夹,r代表raw，表示后面的字符串就是原生的，不需要转意的字符
#print(os.listdir(r"/home/ivanl001"))

# 删除指定文件,文件夹必须存在，如果没有是会报错的
#os.remove("ivanl001/zhang.text")

#重命名，文件或文件夹都可以，不会更改文件内容,注意必须要有该文件才能重命名，否则会报错
#os.rename("ivanl001.txt","zhang.txt")
#os.rename("ivanl002","ivanl0002")


#获取文件信息，包括文件大小，创建时间，可以简单理解为文件属性
#st_atime是最后一次被人访问的时间，st_mtime是被修改的时间
#st_size是文件大小
#print(os.stat("./zhang.txt"))

#就是斜杠，在不同的系统下是不同的斜杠，也就是分隔符
#sep就是seperator
#print(os.sep)

#环境变量的分隔符，linux是:   windows是;
#print(os.pathsep)

#print("--------------------")
#执行命令
#print(os.system("pwd"))
#print("--------------------")

#获取环境变量，比较多，所以先注释
# print(os.environ)

#通过相对路径获取绝对路径
#print(os.path.abspath("../"))

#把文件名和之间到路径分开，转成字符串返回
#print(os.path.split("/home/ivanl001/IMPython/01-基础/day19/zhang.txt"))

#父级文件夹名字,其实就是从最后一个/来判断的，参数里面必须有父路径才行呢
#print(os.path.dirname("./zhang.txt"))
#print(os.path.dirname("/home/ivanl001/IMPython/01-基础/day19/zhang.txt"))

#判断路径是否存在
#print(os.path.exists("/home"))
''''''

##### 序列化和反序列化
#* dict对象的序列化
''''''
import pickle
#dict对象的序列化和反序列化
dict01 = dict(name="ivanl001", age=20, score=100)
str01 = pickle.dumps(dict01)#序列化后的字符串是不能识别的
print(str01)

file04 = open("resources/file03.txt", "wb")
pickle.dump(dict01, file04)
file04.close()

file05 = open("resources/file03.txt", "rb")
dict02 = pickle.load(file05)
print(dict02)
''''''

#* json对象的序列化和反序列化
''''''
import json

dict03 = dict(name="ivanl001001", age=10, num="10120945",keyword="Ivan is the king of world!")
jsonStr = json.dumps(dict03)
print(jsonStr)
#反序列化
dict04 = json.loads(jsonStr)
print(dict04)#看不出大的差别，貌似之前的双引号变成了单引号
''''''
