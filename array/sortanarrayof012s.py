# Sort an array of 0's 1's and 2's

# Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order. The sorting must be done in-place, without making a copy of the original array.
# Examples:
# Input: nums = [1, 0, 2, 1, 0]
# Output: [0, 0, 1, 1, 2]
# Explanation: The nums array in sorted order has 2 zeroes, 2 ones and 1 two
# Input: nums = [0, 0, 1, 1, 1]
# Output: [0, 0, 1, 1, 1]
# Explanation: The nums array in sorted order has 2 zeroes, 3 ones and zero twos

def sortt(arr):
    n=len(arr)
    low=0
    mid=0
    high=n-1
    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    return arr

arr=[0,1,1,0,1,2,1,2,0,0,0]
result=sortt(arr)
print(result)