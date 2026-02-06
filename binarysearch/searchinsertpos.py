# Search insert position

# Given a sorted array of nums consisting of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# Examples:
# Input: nums = [1, 3, 5, 6], target = 5
# Output: 2
# Explanation: The target value 5 is found at index 2 in the sorted array. Hence, the function returns 2.
# Input: nums = [1, 3, 5, 6], target = 2
# Output: 1
# Explanation: The target value 2 is not found in the array. However, it should be inserted at index 1 to maintain the sorted order of the array.

def searchinsert(arr,target):
    low=0
    high=len(arr)-1
    ans=len(arr)
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
arr=[3,5,8,15,17,19]
target=9
print(searchinsert(arr,target))
