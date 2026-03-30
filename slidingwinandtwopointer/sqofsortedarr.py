# 977. Squares of a Sorted Array

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

def sortedSquares(nums):
        n = len(nums)
        res = [0] * n
        left = 0
        right = n - 1
        pos = n - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[pos] = nums[left] ** 2
                left += 1
            else:
                res[pos] = nums[right] ** 2
                right -= 1
            pos -= 1
        return res
nums = [-4,-1,0,3,10]
result=sortedSquares(nums)
print(result)
