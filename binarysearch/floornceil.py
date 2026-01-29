# Floor and Ceil in Sorted Array

# Given a sorted array nums and an integer x. Find the floor and ceil of x in nums. The floor of x is the largest element in the array which is smaller than or equal to x. The ceiling of x is the smallest element in the array greater than or equal to x. If no floor or ceil exists, output -1.
# Examples:
# Input : nums =[3, 4, 4, 7, 8, 10], x= 5
# Output: 4 7
# Explanation: The floor of 5 in the array is 4, and the ceiling of 5 in the array is 7.
# Input : nums =[3, 4, 4, 7, 8, 10], x= 8
# Output: 8 8
# Explanation: The floor of 8 in the array is 8, and the ceiling of 8 in the array is also 8.

def ceil(arr,target):
    low=0
    high=len(arr)-1
    ans=len(arr)
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=target:
            ans=arr[mid]
            high=mid-1
        else:
            low=mid+1
    return ans
def floor(arr,target):
    low=0
    high=len(arr)-1
    ans=len(arr)
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<=target:
            ans=arr[mid]
            low=mid+1
        else:
            high=mid-1
    return ans
arr=[3, 4, 4, 7, 8, 10]
target=5
print(floor(arr,target))
print(ceil(arr,target))