# Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".
# Examples:
# Input : str = ["flowers" , "flow" , "fly", "flight" ]
# Output : "fl"
# Explanation :
# All strings given in array contains common prefix "fl".
# Input : str = ["dog" , "cat" , "animal", "monkey" ]
# Output : ""
# Explanation :
# There is no common prefix among the given strings in array.

def largecommon(s):
    if not s:
        return ""
    s.sort()
    f=s[0]
    l=s[-1]
    ans=[]
    for i in range(min(len(f),len(l))):
        if f[i]!=l[i]:
            return ''.join(ans)
        ans.append(f[i])
    return ''.join(ans)
s=["flowers" , "flow" , "floy", "floght" ]
print(largecommon(s))
