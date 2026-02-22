# Sum Of Digits

# Given a positive number n. Find the sum of all the digits of n.

# Examples:
# Input: n = 687
# Output: 21
# Explanation: Sum of 687's digits: 6 + 8 + 7 = 21
# Input: n = 12
# Output 3
# Explanation: Sum of 12's digits: 1 + 2 = 3

def sumOfDigits(n):
    sum=0
    while n>0:
        res=n%10
        n=n//10
        sum+=res
    return sum
n=687
print(sumOfDigits(n))