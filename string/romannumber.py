# Roman to Integer

# Roman numerals are represented by seven different symbols:
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

# Roman numerals are typically written from largest to smallest, left to right. However, in specific cases, a smaller numeral placed before a larger one indicates subtraction.

# The following subtractive combinations are valid:
# I before V (5) and X (10) → 4 and 9
# X before L (50) and C (100) → 40 and 90
# C before D (500) and M (1000) → 400 and 900

# Given a Roman numeral, convert it to an integer.
# Examples:
# Input: s = "III"
# Output: 3
# Explanation: III = 1 + 1 + 1 = 3
# Input: s = "XLII"
# Output: 42
# Explanation: XL = 40, II = 2 → 40 + 2 = 42
# Input: s = "DCCCXC"
# 890
# 990
# 1090
# 840

def roman(s):
    roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    res=0
    for i in range(len(s)):
        if i+1<len(s) and roman[s[i]]<roman[s[i+1]]:
            res-=roman[s[i]]
        else:
            res+=roman[s[i]]
    return res
s = "XLII"
print(roman(s))