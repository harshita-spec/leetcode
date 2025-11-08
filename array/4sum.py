# 18. 4Sum

# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.
# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

def sum(arr,target):
    ans=[]
    arr=sorted(arr)
    for i in range(len(arr)):
        if i>0 and arr[i]==arr[i-1]:
            continue
        for j in range(i+1 ,len(arr)):
            if j!=i+1 and arr[j]==arr[j-1]:
                continue
            k=j+1
            l=len(arr)-1
            while k<l:
                sum = arr[i]+arr[j]
                sum+=arr[k]
                sum+=arr[l]
                if sum==target:
                    temp=[arr[i],arr[j],arr[k],arr[l]]
                    ans.append(temp)
                    l-=1
                    k-=1
                    while k<l and arr[k]==arr[k-1]:
                        k+=1
                    while k<l and arr[l]==arr[l+1]:
                        l-=1
                elif sum<target:
                    k+=1
                else:
                    l-=1
    return ans

arr = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6]
target=14
ans = sum(arr,target) 
print(ans)