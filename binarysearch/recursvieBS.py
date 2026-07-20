def BS(arr,low,high,target):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return BS(arr,low,mid-1,target)
    else:
        return BS(arr,mid+1,high,target)
arr=[2,3,4,6,7,8,9]
low=0
high=len(arr)-1
target=5
print(BS(arr,low,high,target))