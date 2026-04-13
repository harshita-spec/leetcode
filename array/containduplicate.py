# 217. Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# All elements are distinct.
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

def dup(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                return True
    return False
nums = [1,1,1,3,3,4,3,2,4,2]
print(dup(nums))

def containdup(arr):
    s = set()
    for i in arr:
        if i in s:
            return True
        s.add(i)
    return False
arr=[1,3,5,6,2,6,7]
print(containdup(arr))