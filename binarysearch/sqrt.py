# Find square root of a number

# Given a positive integer n. Find and return its square root. If n is not a perfect square, then return the floor value of sqrt(n).
# Examples:
# Input: n = 36
# Output: 6
# Explanation: 6 is the square root of 36.
# Input: n = 28
# Output: 5
# Explanation: The square root of 28 is approximately 5.292. So, the floor value will be 5.

# def squrt(n):
#     if n==0:
#         return 0
#     low=1
#     high=n
#     while low<=high:
#         mid=(low+high)//2
#         if (mid*mid)<=n:
#             ans=mid
#             low=mid+1
#         else:
#             high=mid-1
#     return ans
# n=1
# result=squrt(n)
# print(result)

def f(n):
    low=1
    high=n
    while low<=high:
        mid=(low+high)//2
        if mid*mid <= n:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans
n=9
result=f(n)
print(result)