# 137. Single Number II

# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:
# Input: nums = [0,1,0,1,0,1,99]
# Output: 99

def singlenumber(nums):
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    count+=1
            if count==1:
                return nums[i] 
nums = [2,2,3,2]
print(singlenumber(nums))   

def singlenum2(nums):
        freq={}
        for s in nums:
            freq[s]=freq.get(s,0)+1
        for i,l in freq.items():
            if l==1:
                 return i
nums=[4,5,4,5,6,7,6]
print(singlenum2(nums))