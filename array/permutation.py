# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1].

# The next permutation of an array of integers is the next lexicographically greater permutation of its integers.
# More formally, if all the permutations of the array are sorted in lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted order.

# If such arrangement is not possible (i.e., the array is the last permutation), then rearrange it to the lowest possible order (i.e., sorted in ascending order).

# You must rearrange the numbers in-place and use only constant extra memory.
# Examples:
# Input: nums = [1,2,3]
# Output: [1,3,2]
# Explanation: The next permutation of [1,2,3] is [1,3,2].
# Input: nums = [3,2,1]
# Output: [1,2,3]
# Explanation: [3,2,1] is the last permutation. So we return the first: [1,2,3].

def nextGreaterPermutation(A):
    n = len(A) 
    ind = -1 
    for i in range(n-2, -1, -1):
        if A[i] < A[i + 1]:
            ind = i
            break
    if ind == -1:
        A.reverse()
        return A
    for i in range(n - 1, ind, -1):
        if A[i] > A[ind]:
            A[i], A[ind] = A[ind], A[i]
            break
    A[ind+1:] = reversed(A[ind+1:])
    return A

A = [2, 1, 5, 4, 3, 0, 0]
ans = nextGreaterPermutation(A)
print("The next permutation is: [", end="")
for it in ans:
    print(it, end=" ")
print("]")
