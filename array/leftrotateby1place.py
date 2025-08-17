# left rotate  the array by one places

# ip: arr[]=[1,2,3,4,5,6]

# op: [2,3,4,5,6,1]

def rotate(arr):
    temp=arr[0]
    for i in range(len(arr)):
        arr[i-1]=arr[i]
    arr[len(arr)-1]=temp
    return arr


