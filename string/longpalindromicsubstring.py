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
print(palindrome(s))  # Output: "bb"
