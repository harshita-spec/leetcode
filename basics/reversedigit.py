# Reverse digits

# You are given an integer n. Your task is to reverse the digits, ensuring that the reversed number has no leading zeroes.

# Examples:
# Input: n = 122
# Output: 221
# Explanation: By reversing the digits of number, number will change into 221.
# Input : n = 200
# Output: 2
# Explanation: By reversing the digits of number, number will change into 2.
# Input : n = 12345 
# Output: 54321
# Explanation: By reversing the digits of number, number will change into 54321.

def reversedigit(n):
    rev=0
    while n>0:
        res=n%10
        n=n//10
        rev=rev*10+res
    return rev
n=122
print(reversedigit(n))