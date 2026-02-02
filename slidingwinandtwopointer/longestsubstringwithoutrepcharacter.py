# Longest Substring Without Repeating Characters

# Given a string, S. Find the length of the longest substring without repeating characters.
# Example 1
# Input : S = "abcddabac"
# Output : 4
# Explanation : The answer is "abcd" , with a length of 4.
# Example 2
# Input : S = "aaabbbccc"
# Output : 2
# Explanation : The answers are "ab" , "bc". Both have maximum length 2.

def substring(s):
    maxlen=0
    for i in range(len(s)):
        hash=[0]*256
        for j in range(i,len(s)):
            if hash[ord(s[j])]==1:
                break
            leng=j-i+1
            maxlen=max(leng,maxlen)
            hash[ord(s[j])]=1
    return maxlen
s="abcddabac"
result=substring(s)
print(result)