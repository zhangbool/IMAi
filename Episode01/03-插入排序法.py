
#1， 从第二个开始，和之前所有的数进行比较，插入到正确的位置

arr = [3, 1, 4, 2, 100, 34, 23, 254, 234]

for i in range(1, len(arr)):
    temp = arr[i]
    j = i
    while j >0 and temp < arr[j-1]:
        arr[j] = arr[j-1]
        j = j-1
    arr[j] = temp

print(arr)




















#这种写法排的不正确，找了好久也找不到哪里错误
# for i in range(1, len(arr)):
#     index = i
#     for j in range(i,-1, -1):
#         print(j)
#         if arr[j] > arr[index]:#注意：这个算法和之前的两个都不一样，这里的>不能直接替换成<
#             temp = index
#             index = j
#             j = temp
#
#     #循环完成之后进行替换
#     temp = arr[index]
#     arr[index] = arr[i]
#     arr[i] = temp
#     print(arr)
#
# print(arr)
