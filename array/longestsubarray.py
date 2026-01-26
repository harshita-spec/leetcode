# Longest subarray with sum K

# Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.
# Examples:
# Input: nums = [10, 5, 2, 7, 1, 9],  k=15
# Output: 4
# Explanation:
# The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.
# Input: nums = [-3, 2, 1], k=6
# Output: 0
# Explanation:
# There is no sub-array in the array that sums to 6. Therefore, the output is 0.
#brute force
def findsubarray(arr,k):
    lenh=0
    for i in range(len(arr)):
        sum=0
        for j in range(i,len(arr)):
            sum+=arr[j]
            if sum==k:
                lenh=max(lenh,j-i+1)
    return lenh

#optimal solution
def getLongestSubarray(a, k):
    n = len(a) 
    left= right = 0
    Sum = a[0]
    maxLen = 0
    while right < n:
        while left <= right and Sum > k:
            Sum -= a[left]
            left += 1
        if Sum == k:
            maxLen = max(maxLen, right - left + 1)
        right += 1
        if right < n: 
            Sum += a[right]
    return maxLen
arr = [10, 5, 2, 7, 1, 9]
k = 15
print(getLongestSubarray(arr, k))
print(findsubarray(arr,k))