
#1,计算ptyhon的运行时间

#1.1,datetime
# import datetime
# starttime = datetime.datetime.now()
# for _ in range(1000000):
#     print("ivan is the king of world")
# endtime = datetime.datetime.now()
# print((endtime - starttime).microseconds)

#1.2,这个比较精确
# import time
# start = time.time()
# for _ in range(1000000):
#     print("ivan is the king of world")
# end = time.time()
# print(end-start)

#1.3,
# import time
# start = time.clock()
# for _ in range(1000000):
#     print("ivan is the king of world")
# end = time.clock()
# print(end-start)


#1.4, 还有比较牛逼的方式：
from timeit import timeit
#看执行1000000次x=1的时间：
timeit('x=1')
#看x=1的执行时间，执行1次(number可以省略，默认值为1000000)：
print(timeit('x=1', number=1))
#看一个列表生成器的执行时间,执行1次：
print(timeit('[i for i in range(10000)]', number=1))
#看一个列表生成器的执行时间,执行10000次：
print(timeit('[i for i in range(100) if i%2==0]', number=10000))






