# Find row with maximum 1's

# Given a non-empty grid mat consisting of only 0s and 1s, where all the rows are sorted in ascending order, find the index of the row with the maximum number of ones.
# If two rows have the same number of ones, consider the one with a smaller index. If no 1 exists in the matrix, return -1.
# Examples:
# Input : mat = [ [1, 1, 1], [0, 0, 1], [0, 0, 0] ]
# Output: 0
# Explanation: The row with the maximum number of ones is 0 (0 - indexed).
# Input: mat = [ [0, 0], [0, 0] ]
# Output: -1
# Explanation: The matrix does not contain any 1. So, -1 is the answer.

def lowerBound(arr, n, x):
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1  
    return ans

def rowWithMax1s(matrix, n, m):
    cnt_max = 0
    index = -1
    for i in range(n):
        cnt_ones = m - lowerBound(matrix[i], m, 1)
        if cnt_ones > cnt_max:
            cnt_max = cnt_ones
            index = i
    return index

matrix = [[1, 1, 1], [0, 0, 1], [0, 0, 0]]
n = 3
m = 3
result=rowWithMax1s(matrix,n,m)
print(result)