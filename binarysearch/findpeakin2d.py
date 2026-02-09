# Find Peak Element - II

# Given a 0-indexed n x m matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the array [i, j].A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbours to the left, right, top, and bottom.
# Assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.
# Note: As there can be many peak values, 1 is given as output if the returned index is a peak number, otherwise 0.
# Examples:
# Input: mat=[[10, 20, 15], [21, 30, 14], [7, 16, 32]]
# Output: [1, 1]
# Explanation: The value at index [1, 1] is 30, which is a peak element because all its neighbours are smaller or equal to it. Similarly, {2, 2} can also be picked as a peak.
# Input: mat=[[10, 7], [11, 17]]
# Output : [1, 1]
# Explanation:The value at index [1, 1] is 17, which is the only peak element because all its neighbours are smaller or equal to it.

def peak(matrix,n,m):
    low=0
    high=m-1
    while low<=high:
        mid=(low+high)//2
        row=maxele(matrix,n,m,mid)
        left = matrix[row][mid - 1] if mid - 1 >= 0 else float('-inf')
        right = matrix[row][mid + 1] if mid + 1 < m else float('-inf')
        if matrix[row][mid]>left and matrix[row][mid]>right:
            return [row, mid]
        elif matrix[row][mid]<left:
            high=mid-1
        else:
            low=mid+1
    return [-1,-1]
def maxele(mat,n,m,mid):
    maxvalue=-1
    index=-1
    for i in range(n):
        if mat[i][mid]>maxvalue:
            maxvalue=mat[i][mid]
            index=i
    return index
matrix=[[10, 20, 15], [21, 30, 14], [7, 16, 32]]
n=len(matrix)
m=len(matrix[0])
result=peak(matrix,n,m)
print(result)