# Sum of Subarray Ranges

# Given an integer array nums, determine the range of a subarray, defined as the difference between the largest and smallest elements within the subarray. Calculate and return the sum of all subarray ranges of nums.
# A subarray is defined as a contiguous, non-empty sequence of elements within the array.

# Example 1
# Input: nums = [1, 2, 3]
# Output: 4
# Explanation: The 6 subarrays of nums are the following:
# [1], range = largest - smallest = 1 - 1 = 0 
# [2], range = 2 - 2 = 0
# [3], range = 3 - 3 = 0
# [1,2], range = 2 - 1 = 1
# [2,3], range = 3 - 2 = 1
# [1,2,3], range = 3 - 1 = 2
# So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

# Example 2
# Input: nums = [1, 3, 3]
# Output: 4
# Explanation: The 6 subarrays of nums are the following:
# [1], range = largest - smallest = 1 - 1 = 0
# [3], range = 3 - 3 = 0
# [3], range = 3 - 3 = 0
# [1,3], range = 3 - 1 = 2
# [3,3], range = 3 - 3 = 0
# [1,3,3], range = 3 - 1 = 2
# So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.

# brute force approach
def sumofsubarrayrange(nums):
    n=len(nums)
    total=0
    for i in range(n):
        mini=float('inf')
        maxi=float('-inf')
        for j in range(i,n):
            mini=min(mini,nums[j])
            maxi=max(maxi,nums[j])
            total=(total+(maxi-mini))%(10**9+7)
    return total
nums=[1, 2, 3]
print(sumofsubarrayrange(nums))

