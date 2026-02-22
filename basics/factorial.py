# Factorial of a Number
# Last Updated : 13 Jan, 2026
# Given the non-negative integers n , compute the factorial of a given number.
# Note: Factorial of n is defined as n * (n -1) * (n - 2) * ... * 1, for n = 0, factorial is 1.

# Examples:
# Input: n = 5
# Output: 120
# Explanation: 5! = 5 * 4 * 3 * 2 * 1 = 120

# Input: n = 4
# Output: 24
# Explanation: 4! = 4 * 3 * 2 * 1 = 24

def factorial(self, n: int) -> int:
        # code here
        fact=1
        for i in range(n,0,-1):
            fact=fact*i
        return fact
n=5
print(factorial(0,n))
