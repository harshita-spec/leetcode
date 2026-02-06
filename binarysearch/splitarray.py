# Split array - largest sum

# Given an integer array a of size n and an integer k. Split the array a into k non-empty subarrays such that the largest sum of any subarray is minimized. Return the minimized largest sum of the split.
# Examples:
# Input: a = [1, 2, 3, 4, 5], k = 3
# Output:6
# Explanation: There are many ways to split the array a[] into k consecutive subarrays. The best way to do this is to split the array a[] into [1, 2, 3], [4], and [5], where the largest sum among the three subarrays is only 6.
# Input: a = [3,5,1], k = 3
# Output: 5
# Explanation: There is only one way to split the array a[] into 3 subarrays, i.e., [3], [5], and [1]. The largest sum among these subarrays is 5.

import math
def split(arr,m):
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
arr=[3,5,1]
m=3
result=split(arr,m)
print(result)