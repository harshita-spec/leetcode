# Merge Overlapping Subintervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

# You can return the intervals in any order.
# Examples:
# Input: intervals = [[1,5],[3,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Intervals [1,5] and [3,6] overlap, so they are merged into [1,6].
# Input: intervals = [[5,7],[1,3],[4,6],[8,10]]
# Output: [[1,3],[4,7],[8,10]]
# Explanation: Intervals [4,6] and [5,7] overlap and are merged into [4,7].

def merged(arr):
    n=len(arr)
    arr=sorted(arr)
    ans=[]
    for i in range(n):
        if not ans or arr[i][0] > ans[-1][1]:
            ans.append(arr[i])
        else:
            ans[-1][1]=max(ans[-1][1],arr[i][1])
    return ans
arr=[[5,7],[1,3],[4,6],[8,10]]
result=merged(arr)
print(result)