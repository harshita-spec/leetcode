# 48. Rotate Image

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

#brute force
def matrotate(matrix):
    n=len(matrix)
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[j][n-1-i] = matrix[i][j]
    return ans
matrix = [[1,2,3],[4,5,6],[7,8,9]]
ans = matrotate(matrix)
print(ans)      

#optimal 
def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        rev(matrix[i])
    return matrix
def rev(arr):
    l=0
    r=len(arr)-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
matrix = [[1,2,3],[4,5,6],[7,8,9]]
ans = rotate(matrix)
print(ans)

