# First and last occurrence

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. If the target is not found in the array, return [-1, -1].
# Examples:
# Input: nums = [5, 7, 7, 8, 8, 10], target = 8
# Output: [3, 4]
# Explanation:The target is 8, and it appears in the array at indices 3 and 4, so the output is [3,4]
# Input: nums = [5, 7, 7, 8, 8, 10], target = 6
# Output: [-1, -1]
# Expalantion: The target is 6, which is not present in the array. Therefore, the output is [-1, -1].

def firstnlast(arr,n,k):
    f1=first(arr,n,k)
    if f1==-1:
        return {-1,-1}
    l1=last(arr,n,k)
    return {f1,l1}
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
    first= -1
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
result=firstnlast(arr,n,k)
print(result)