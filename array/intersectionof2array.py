# 350. Intersection of Two Arrays II

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

def intersection(num1,num2):
        n1=sorted(num1)
        n2=sorted(num2)
        i=0
        j=0
        ans=[]
        while i<len(n1) and j<len(n2):
            if n1[i]==n2[j]:
                ans.append(n1[i])
                i+=1
                j+=1
            elif n1[i]< n2[j]:
                i+=1
            else:
                j+=1
        return ans
num1=[4,9,5]
num2 = [9,4,9,8,4]
print(intersection(num1,num2))