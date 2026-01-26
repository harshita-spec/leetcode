# Find missing number

# Given an integer array of size n containing distinct values in the range from 0 to n (inclusive), return the only number missing from the array within this range.
# Examples:
# Input: nums = [0, 2, 3, 1, 4]
# Output: 5
# Explanation:
# nums contains 0, 1, 2, 3, 4 thus leaving 5 as the only missing number in the range [0, 5]
# Input: nums = [0, 1, 2, 4, 5, 6]
# Output: 3
# Explanation:
# nums contains 0, 1, 2, 4, 5, 6 thus leaving 3 as the only missing number in the range [0, 6]

def miss(arr,n):
    sum=(n*(n+1))/2
    s2=0
    for i in range(n):
        s2+=arr[i]
    return int(sum-s2)
def misss(arr,n):
    for i in range(n):
        if i not in arr:
            return i
    return n  
arr=[0, 1, 2, 4, 5, 6]
n=len(arr)
print(miss(arr,n))
print(misss(arr,n))