# 907. Sum of Subarray Minimums

# Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.
# Example 1:
# Input: arr = [3,1,2,4]
# Output: 17
# Explanation: 
# Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
# Sum is 17.
# Example 2:
# Input: arr = [11,81,94,43,3]
# Output: 444

# brute force approach
def sumofsubarrayminimum(arr):
    n=len(arr)
    total=0
    for i in range(n):
        mini=float('inf')
        for j in range(i,n):
            mini=min(mini,arr[j])
            total=(total+mini)%(10**9+7)
    return total
arr=[3,1,2,4]
print(sumofsubarrayminimum(arr))