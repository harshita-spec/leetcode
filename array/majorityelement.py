# Majority Element-I

# Given an integer array nums of size n, return the majority element of the array.

# The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.
# Examples:
# Input: nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
# Output: 7
# Explanation: The number 7 appears 5 times in the 9 sized array
# Input: nums = [1, 1, 1, 2, 1, 2]
# Output: 1
# Explanation: The number 1 appears 4 times in the 6 sized array

def majority(arr):
    for i in range(len(arr)):
        count=0
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                count+=1
        if count>len(arr)/2:
            return arr[i]
    return -1
arr=[7, 0, 0, 1, 7, 2, 7, 7,7 ,7,7,7]
result=majority(arr)
print(result) 

def Majority(arr):
    hash_map={}
    for i in range(len(arr)):
        if arr[i] in hash_map:
            hash_map[arr[i]]+=1
        else:
            hash_map[arr[i]]=1
    for key in hash_map:
        if hash_map[key]>len(arr)/2:
            return key
    return -1
arr=[7, 0, 0, 1, 7, 7, 2, 7, 7]
result=Majority(arr)
print(result)

def major(arr):
    count=0
    for i in range(len(arr)):
        if count==0:
            count=1
            ele=arr[i]
        elif arr[i]==ele:
            count+=1
        else:
            count-=1
    count1=0
    for i in range(len(arr)):
        if arr[i]==ele:
            count1+=1
        if count1>(len(arr)/2):
            return ele
    return -1
arr=[7, 0, 0, 1, 7, 7, 2, 7, 7]
result=major(arr)
print(result)

