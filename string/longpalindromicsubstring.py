# Longest Palindromic Substring

# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"

def palindrome(s):
    n = len(s)
    longest = ""
    
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if substring == substring[::-1] and len(substring) > len(longest):
                longest = substring
    
    return longest

s = "cbbd"
print(palindrome(s))  

def palindrome(s):
    res = ""
    reslen = 0
    n = len(s)
    def string(l, r):
        nonlocal res, reslen
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > reslen:
                res = s[l:r+1]
                reslen = r - l + 1
            l -= 1
            r += 1

    for i in range(n):
        string(i, i)
        string(i, i+1)
    return res
s = "cbbd"
print(palindrome(s))  
