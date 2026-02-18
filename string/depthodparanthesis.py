# Maximum Nesting Depth of the Parentheses

# A string s is a valid parentheses string (VPS) if it meets the following conditions:
# It only contains digits 0-9, arithmetic operators +, -, *, /, and parentheses (, ).
# The parentheses are balanced and correctly nested.

# Your task is to compute the maximum nesting depth of parentheses in s. The nesting depth is the highest number of parentheses that are open at the same time at any point in the string.
# Examples:
# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3
# Explanation: The deepest nested sub-expression is ((8)/4), which has 3 layers of parentheses.

# Input: s = "(1)+((2))+(((3)))"
# Output: 3
# Explanation: The digit '3' is enclosed in 3 pairs of parentheses.

def depthparanthesis(s):
    stack=[]
    count=0
    maxcount=0
    n=len(s)
    for i in range(n):
        if s[i]=='(':
            stack.append(s[i])
            count+=1
            if count>maxcount:
                maxcount=count
        elif s[i]==")":
            stack.pop()
            count-=1
    return maxcount
s =  "(1+(2*3)+((8)/4))+1"
print(depthparanthesis(s))