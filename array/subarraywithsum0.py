# Largest Subarray with Sum 0

# You are given an integer array arr of size n which contains both positive and negative integers. Your task is to find the length of the longest contiguous subarray with sum equal to 0.
# Return the length of such a subarray. If no such subarray exists, return 0.
# Examples:
# Input: arr = [15, -2, 2, -8, 1, 7, 10, 23]
# Output: 5
# Explanation:
# The subarray [-2, 2, -8, 1, 7] sums up to 0 and has the maximum length among all such subarrays.
# Input: arr = [2, 10, 4]
# Output: 0
# Explanation:
# There is no subarray whose elements sum to 0.

def maxLen(A,n):
    mpp = {}
    maxi = 0
    sum = 0
    for i in range(n):
        sum += A[i]
        if sum == 0:
            maxi = i + 1
        else:
            if sum in mpp:
                maxi = max(maxi, i - mpp[sum])
            else:
                mpp[sum] = i
    return maxi
a=[1,-1,3,2,-2,-8,1,7,10,23]
n=len(a)
result=maxLen(a,n)
print(result)