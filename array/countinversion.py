# Count Inversions

# Given an integer array nums. Return the number of inversions in the array.

# Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
# It indicates how close an array is to being sorted.
# A sorted array has an inversion count of 0.
# An array sorted in descending order has maximum inversion.
# Examples:
# Input: nums = [2, 3, 7, 1, 3, 5]
# Output: 5
# Explanation: The responsible indexes are:
# nums[0], nums[3], values: 2 > 1 & indexes: 0 < 3
# nums[1], nums[3], values: 3 > 1 & indexes: 1 < 3
# nums[2], nums[3], values: 7 > 1 & indexes: 2 < 3
# nums[2], nums[4], values: 7 > 3 & indexes: 2 < 4
# nums[2], nums[5], values: 7 > 5 & indexes: 2 < 5
# Input: nums = [-10, -5, 6, 11, 15, 17]
# Output: 0
# Explanation: nums is sorted, hence no inversions present.
import math
def merge(arr,low,mid,high):
    temp=[]
    left=low
    right=mid+1
    count=0
    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            count+=(mid-left+1)
            right+=1
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
    for i in range(low,high):
        arr[i]=temp[i-low]
    return count
def mergesort(arr,low,high):
    count=0
    if low>=high:
        return count
    mid=math.floor((low+high)/2)
    count+=mergesort(arr,low,mid)
    count+=mergesort(arr,mid+1,high)
    count+=merge(arr,low,mid,high)
    return count
def inversion(arr,n):
    return mergesort(arr,0,n-1)
arr=[-10, -5, 6, 11, 15, 17]
n=len(arr)
result=inversion(arr,n)
print(result)