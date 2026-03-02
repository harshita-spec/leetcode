# Kadane's Algorithm

# Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.

# A subarray is a contiguous non-empty sequence of elements within an array.
# Examples:
# Input: nums = [2, 3, 5, -2, 7, -4]
# Output: 15
# Explanation: The subarray from index 0 to index 4 has the largest sum = 15
# Input: nums = [-2, -3, -7, -2, -10, -4]
# Output: -2
# Explanation: The element on index 0 or index 3 make up the largest sum when taken as a subarray

def maximum(arr):
    n=len(arr)
    maxi=-float('inf')
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sum=0
            for k in range(i,j+1):
                sum+=arr[k]
            maxi=max(sum,maxi)
    return maxi 
arr=[2, 3, 5, -2, 7, -4]
result=maximum(arr)
print(result)

def Maximumsum(arr):
    n=len(arr)
    maxi=-float('inf')
    for i in range(len(arr)):
        sum=0
        for j in range(i,len(arr)):
            sum+=arr[j]
            maxi=max(sum,maxi)
    return maxi
arr=[2, 3, 5, -2, 7, -4]
result=Maximumsum(arr)
print(result)

import sys
def kadane(arr):
    n=len(arr)
    sum=0
    maxi=-float('inf')
    for i in range(n):
        sum+=arr[i]
        if sum>maxi:
            maxi=sum
        if sum<0:
            sum=0
    return maxi
arr=[2, 3, 5, -2, 7, -4]
result=kadane(arr)
print(result)