# Longest Repeating Character Replacement

# Given an integer k and a string s, any character in the string can be selected and changed to any other uppercase English character. This operation can be performed up to k times. After completing these steps, return the length of the longest substring that contains the same letter.
# Example 1
# Input : s = "BAABAABBBAAA" , k = 2
# Output : 6
# Explanation : we can change the B present at index 0 , 3 (0 base indexing) to A.
# The new string is "AAAAAABBBAAA".
# The substring "AAAAAA" is the longest substring having same letter with length 6.
# Example 2
# Input : s = "AABABBA" , k = 1
# Output : 4
# Explanation : The underlined characters are changed in the new string obtained.
# The new string is "AABBBBA". The substring "BBBB" is the answer.
# There are other ways to achieve this answer.

def characterReplacement( s, k):
        freq = {}
        left = 0
        max_freq = 0
        max_len = 0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(max_freq, freq[s[right]])
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
s="AABABBA"
k=3
result=characterReplacement(s,k)
print(result)
