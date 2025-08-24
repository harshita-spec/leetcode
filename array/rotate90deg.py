# Rotate matrix by 90 degrees

# Given an N * N 2D integer matrix, rotate the matrix by 90 degrees clockwise.

# The rotation must be done in place, meaning the input 2D matrix must be modified directly.
# Examples:
# Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Output: matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

# Input: matrix = [[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]]

# Output: matrix = [[5, 4, 2, 0], [6, 5, 0, 1], [7, 0, 3, 1], [0, 5, 1, 2]]

def mat(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(n):
        matrix[i].reverse()

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat(arr)
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j], end=" ")
    print()
