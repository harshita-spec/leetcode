# 387. First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:
# Input: s = "leetcode"
# Output: 0
# Explanation:
# The character 'l' at index 0 is the first character that does not occur at any other index.
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
# Example 3:
# Input: s = "aabb"
# Output: -1

# Constraints:
# 1 <= s.length <= 105
# s consists of only lowercase English letters.

def firstunique(s):
        for i in range(len(s)):
            count=0
            for j in range(len(s)):
                if s[i]==s[j]:
                    count+=1
            if count == 1:
                return i
        return -1
s= "loveleetcode"
print(firstunique(s))

def unique(s):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        return -1
s = "leetcode"
print(unique(s))