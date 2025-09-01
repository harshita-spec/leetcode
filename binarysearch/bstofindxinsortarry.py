# Search X in sorted array

# Given a sorted array of integers nums with 0-based indexing, find the index of a specified target integer. If the target is found in the array, return its index. If the target is not found, return -1.
# Examples:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: The target integer 9 exists in nums and its index is 4
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: The target integer 2 does not exist in nums so return -1

def binary(arr,target):
    n=len(arr)
    low=0
    high=n-1
    while low<high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return -1
arr=[3,4,6,7,9,12,16,17]
target=7
result=binary(arr,target)
print(result)