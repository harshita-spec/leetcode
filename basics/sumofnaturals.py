# Program for sum of n natural numbers

# Given a positive integer n, find the sum of the first n natural numbers.

# Examples : 

# Input: n = 3
# Output: 6
# Explanation: 1 + 2 + 3 = 6

# Input: n = 5
# Output: 15 
# Explanation:  1 + 2 + 3 + 4 + 5 = 15

def sumofnaturals(n):
    sum=0
    for i in range(n+1):
        sum+=i
    return sum

def summ(n):
    return (n*(n+1))//2
n=6
print(sumofnaturals(n))
m=5
print(summ(m))