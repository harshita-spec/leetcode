# Merge two sorted arrays without extra space

# Given two integer arrays nums1 and nums2. Both arrays are sorted in non-decreasing order.

# Merge both the arrays into a single array sorted in non-decreasing order.
# The final sorted array should be stored inside the array nums1 and it should be done in-place.
# nums1 has a length of m + n, where the first m elements denote the elements of nums1 and rest are 0s.
# nums2 has a length of n.
# Examples:
# Input: nums1 = [-5, -2, 4, 5], nums2 = [-3, 1, 8]
# Output: [-5, -3, -2, 1, 4, 5, 8]
# Explanation: The merged array is: [-5, -3, -2, 1, 4, 5, 8], where [-5, -2, 4, 5] are from nums1 and [-3, 1, 8] are from nums2
# Input: nums1 = [0, 2, 7, 8], nums2 = [-7, -3, -1]
# Output: [-7, -3, -1, 0, 2, 7, 8]
# Explanation: The merged array is: [-7, -3, -1, 0, 2, 7, 8], where [0, 2, 7, 8] are from nums1 and [-7, -3, -1] are from nums2

#brute force approach
def merge(arr1,arr2,n,m):
    arr3=[0]*(n+m)
    i=0
    j=0
    index=0
    while i<n and j<m:
        if arr1[i]<arr2[j]:
            arr3[index]=arr1[i]
            i+=1
        else:
            arr3[index]=arr2[j]
            j+=1
        index+=1
    while i<n:
        arr3[index]=arr1[i]
        i+=1
        index+=1
    while j<m:      
        arr3[index]=arr2[j]
        j+=1
        index+=1
    return arr3
nums1 = [-5, -2, 4, 5]
nums2 = [-3, 1, 8]
n=len(nums1)
m=len(nums2)
result=merge(nums1,nums2,n,m)
print(result)
print()

def merge(arr1,arr2,n,m):
    arr3=[0]*(n+m)
    i=0
    j=0
    index=0
    while i<n and j<m:
        if arr1[i]<arr2[j]:
            arr3[index]=arr1[i]
            i+=1
        else:
            arr3[index]=arr2[j]
            j+=1
        index+=1
    while i<n:
        arr3[index]=arr1[i]
        i+=1
        index+=1
    while j<m:
        arr3[index]=arr2[j]
        j+=1
        index+=1
    for i in range(len(arr3)):
        if i<n:
            arr1[i]=arr3[i]
        else:
            arr2[i-n]=arr3[i]   
arr1=[-5, -2, 4, 5]
arr2=[-3, 1, 8]
n=len(arr1)
m=len(arr2)
merge(arr1,arr2,n,m)
print(arr1)
print(arr2) 
print()

#optimal approach
def merged(arr1,arr2,n,m):
    left=n-1
    right=0
    while left>=0 and right<m:
        if arr1[left]>arr2[right]:
            arr1[left],arr2[right]=arr2[right],arr1[left]
            left-=1
            right+=1
        else:
            break
    arr1.sort()
    arr2.sort()
arr1=[1,3,5,7]
arr2=[0,2,6,8,9]
n=len(arr1)
m=len(arr2)
result= merged(arr1,arr2,n,m)
print("arr1[] = ", end="")
for i in range(n):              
    print(arr1[i], end=" ") 
print("\n")                    
print("arr2[] = ", end="")
for i in range(m):
    print(arr2[i], end=" ")
print() 

def overlap(arr1,arr2,n,m):
    len=n+m
    gap=(len//2)+(len%2)
    while gap>0:
        left=0
        right=left+gap
        while right<len:
            if left<n and right>=n:
                swap(arr1,arr2,left,right-n)
            elif left>=n:
                swap(arr2,arr2,left-n,right-n)
            else:
                swap(arr1,arr1,left,right)
            left+=1
            right+=1
        if gap==1:
            break
        gap=(gap//2)+(gap%2)
def swap(arr1,arr2,ind1,ind2):
    if arr1[ind1]>arr2[ind2]:
        arr1[ind1],arr2[ind2]=arr2[ind2],arr1[ind1]
arr1=[1,3,5,7]
arr2=[0,2,6,8,9]
n=len(arr1)
m=len(arr2)
overlap(arr1,arr2,n,m)
print("\n")
print("arr1[] = ", end="")
for i in range(n):
    print(arr1[i], end=" ")
print("\n")  
print("arr2[] = ", end="")
for i in range(m):
    print(arr2[i], end=" ")
print()