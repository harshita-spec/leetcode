# Count Occurrences in a Sorted Array

# You are given a sorted array of integers arr and an integer target. Your task is to determine how many times target appears in arr.

# Return the count of occurrences of target in the array.
# Examples:
# Input: arr = [0, 0, 1, 1, 1, 2, 3], target = 1
# Output: 3
# Explanation: The number 1 appears 3 times in the array.
# Input: arr = [5, 5, 5, 5, 5, 5], target = 5
# Output: 6
# Explanation: All elements in the array are 5, so the target appears 6 times.

def firstnlast(arr,n,k):
    f1=first(arr,n,k)
    if f1 == -1:
        return (-1, -1) 
    l1=last(arr,n,k)
    return (f1, l1)
def first(arr,n,k):
    low=0
    high=n-1
    first= -1
    while low <= high:
        mid=(low+high)//2
        if arr[mid]==k:
            first=mid
            high=mid-1
        elif arr[mid]<k:
            low=mid+1
        else:
            high=mid-1
    return first
def last(arr,n,k):
    low=0
    high=n-1
    last= -1
    while low <= high:
        mid=(low+high)//2
        if arr[mid]==k:
            last=mid
            low=mid+1
        elif arr[mid]<k:
            low=mid+1
        else:
            high=mid-1
    return last
def cnt(arr,n,k):
    first,last = firstnlast(arr,n,k)
    if first==-1:
        return 0
    return last - first + 1
arr=[2,8,8,8,8,8,8,10,11]
n=len(arr)
k=5
result=cnt(arr,n,k)
print(result)