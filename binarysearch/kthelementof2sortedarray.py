# Kth element of 2 sorted arrays

# Given two sorted arrays a and b of size m and n respectively. Find the kth element of the final sorted array.
# Examples:
# Input: a = [2, 3, 6, 7, 9], b = [1, 4, 8, 10], k = 5
# Output: 6
# Explanation: The final sorted array would be [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th element of this array is 6.
# Input: a = [100, 112, 256, 349, 770], b = [72, 86, 113, 119, 265, 445, 892], k = 7
# Output: 256
# Explanation: Final sorted array is - [72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892], 7th element of this array is 256.

def kthElement(a, b, m, n, k):
    if m > n:
        return kthElement(b, a, n, m, k)
    left = k  
    low = max(0, k - n)
    high = min(k, m)
    while low <= high:
        mid1 = (low + high) // 2
        mid2 = left - mid1
        l1 = float('-inf')
        l2 = float('-inf')
        r1 = float('inf')
        r2 = float('inf')
        if mid1 < m:
            r1 = a[mid1]
        if mid2 < n:
            r2 = b[mid2]
        if mid1 - 1 >= 0:
            l1 = a[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = b[mid2 - 1]
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
    return 0  
a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
print(kthElement(a, b, len(a), len(b), 5))
        