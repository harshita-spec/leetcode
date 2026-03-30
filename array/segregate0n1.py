# Segregate 0s and 1s

# Given an array arr consisting of only 0's and 1's in random order. Modify the array in-place to segregate 0s onto the left side and 1s onto the right side of the array.
# Examples :
# Input: arr[] = [0, 0, 1, 1, 0]
# Output: [0, 0, 0, 1, 1]
# Explanation:  After segregation, all the 0's are on the left and 1's are on the right. Modified array will be [0, 0, 0, 1, 1].
# Input: arr[] = [1, 1, 1, 1]
# Output: [1, 1, 1, 1]
# Explanation: There are no 0s in the given array, so the modified array is [1, 1, 1, 1]
# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

def segregate(arr):
    left=0
    right=len(arr)-1
    while left<right:
        while arr[left]==0 and left<right:
            left+=1
        while arr[right]==1 and left<right:
            right-=1
        if left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
    return arr
arr=[0, 0, 1, 1, 0]
result=segregate(arr)
print(result)