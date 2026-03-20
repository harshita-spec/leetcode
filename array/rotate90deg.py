# Rotate matrix by 90 degrees

# Given an N * N 2D integer matrix, rotate the matrix by 90 degrees clockwise.

# The rotation must be done in place, meaning the input 2D matrix must be modified directly.
# Examples:
# Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Output: matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

# Input: matrix = [[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]]

# Output: matrix = [[5, 4, 2, 0], [6, 5, 0, 1], [7, 0, 3, 1], [0, 5, 1, 2]]

#brute force
def matrotate(matrix):
    n=len(matrix)
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[j][n-1-i] = matrix[i][j]
    return ans
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrotate(matrix))
   
#optimal 
def mat(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(n):
        rev(matrix[i])

def rev(arr):   
    l=0
    r=len(arr)-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1    
arr = [[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]]
mat(arr)
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j], end=" ")
    print()
