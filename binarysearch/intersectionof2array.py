# 349. Intersection of Two Arrays

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

def intersection(nums1, nums2):
        st=set()
        ans=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2 and nums1[i] not in st:
                ans.append(nums1[i])
                st.add(nums1[i])
        return ans 
nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1,nums2))

def intersections(nums1,nums2):
        n1=sorted(nums1)
        n2=sorted(nums2)
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
nums3 = [4,9,5]
nums4 = [9,4,9,8,4]
print(intersections(nums3,nums4))