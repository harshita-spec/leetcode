# Rearrange array elements by sign

# Given an integer array nums of even length consisting of an equal number of positive and negative integers.Return the answer array in such a way that the given conditions are met:

# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Examples:
# Input : nums = [2, 4, 5, -1, -3, -4]
# Output : [2, -1, 4, -3, 5, -4]
# Explanation: The positive number 2, 4, 5 maintain their relative positions and -1, -3, -4 maintain their relative positions
# Input : nums = [1, -1, -3, -4, 2, 3]
# Output : [1, -1, 2, -3, 3, -4]
# Explanation: The positive number 1, 2, 3 maintain their relative positions and -1, -3, -4 maintain their relative positions

def rearrange(arr):
    n=len(arr)
    neg=[]
    pos=[]
    for i in range(n):
        if arr[i]<0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])
    if len(pos)>len(neg):
        for i in range(len(neg)):
            arr[2*i]=pos[i]
            arr[2*i+1]=neg[i]
        index=len(neg)*2
        for i in range(len(neg),len(pos)):
            arr[index]=pos[i]
            index+=1
    else:
        for i in range(len(pos)):
            arr[2*i]=pos[i]
            arr[2*i+1]=neg[i]
        index=len(pos)*2
        for i in range(len(pos),len(neg)):
            arr[index]=neg[i]
            index+=1
    return arr
arr=[3,-2,4,5,9,-4,-1,-8]
result=rearrange(arr)
print(result)