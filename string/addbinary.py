# 67. Add Binary

# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

def addbinary(a,b):
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        ans = []
        while i >= 0 or j >= 0 or carry:
            bit1 = int(a[i]) if i >= 0 else 0
            bit2 = int(b[j]) if j >= 0 else 0
            total = bit1 + bit2 + carry
            ans.append(str(total % 2))
            carry = total // 2
            i -= 1
            j -= 1
        return "".join(ans[::-1])   
a = "1010"
b = "1011"
print(addbinary(a,b))