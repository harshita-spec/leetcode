# Next Smaller Element

# Given an array of integers arr, your task is to find the Next Smaller Element (NSE) for every element in the array.
# The Next Smaller Element for an element x is defined as the first element to the right of x that is smaller than x.
# If there is no smaller element to the right, then the NSE is -1.

# Example 1
# Input: arr = [4, 8, 5, 2, 25]
# Output: [2, 5, 2, -1, -1]
# Explanation:
# - For 4, the next smaller element is 2.
# - For 8, the next smaller element is 5.
# - For 5, the next smaller element is 2.
# - For 2, there is no smaller element to its right → -1.
# - For 25, no smaller element exists → -1.

# Example 2
# Input: arr = [10, 9, 8, 7]
# Output: [9, 8, 7, -1]
# Explanation:
# Each element’s next right neighbor is smaller.

# brute force approach
def nextsmallerelement(arr):
    n=len(arr)
    nse=[0]*n
    for i in range(n):
        for j in range(i+1,n):
            if arr[j]<arr[i]:
                nse[i]=arr[j]
                break
        else:
            nse[i]=-1
    return nse
arr = [4, 8, 5, 2, 25]
print(nextsmallerelement(arr))

#optimal approach
def nextsmallerele(arr):
    n=len(arr)
    nse=[0]*n
    st=[]
    for i in range(n-1,-1,-1):
        while st and st[-1]>=arr[i]:
            st.pop()
        if st:
            nse[i]=st[-1]
        else:
            nse[i]=-1
        st.append(arr[i])
    return nse
arr = [10, 9, 8, 7]
print(nextsmallerele(arr))
