# sorting a array in ascending order using for loop
arr=[64, 34, 25, 12, 22, 11, 90]
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print( arr)