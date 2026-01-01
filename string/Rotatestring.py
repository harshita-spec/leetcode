# Rotate String

# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.
# Examples:
# Input : s = "abcde" , goal = "cdeab"
# Output : true
# Explanation :
# After performing 2 shifts we can achieve the goal string from string s.
# After first shift the string s is => bcdea
# After second shift the string s is => cdeab.
# Input : s = "abcde" , goal = "adeac"
# Output : false
# Explanation :
# Any number of shift operations cannot convert string s to string goal.

def rotate(s1,s2):
    if len(s1)==len(s2):
        s=s1+s1
        if s2 in s:
            return  True
        else:
            return False
    else:
        return False
s1 = "abcde" 
s2 = "cdeab"
print(rotate(s1,s2))