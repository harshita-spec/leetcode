# Single element in sorted array

# Given an array nums sorted in non-decreasing order. Every number in the array except one appears twice. Find the single number in the array.
# Examples:
# Input :nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
# Output:4
# Explanation: Only the number 4 appears once in the array.
# Input : nums = [1, 1, 3, 5, 5]
# Output:3
# Explanation: Only the number 3 appears once in the array.

def find(arr,n):
    if n==1:
        return arr[0]
    if arr[0]!=arr[1]:
        return arr[0]
    if arr[n-1]!=arr[n-2]:
        return arr[n-1]
    low=1
    high=n-2
    while low<=high:
        mid=(low+high)//2
        if arr[mid]!=arr[mid+1] and arr[mid]!=arr[mid-1]:
            return arr[mid]
        if (mid%2==1 and arr[mid-1]==arr[mid])or(mid%2==0 and arr[mid]==arr[mid+1]):
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[1,1,2,2,3,3,4,4,5,5,6,6,7]
n=len(arr)
result=find(arr,n)
print(result)