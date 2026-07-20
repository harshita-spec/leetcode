# 219. Contains Duplicate II

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

def duplicate(nums,k):
        w = set()
        for i in range(len(nums)):
            if nums[i] in w:
                return True
            w.add(nums[i])
            if len(w) > k:
                w.remove(nums[i - k])
        return False  
arr=[1,1,1,3,3,4,3,2,4,2]
k=3
print(duplicate(arr,k))