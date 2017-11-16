
###首先理解一下数组和list：
    #* 1，数组就是一块连续的内存空间，是没有方法或者属性的
    #* 2，list则是一个对象，对象可以拥有自己的方法属性等

###### list，有序可重复
''''''
list01 = [1,2,3,"zhang",[2,4,5], {"name":"ivanl", "age":10}]
print(type(list))
print(type(list01))
#1,访问元素
print(list01[-1])#python可以倒着数
#2,查找元素位置
print(list01.index("zhang"))
#3,添加元素
list01.append("zhang001")#追加一个元素
list01.extend([2,"kkk",0])#追加一个数组中的每个元素
del list01[-1] #删掉最后一个元素
#4,判断是否为空
if list01 != None:
    print("+++++++++++++++++++++++++++++++++++")
print(list01)
#5,两种遍历方式
for item in list01:
    print(item)
for i in range(len(list01)):
    # print(list01[i])
    print(str(i) + "--------" + str(list01[i]))
''''''

###### dict，无序
''''''
dict01 = {"name":"ivanl", "age":10, "num":"10120945", 2: "good"}
print(type(dict))
print(type(dict01))
#1,访问元素
print(dict01["name"])
#2,判断是否存在
if dict01["name"] != None:
    print("name存在")
print("age" in dict01)
print(2 in dict01)
#3,删除
del dict01[2]
#4，遍历
for key in dict01:
    print(str(key) + "--------" + str(dict01[key]))
print('==========================================')
for key, value in dict01.items():
    print(key, value)
#5, 增加元素
dict01["money"] = 200
print(dict01)
''''''

###### set,不重复
''''''
print("____________________set_______________________")
set01 = set([1,2,3,4,22,432,2,3432])
set02 = set([2,343, 2234,321,21,1])
#1, 判断元素是否存在
print(4 in set01)
#2, 求并集,交集，差集
print(set01 | set02)
print(set01.union(set02))
print(set01 & set02)
print(set01.intersection(set02))
print(set01-set02)
print(set01.difference(set02))
#3, 对称差集，类似与异或操作，先求并集，然后减去两个的差集， 也就是去掉两个都有的
print(set01^set02)
print(set01.symmetric_difference(set02))
#4, 修改元素，比如添加等
set01.add("oooo")
set01.remove(22)
print("----")
for i in set01:
    print(i)

print(set01)

''''''


###### 切片
''''''
list02 = [0,1,2,3,4,5,6,7,8,9]
print(list02[0:2])
print(list02[:4])#包括前面，不包括后面
print(list02[3:])
print(list02[3:8:2])
print(list02[::-1])





''''''


###### 作业
#* 把一个字符串根据单词逆序
''''''
print("--------作业--------")
str = "I am the king of world! good and very good!"
handledStrArr = str.split(" ")
print(handledStrArr)
handledStrArr.reverse()
print(" ".join(handledStrArr))

''''''


