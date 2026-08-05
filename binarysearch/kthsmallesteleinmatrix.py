# 378. Kth Smallest Element in a Sorted Matrix

# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# You must find a solution with a memory complexity better than O(n2).

# Example 1:
# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
# Example 2:
# Input: matrix = [[-5]], k = 1
# Output: -5

def kthSmallest(matrix, k):
        low=matrix[0][0]
        n=len(matrix[0])
        high = matrix[n-1][n-1]
        while low<=high:
            mid=(low+high)//2
            if bs(matrix,mid) >= k:
                high = mid-1
            else:
                low = mid+1
        return low 

def bs(matrix,mid):
        n = len(matrix)
        row = n - 1
        col = 0
        count = 0
        while row >= 0 and col < n:
            if matrix[row][col] <= mid:
                count += (row + 1)
                col += 1
            else:
                row -= 1
        return count

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print(kthSmallest(matrix, k))