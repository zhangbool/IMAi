
#1， 在0至n-1的范围内，找出最小值，放在第一个位置
#2， 在1至n-1的范围内，找出最小值，放在第二个位置
#3， 按照上面的方式依次进行，直到最后一位即可

arr = [3, 1, 4, 2, 100, 34, 23, 254, 234]

for i in range(len(arr)):
    index = i#这个是最值序号
    #print("-----------------------")
    for j in range(i+1, len(arr)):
        #print(arr[j])
        if arr[index] < arr[j]:#这里把序号互换方便之后进行数值的替换
            temp = index
            index = j
            j = temp
    if index != i:
        temp = arr[i]
        arr[i] = arr[index]
        arr[index] = temp
    #print(arr)

print(arr)




