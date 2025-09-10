# Linear Search

# Given an array of integers nums and an integer target, find the smallest index (0 based indexing) where the target appears in the array. If the target is not found in the array, return -1.
# Examples:
# Input: nums = [2, 3, 4, 5, 3], target = 3
# Output: 1
# Explanation:
# The first occurence of 3 in nums is at index 1
# Input: nums = [2, -4, 4, 0, 10], target = 6
# Output: -1
# Explanation:
# The value 6 does not occur in the array, hence output is -1

def array(arr,n):
    num=int(input("enter the number: "))
    for i in range(n):
        if arr[i]==num:
            return i
        else:
            return -1
    return i
arr=[1,4,6,7,8]
n=len(arr)
result=array(arr,n)
print(result)