# Lower Bound

# Given a sorted array of nums and an integer x, write a program to find the lower bound of x.
# The lower bound algorithm finds the first and smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.
# If no such index is found, return the size of the array.
# Examples:
# Input : nums= [1,2,2,3], x = 2
# Output:1
# Explanation:
# Index 1 is the smallest index such that arr[1] >= x.
# Input : nums= [3,5,8,15,19], x = 9
# Output: 3
# Explanation:
# Index 3 is the smallest index such that arr[3] >= x.

def lb(arr,target):
    n=len(arr)
    low=0
    high=n-1
    ans=n
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
arr=[3,5,8,15,19]
target=9
result=lb(arr,target)
print(result)