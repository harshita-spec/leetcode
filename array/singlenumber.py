# Single Number - I
# Given an array of nums of n integers. Every integer in the array appears twice except one integer. Find the number that appeared once in the array.
# Example 1
# Input : nums = [1, 2, 2, 4, 3, 1, 4]
# Output : 3
# Explanation : The integer 3 has appeared only once.
# Example 2
# Input : nums = [5]
# Output : 5
# Explanation : The integer 5 has appeared only once

#brute
def single(arr):
    for i in range(len(arr)):
        count=0
        num=arr[i]
        for j in range(len(arr)):
            if arr[j]==num:
                count+=1
        if count==1:
            return num
        
#better
def single(arr):
    mpp={}
    for i in range(len(arr)):
        if arr[i] in mpp:
            mpp[arr[i]]+=1
        else:
            mpp[arr[i]]=1
    for i ,value in mpp.items():
        if value==1:
            return i

#optimal
def single(arr):
    res=0
    for i in range(len(arr)):
        res=res^arr[i]
    return res

arr=[1,2,2,4,3,3,5,1,5,6,4]
print(single(arr))