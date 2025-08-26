# 3 Sum

# Given an integer array nums. Return all triplets such that:
# i != j, i != k, and j != k
# nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets. One element can be a part of multiple triplets. The output and the triplets can be returned in any order.
# Examples:
# Input: nums = [2, -2, 0, 3, -3, 5]
# Output: [[-2, 0, 2], [-3, -2, 5], [-3, 0, 3]]
# Explanation: nums[1] + nums[2] + nums[0] = 0
# nums[4] + nums[1] + nums[5] = 0
# nums[4] + nums[2] + nums[3] = 0
# Input: nums = [2, -1, -1, 3, -1]
# Output: [[-1, -1, 2]]
# Explanation: nums[1] + nums[2] + nums[0] = 0
# Note that we have used two -1s as they are separate elements with different indexes
# But we have not used the -1 at index 4 as that would create a duplicate triplet

# def triplet(n, arr):
#     st = set()

#     for i in range(n):
#         hashset = set()
#         for j in range(i + 1, n):
#             third = -(arr[i] + arr[j])
#             if third in hashset:
#                 temp = [arr[i], arr[j], third]
#                 temp.sort()
#                 st.add(tuple(temp))
#             hashset.add(arr[j])
#     ans = list(st)
#     return ans

#optimal
def sum(arr):
    ans=[]
    arr=sorted(arr)
    for i in range(len(arr)):
        if i>0 and arr[i]==arr[i-1]:
            continue
        j=i+1
        k=len(arr)-1
        while j<k:
            sum = arr[i]+arr[j]+arr[k]
            if sum<0:
                j+=1
            elif sum>0:
                k-=1
            else:
                temp=(arr[i],arr[j],arr[k])
                ans.append(temp)
                j+=1
                k-=1
                while j<k and arr[j]==arr[j-1]:
                    j+=1
                while j<k and arr[k]==arr[k+1]:
                    k-=1
    return ans

arr = [-1, 0, 1, 2, -1, -4]
ans = sum(arr) 
print(ans)

