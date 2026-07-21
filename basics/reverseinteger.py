# 7. Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321
# Example 2:
# Input: x = -123
# Output: -321
# Example 3:
# Input: x = 120
# Output: 21
 
def reversedigit(x):
        ans=0
        sign = 1
        if x < 0:
            sign = -1
        x=abs(x)
        while x > 0:
            num = x % 10
            ans = (ans * 10)+ num
            x = x // 10
        if -(2**31 )<= (sign * ans) <= ((2**31)-1):
            return sign *ans
        else:
            return 0
        
x=123
print(reversedigit(x))