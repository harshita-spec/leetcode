# upper Bound

# Given a sorted array of nums and an integer x, write a program to find the lower bound of x.
# The lower bound algorithm finds the first and smallest index in a sorted array where the value at that index is greater than a given key i.e. x.
# If no such index is found, return the size of the array.
# Examples:
# Input : nums= [1,2,2,3], x = 2
# Output:3

def ub(arr,target):
    n=len(arr)
    low=0
    high=n-1
    ans=n
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
arr=[3,5,8,15,19]
target=5
result=ub(arr,target)
print(result)