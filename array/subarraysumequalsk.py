# 560. Subarray Sum Equals K

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2

from collections import defaultdict
def findAllSubarraysWithGivenSum(arr, k):
    n = len(arr) 
    mpp = defaultdict(int)
    preSum = 0
    cnt = 0
    mpp[0] = 1 
    for i in range(n):
        preSum += arr[i]
        remove = preSum - k
        cnt += mpp[remove]
        mpp[preSum] += 1
    return cnt
arr = [3, 1, 2, 4,7]
k = 6
cnt = findAllSubarraysWithGivenSum(arr, k)
print("The number of subarrays is:", cnt)
