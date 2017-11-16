
#第一圈循环就是普通的循环
#第二圈循环是在第一圈循环的基础上进行的，也就是把arr[i]同数据中第i个数后面的所有数进行比较，依次往后冒泡即可

arr = [3, 1, 4, 2, 100, 34, 23, 254, 234]
for i in range(len(arr)-1):#从0开始，到倒数第二位，包括0， 不包括倒数第二位
    for j in range(i+1, len(arr)):#从i+1开始，到最后一位，包括i+1， 不包括最后一位
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)


