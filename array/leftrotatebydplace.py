# Left Rotate Array by K Places

# Hints
# Company
# Given an integer array nums and a non-negative integer k, rotate the array to the left by k steps.


# Example 1

# Input: nums = [1, 2, 3, 4, 5, 6], k = 2

# Output: nums = [3, 4, 5, 6, 1, 2]

# Explanation:

# rotate 1 step to the left: [2, 3, 4, 5, 6, 1]

# rotate 2 steps to the left: [3, 4, 5, 6, 1, 2]

# Example 2

# Input: nums = [3, 4, 1, 5, 3, -5], k = 8

# Output: nums = [1, 5, 3, -5, 3, 4]

# Explanation:

# rotate 1 step to the left: [4, 1, 5, 3, -5, 3]

# rotate 2 steps to the left: [1, 5, 3, -5, 3, 4]

# rotate 3 steps to the left: [5, 3, -5, 3, 4, 1]

# rotate 4 steps to the left: [3, -5, 3, 4, 1, 5]

# rotate 5 steps to the left: [-5, 3, 4, 1, 5, 3]

# rotate 6 steps to the left: [3, 4, 1, 5, 3, -5]

# rotate 7 steps to the left: [4, 1, 5, 3, -5, 3]

# rotate 8 steps to the left: [1, 5, 3, -5, 3, 4]

# brute force
def rotate(arr,d):
    temp=[]
    for i in range(d):
        temp.append(arr[i])
    for i in range(d,len(arr)):
        arr[i-d]=arr[i]
    for i in range(len(temp)):
        arr[len(arr)-d+i]=temp[i]
    return arr
arr=[1,2,3,4,5,6]
d=2
r=rotate(arr,d)
print(r)

# optimal
def reverse(arr,start,end):
    while start<=end:
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start+=1
        end-=1

def rotate(arr,k):
    n=len(arr)
    k=k%n
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    reverse(arr,0,n-1)
    return arr

arr=[1,2,3,4,5,6,7,8,9]
k=4
r=rotate(arr,k)
print(r)