# Minimum days to make M bouquets

# Given n roses and an array nums where nums[i] denotes that the 'ith' rose will bloom on the nums[i]th day, only adjacent bloomed roses can be picked to make a bouquet. Exactly k adjacent bloomed roses are required to make a single bouquet. Find the minimum number of days required to make at least m bouquets, each containing k roses. Return -1 if it is not possible.
# Examples:
# Input: n = 8, nums = [7, 7, 7, 7, 13, 11, 12, 7], m = 2, k = 3
# Output: 12
# Explanation: On the 12th the first 4 flowers and the last 3 flowers would have already bloomed. So, we can easily make 2 bouquets, one with the first 3 and another with the last 3 flowers.
# Input: n = 5, nums = [1, 10, 3, 10, 2], m = 3, k = 2
# Output: -1
# Explanation: If we want to make 3 bouquets of 2 flowers each, we need at least 6 flowers. But we are given only 5 flowers, so, we cannot make the bouquets.

def bs(arr,m,k):
    n=len(arr)
    if n<(m*k):
        return -1
    mini=float('inf')
    maxi=float('-inf')
    for i in range(n):
        mini=min(mini,arr[i])
        maxi=max(maxi,arr[i])
    low=mini
    high=maxi
    while low<=high:
        mid=(low+high)//2
        if possible(arr,mid,m,k):
            high=mid-1
        else:
            low=mid+1
    return low
def possible(arr,mid,m,k):
    count=0
    b=0
    for i in range(len(arr)):
        if arr[i]<=mid:
            count+=1
        else:
            b+=(count//k)
            count=0
    b+=(count//k)
    return b>=m  
arr=nums = [1, 10, 3, 10, 2]
m = 3
k = 2
result=bs(arr,m,k)
print(result)