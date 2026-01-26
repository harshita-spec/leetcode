# Move Zeros to End
# Given an integer array nums, move all the 0's to the end of the array. The relative order of the other elements must remain the same.

# This must be done in place, without making a copy of the array.
# Example 1
# Input: nums = [0, 1, 4, 0, 5, 2]
# Output: [1, 4, 5, 2, 0, 0]
# Explanation:
# Both the zeroes are moved to the end and the order of the other elements stay the same
# Example 2
# Input: nums = [0, 0, 0, 1, 3, -2]
# Output: [1, 3, -2, 0, 0, 0]
# Explanation:
# All 3 zeroes are moved to the end and the order of the other elements stay the same

#brute force
def move0(arr):
    temp=[]
    for i in range(len(arr)):
        if arr[i]!=0:
            temp.append(arr[i])
    for i in range(len(temp)):
        arr[i]=temp[i]
    for i in range(len(temp),len(arr)):
        arr[i]=0
    return arr
arr=[0, 0, 0, 1, 3, -2]
print(move0(arr))