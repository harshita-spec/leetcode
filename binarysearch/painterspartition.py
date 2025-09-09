# Painter's Partition

# You are given A painters and an array C of N integers where C[i] denotes the length of the ith board. Each painter takes B units of time to paint 1 unit of board. You must assign boards to painters such that:
# Each painter paints only contiguous segments of boards.
# No board can be split between painters.
# The goal is to minimize the time to paint all boards.

# Return the minimum time required to paint all boards modulo 10000003.
# Examples:
# Input: A = 2, B = 5, C = [1, 10]
# Output: 50
# Explanation:
# Painter 1 paints board 0 (length = 1), time = 5
# Painter 2 paints board 1 (length = 10), time = 50
# Max time = 50
# Return 50 % 10000003 = 50
# Input: A = 10, B = 1, C = [1, 8, 11, 3]
# Output: 11
# Explanation:
# Assign each board to a different painter
# Max time = max(1, 8, 11, 3) = 11
# Return 11 % 10000003 = 11

import math
def painterpartition(arr,m):
    if m>len(arr):
        return -1
    low=max(arr)
    high=sum(arr)
    while low<=high:
        mid=(low+high)//2
        if (fun(arr,mid)<=m):
            high=mid-1
        else:
            low=mid+1
    return low
def fun(arr,mid):
    stu=1
    pagestu=0
    for i in range(len(arr)):
        if pagestu+arr[i]<=mid:
            pagestu+=arr[i]
        else:
            stu+=1
            pagestu=arr[i]
    return stu
arr=[1, 8, 11, 3]
m=3
result=painterpartition(arr,m)
print(result)