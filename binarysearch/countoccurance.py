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

def count(arr,n,k):
    f1=first(arr,k)
    if f1 == -1:
        return 0 
    l1=last(arr,k)
    return l1-f1+1
def first(arr,k):
    n=len(arr)
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
def last(arr,k):
    n=len(arr)
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

arr=[2,8,8,8,8,8,8,10,11]
n=len(arr)
k=8
result=count(arr,n,k)
print(result)