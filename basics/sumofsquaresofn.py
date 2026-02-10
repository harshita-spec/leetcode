# Program for Sum of squares of first n natural numbers

# Given a positive integer n, we have to find the sum of squares of first n natural numbers. 
# Examples : 

# Input : n = 2
# Output: 5
# Explanation: 1^2+2^2 = 5

# Input : n = 8
# Output: 204
# Explanation :  1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2 + 7^2 + 8^2 = 204 

def sumofsquares(n):
    sum=0
    for i in range(n+1):
        sum+=(i**2)
    return sum
n=8
print(sumofsquares(n))