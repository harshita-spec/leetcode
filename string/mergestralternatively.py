# 1768. Merge Strings Alternately

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d

def merge(word1,word2):
        n=len(word1)
        m=len(word2)
        ans=[0]*(n+m)
        i=0
        j=0
        idx=0
        while i<n and j<m:
            ans[idx]=word1[i]
            idx+=1
            ans[idx]=word2[j]
            idx+=1
            i+=1
            j+=1
        while i<n:
            ans[idx]=word1[i]
            idx+=1
            i+=1
        while j<m:
            ans[idx]=word2[j]
            idx+=1
            j+=1
        return "".join(ans)
word1 = "abcd"
word2 = "pq"
print(merge(word1,word2))