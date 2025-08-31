# Reverse Pairs

# Given an integer array nums. Return the number of reverse pairs in the array.
# An index pair (i, j) is called a reverse pair if:
# 0 <= i < j < nums.length
# nums[i] > 2 * nums[j]
# Examples:
# Input: nums = [6, 4, 1, 2, 7]
# Output: 3
# Explanation: The reverse pairs are:
# (0, 2) : nums[0] = 6, nums[2] = 1, 6 > 2 * 1
# (0, 3) : nums[0] = 6, nums[3] = 2, 6 > 2 * 2
# (1, 2) : nums[1] = 4, nums[2] = 1, 4 > 2 * 1
# Input: nums = [5, 4, 4, 3, 3]
# Output: 0
# Explanation: No pairs satisfy both the conditons.

def merge(arr,low,mid,high):
    temp=[]
    left=low
    right=mid+1
    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
    for i in range(low,high+1):
        arr[i]=temp[i-low]
def mergesort(arr,low,high):
    count=0
    if low>=high:
        return count
    mid=(low+high)//2
    count+=mergesort(arr,low,mid)
    count+=mergesort(arr,mid+1,high)
    count+=countpair(arr,low,mid,high)
    merge(arr,low,mid,high)
    return count
def countpair(arr,low,mid,high):
    count=0
    right=mid+1
    for i in range(low,mid+1):
        while right<=high and arr[i]>2*arr[right]:
            right+=1
        count+=(right-(mid+1))
    return count
def reversepair(arr,n):
    return mergesort(arr,0,n-1)
arr=[6, 4, 1, 2, 7]
n=len(arr)
result=reversepair(arr,n)
print(result)