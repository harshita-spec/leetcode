# Search in a 2D matrix

# Given a 2-D array mat where the elements of each row are sorted in non-decreasing order, and the first element of a row is greater than the last element of the previous row (if it exists), and an integer target, determine if the target exists in the given mat or not.
# Examples:
# Input: mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ], target = 8
# Output: True
# Explanation: The target = 8 exists in the 'mat' at index (1, 3).
# Input: mat = [ [1, 2, 4], [6, 7, 8], [9, 10, 34] ], target = 78
# Output: False
# Explanation: The target = 78 does not exist in the 'mat'. Therefore in the output, we see 'false'.

def search(matrix,target):
    n = len(matrix)
    m = len(matrix[0])
    low=0
    high=(n*m-1)
    while low<=high:
        mid=(low+high)//2
        row=mid//m
        col=mid%m
        if matrix[row][col]==target:
            return True
        elif matrix[row][col]<target:
            low=mid+1
        else:
            high=mid-1
    return False
mat = [ [1, 2, 4], [6, 7, 8], [9, 10, 34] ]
target = 78
result=search(mat,target)
print(result)