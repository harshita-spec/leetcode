# Matrix Median

# Given a 2D array matrix that is row-wise sorted. The task is to find the median of the given matrix.
# Examples:
# Input: matrix=[[1, 4, 9],[2, 5, 6],[3, 7, 8]] 
# Output: 5
# Explanation: If we find the linear sorted array, the array becomes 1 2 3 4 5 6 7 8 9. So, median = 5
# Input: matrix=[[1, 3, 8],[2, 3, 4],[1, 2, 5]] 
# Output: 3
# Explanation: If we find the linear sorted array, the array becomes 1 1 2 2 3 3 4 5 8. So, median = 3

def findMedian(matrix):
    n = len(matrix)
    m = len(matrix[0])
    low = min(row[0] for row in matrix)
    high = max(row[-1] for row in matrix)
    req = (n * m) // 2

    while low <= high:
        mid = (low + high) // 2
        smallerequals = countLessEqual(matrix, mid, n)
        if smallerequals <= req:
            low = mid + 1
        else:
            high = mid - 1
    return low


def countLessEqual(matrix, target, n):
    count = 0
    for i in range(n):
        count += upperbound(matrix[i], target)
    return count


def upperbound(arr, target):
    n = len(arr)
    low, high = 0, n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
matrix = [[1, 4, 9], [2, 5, 6], [3, 7, 8]]
result = findMedian(matrix)
print(result) 
