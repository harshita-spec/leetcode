# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0. You must do it in place.
# Examples:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Explanation:
# Element at position (1,1) is 0, so set entire row 1 and column 1 to 0.
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
# Explanation:
# There are two zeroes: (0,0) and (0,3).
# Row 0 → all elements become 0
# Column 0 and column 3 → all elements become 0

def zeroMatrix(matrix, n, m):
    # int row[n] = {0}; --> matrix[..][0]
    # int col[m] = {0}; --> matrix[0][..]
    col0 = 1
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] != 0:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0

    return matrix

matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
n = len(matrix)
m = len(matrix[0])
ans = zeroMatrix(matrix, n, m)
print("The Final matrix is:")
for row in ans:
	for ele in row:
	    print(ele, end=" ")
    print()
