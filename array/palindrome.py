# 9. Palindrome Number

# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
def ispalindrome(x):
        x=str(x)
        left=0
        right=len(x)-1
        while left<=right:
            if x[left]!=x[right]:
                return False
            left+=1
            right-=1
        return True  
x=121
print(ispalindrome(x))  

def palindrome(x):
    if x<0:
        return False
    temp = x
    rev = 0
    while x > 0:
        digit = x % 10
        rev = rev * 10 + digit
        x = x // 10
    return temp == rev
x=121
print(palindrome(x))