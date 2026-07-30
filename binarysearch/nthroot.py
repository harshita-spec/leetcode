# Find Nth root of a number

# Given two numbers N and M, find the Nth root of M. The Nth root of a number M is defined as a number X such that when X is raised to the power of N, it equals M. If the Nth root is not an integer, return -1.
# Examples:
# Input: N = 3, M = 27
# Output: 3
# Explanation: The cube root of 27 is equal to 3.
# Input: N = 4, M = 69
# Output:-1
# Explanation: The 4th root of 69 does not exist. So, the answer is -1.
def nthroot(n,m):
    low=1
    high=m
    while low<=high:
        mid=(low+high)//2
        mid1=fun(mid,n,m)
        if mid1==1:
            return mid
        elif mid1==0:
            low=mid+1
        else:
            high=mid-1
    return -1
def fun(mid,n,m):
    ans=1
    for i in range(n):
        ans=ans*mid
        if ans>m:
            return 2
    if ans==m:
        return 1
    return 0
n=3
m=27
result=nthroot(n,m)
print(result)