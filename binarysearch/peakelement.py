# Find peak element

# Given an array arr of integers. A peak element is defined as an element greater than both of its neighbors.
# Formally, if arr[i] is the peak element, arr[i - 1] < arr[i] and arr[i + 1] < arr[i].

# Find the index(0-based) of a peak element in the array. If there are multiple peak numbers, return the index of any peak number.

# Note:
# As there can be many peak values, 1 is given as output if the returned index is a peak number, otherwise 0.
# Examples:
# Input : arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
# Output: 7
# Explanation: In this example, there is only 1 peak that is at index 7.
# Input : arr = [1, 2, 1, 3, 5, 6, 4]
# Output: 1
# Explanation: In this example, there are 2 peak numbers at indices 1 and 5. We can consider any of them.

def f(arr,n):
    if n==1:
        return 0
    if arr[0]>arr[1]:
        return 0
    if arr[n-1]>arr[n-2]:
        return n-1
    low=1
    high=n-2
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            return mid
        elif arr[mid]>arr[mid-1]:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[1, 2, 1, 3, 5, 6, 4]
n=len(arr)
result=f(arr,n)
print(result)