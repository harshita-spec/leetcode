# Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Examples:
# Input : s = "anagram" , t = "nagaram"
# Output : true
# Explanation :
# We can rearrange the characters of string s to get string t as frequency of all characters from both strings is same.
# Input : s = "dog" , t = "cat"
# Output : false
# Explanation :
# We cannot rearrange the characters of string s to get string t as frequency of all characters from both strings is not same.
from collections import Counter
def anagram(s,t):
    return Counter(s)==Counter(t)
s = "dog"
t = "dog"
print(anagram(s,t))