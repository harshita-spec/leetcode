# Max Consecutive Ones III

# Given a binary array nums and an integer k, flip at most k 0's.
# Return the maximum number of consecutive 1's after performing the flipping operation.
# Example 1
# Input : nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0] , k = 3
# Output : 10
# Explanation : The maximum number of consecutive 1's are obtained only if we flip the 0's present at position 3, 4, 5 (0 base indexing).
# The array after flipping becomes [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0].
# The number of consecutive 1's is 10.
# Example 2
# Input : nums = [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1] , k = 3
# Output : 9
# Explanation : The underlines 1's are obtained by flipping 0's in the new array.
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1].
# The number of consecutive 1's is 9.

#brute 
def maxones(nums,k):
    maxlen=0
    for i in range(len(nums)):
        zero=0
        for j in range(i,len(nums)):
            if nums[j]==0:
                zero+=1
            if zero<=k:
                maxlen=max(maxlen,j-i+1)
            else:
                break
    return maxlen

#better
def maxOnes(nums,k):
    l=0
    zero=0
    maxlen=0
    for r in range(len(nums)):
        if nums[r]==0:
            zero+=1
        while zero>k:
            if nums[l]==0:
                zero-=1
            l+=1
        if zero<=k:
            maxlen=max(maxlen,r-l+1)
    return maxlen

#optimal 
def maxOness(nums,k):
    l=0
    zero=0
    maxlen=0
    for r in range(len(nums)):
        if nums[r]==0:
            zero+=1
        while zero>k:
            if nums[l]==0:
                zero-=1
            l+=1
        if zero<=k:
            maxlen=max(maxlen,r-l+1)
    return maxlen

nums=[1,1,1,0,0,0,1,1,1,1,0]
k=3
print(maxones(nums,k))  
print(maxOnes(nums,k))
print(maxOness(nums,k))