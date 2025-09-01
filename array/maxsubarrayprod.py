# 152. Maximum Product Subarray

# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.
# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

def maxpro(arr):
    n=len(arr)
    maxi=arr[0]
    pre=1
    suf=1
    for i in range(n):
        if pre==0:
            pre=1
        if suf==0:
            suf=1
        pre=pre*arr[i]
        suf=suf*arr[n-i-1]
        maxi=max(maxi,max(pre,suf))
    return maxi
arr= [2,3,-2,4]
result=maxpro(arr)
print(result)