# Sort Characters by Frequency
# You are given a string s. Return the array of unique characters, sorted by highest to lowest occurring characters.
# If two or more characters have same frequency then arrange them in alphabetic order.
# Examples:
# Input : s = "tree"
# Output : ['e', 'r', 't' ]
# Explanation :
# The occurrences of each character are as shown below :
# e --> 2
# r --> 1
# t --> 1.
# The r and t have same occurrences , so we arrange them by alphabetic order.
# Input : s = "raaaajj"
# Output : ['a' , 'j', 'r' ]
# Explanation :
# The occurrences of each character are as shown below :
# a --> 4
# j --> 2
# r --> 1

from collections import Counter
def frequency(s):
    n = len(s)
    c = Counter(s)
    bucket = [[] for _ in range(n+1)]
    for ch, freq in c.items():
        bucket[freq].append(ch)
    res = ""
    for freq in range(n, -1, -1):
        for ch in bucket[freq]:
            res += ch * freq  
    return res
s = "tree"
print(frequency(s))
