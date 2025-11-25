# Find out how many times the array is rotated

# Given an integer array nums of size n, sorted in ascending order with distinct values. The array has been right rotated an unknown number of times, between 0 and n-1 (including). Determine the number of rotations performed on the array.
# Examples:
# Input : nums = [4, 5, 6, 7, 0, 1, 2, 3]
# Output: 4
# Explanation: The original array should be [0, 1, 2, 3, 4, 5, 6, 7]. So, we can notice that the array has been rotated 4 times.
# Input: nums = [3, 4, 5, 1, 2]
# Output: 3
# Explanation: The original array should be [1, 2, 3, 4, 5]. So, we can notice that the array has been rotated 3 times.

def minimum(arr,n):
    low=0
    high=n-1
    ans=float('inf')
    index=-1
    while low<=high:
        mid=(low+high)//2
        if arr[low]<=arr[high]:
            index=low
            if arr[low]<ans:
                ans=arr[low]
            break
        elif arr[low]<=arr[mid]:
            index=low
            if arr[low]<ans:
                ans=arr[low]
            low=mid+1
        else:
            index=mid
            if arr[mid]<ans:
                ans=arr[mid]
            high=mid-1
    return index
arr=[4, 5, 6, 7,8,9,0, 1, 2, 3]
n=len(arr)
result=minimum(arr,n)
print(result)