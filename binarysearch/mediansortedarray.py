# Median of 2 sorted arrays

# Given two sorted arrays arr1 and arr2 of size m and n respectively, return the median of the two sorted arrays.

# The median is defined as the middle value of a sorted list of numbers. In case the length of the list is even, the median is the average of the two middle elements.
# Examples:
# Input: arr1 = [2, 4, 6], arr2 = [1, 3, 5]
# Output: 3.5
# Explanation: The array after merging arr1 and arr2 will be [ 1, 2, 3, 4, 5, 6 ]. As the length of the merged list is even, the median is the average of the two middle elements. Here two medians are 3 and 4. So the median will be the average of 3 and 4, which is 3.5.
# Input: arr1 = [2, 4, 6], arr2 = [1, 3]
# Output: 3.0
# Explanation: The array after merging arr1 and arr2 will be [ 1, 2, 3, 4, 6 ]. The median is simply 3.

def median(a,b):
    n1=len(a)
    n2=len(b)
    if n1>n2:
        return median(b,a)
    low=0
    high=n1
    left=(n1+n2+1)//2
    n=n1+n2
    while low<=high:
        mid1=(low+high)>>1
        mid2=left-mid1
        l1=float('inf')
        l2=float('inf')
        r1=float('-inf')
        r2=float('-inf')
        if mid1<n1:
            r1=a[mid1]
        if mid2<n2:
            r2=b[mid2]
        if mid1-1>=0:
            l1=a[mid1-1]
        if mid2-1>=0:
            l2=b[mid2-1]
        if l1<=r2 and l2<=r1:
            if n%2 ==1:
                return max(l1,l2)
            return ((max(l1,l2)+min(r1,r2))/2.0)
        elif l1>r2:
            high=mid1-1
        else:
            low=mid1+1
    return 0

a=[2, 4, 6]
b=[1, 3, 5]
result=median(a,b)
print(result)