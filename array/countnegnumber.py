# 1351. Count Negative Numbers in a Sorted Matrix

# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

# Example 1:
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:
# Input: grid = [[3,2],[1,0]]
# Output: 0

def countneg(grid):
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]<0:
                    count+=1
        return count
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countneg(grid))

def grids(grid):
        r = len(grid)
        c = len(grid[0])
        i = 0
        j = c-1
        count=0
        while i >= 0 and i < r and j >=0 and j < c:
            if grid[i][j] < 0:
                count += r - i
                j = j-1
            else:
                i = i+1
        return count
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(grids(grid))
