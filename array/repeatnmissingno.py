# Find the repeating and missing number

# Given an integer array nums of size n containing values from [1, n] and each value appears exactly once in the array, except for A, which appears twice and B which is missing.
# Return the values A and B, as an array of size 2, where A appears in the 0-th index and B in the 1st index.

# Note: You are not allowed to modify the original array.
# Examples:
# Input: nums = [3, 5, 4, 1, 1]
# Output: [1, 2]
# Explanation: 1 appears two times in the array and 2 is missing from nums
# Input: nums = [1, 2, 3, 6, 7, 5, 7]
# Output: [7, 4]
# Explanation: 7 appears two times in the array and 4 is missing from nums.

def number(arr):
    n=len(arr)
    sn=(n*(n+1))/2
    s2n=(n*(n+1)*(2*n+1))/6
    s=0
    s2=0
    for i in range(n):
        s+=arr[i]
        s2+=arr[i]*arr[i]
    val1=s-sn
    val2=s2-s2n
    val2=val2/val1
    x=(val1+val2)/2
    y=(x-val1)
    return {int(x),int(y)}
arr=[4,3,6,2,1,1]
result=number(arr)
print(result)