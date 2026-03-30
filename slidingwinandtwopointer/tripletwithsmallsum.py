# Triplets with Smaller Sum

# Given an array arr[] of distinct integers of size n and a value sum, the task is to find the count of triplets (i, j, k), having (i<j<k) with the sum of (arr[i] + arr[j] + arr[k]) smaller than the given value sum.
# Examples :
# Input: n = 4, sum = 2, arr[] = {-2, 0, 1, 3}
# Output:  2
# Explanation: Below are triplets with sum less than 2 (-2, 0, 1) and (-2, 0, 3). 
# Input: n = 5, sum = 12, arr[] = {5, 1, 3, 4, 7}
# Output: 4
# Explanation: Below are triplets with sum less than 12 (1, 3, 4), (5, 1, 3), (1, 3, 7) and (5, 1, 4).

def counttriplet(arr,sum):
    arr.sort()
    count=0
    for i in range(len(arr)):
        j=i+1
        k=len(arr)-1
        while j<k:
            if arr[i]+arr[j]+arr[k]<sum:
                count+=1
                j+=1
            elif arr[i]+arr[j]+arr[k]>=sum:
                k-=1
    return count
arr=[-2, 0, 1, 3]
sum=2
result=counttriplet(arr,sum)
print(result)