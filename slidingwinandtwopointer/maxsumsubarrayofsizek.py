# Max Sum Subarray of size K

# Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.
# Note: A subarray is a contiguous part of any given array.
# Examples:
# Input: arr[] = [100, 200, 300, 400], k = 2
# Output: 700
# Explanation: arr2 + arr3 = 700, which is maximum.
# Input: arr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
# Output: 39
# Explanation: arr1 + arr2 + arr3 + arr4 = 39, which is maximum.
# Input: arr[] = [100, 200, 300, 400], k = 1
# Output: 400
# Explanation: arr3 = 400, which is maximum.

def maxsum(arr,k):
    maxsum=0
    sum1=0
    for i in range(k):
        sum1+=arr[i]
    maxsum=sum1
    for i in range(k,len(arr)):
        sum1=sum1+arr[i]-arr[i-k]
        maxsum=max(sum1,maxsum)
    return maxsum
arr=[100, 200, 300, 400]
k=2
print(maxsum(arr,k))

    