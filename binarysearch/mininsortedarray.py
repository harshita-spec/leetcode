# Find minimum in Rotated Sorted Array

# Given an integer array nums of size N, sorted in ascending order with distinct values, and then rotated an unknown number of times (between 1 and N), find the minimum element in the array.
# Examples:
# Input : nums = [4, 5, 6, 7, 0, 1, 2, 3]
# Output: 0
# Explanation: Here, the element 0 is the minimum element in the array.
# Input : nums = [3, 4, 5, 1, 2]
# Output: 1
# Explanation:Here, the element 1 is the minimum element in the array.

def minimum(arr):
    n=len(arr)
    low=0
    high=n-1
    ans=float('inf')
    while low<=high:
        mid=(low+high)//2
        if arr[low]<=arr[high]:
            ans=min(ans,arr[low])
            break
        elif arr[low]<=arr[mid]:
            ans=min(ans,arr[low])
            low=mid+1
        else:
            ans=min(ans,arr[mid])
            high=mid-1
    return ans
arr=[4, 5, 6, 7, 0, 1, 2, 3]
result=minimum(arr)
print(result)