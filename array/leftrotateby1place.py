# left rotate  the array by one places

# ip: arr[]=[1,2,3,4,5,6]

# op: [2,3,4,5,6,1]

def rotate(arr,k):
    n=len(arr)
    k=k%n
    temp=arr[-k:]
    for i in range(n-k-1,-1,-1):
        arr[i+k]=arr[i]
    for i in range(k):
        arr[i]=temp[i]
    return arr
arr=[1,2,3,4,5]
k=4
r=rotate(arr,k)
print(r)