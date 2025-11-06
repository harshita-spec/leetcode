# Reverse every word in a string

# Given an input string, containing upper-case and lower-case letters, digits, and spaces( ' ' ). A word is defined as a sequence of non-space characters. The words in s are separated by at least one space.

# Return a string with the words in reverse order, concatenated by a single space.
# Examples:
# Input: s = "welcome to the jungle"

# Output: "jungle the to welcome"

# Explanation: The words in the input string are "welcome", "to", "the", and "jungle". Reversing the order of these words gives "jungle", "the", "to", and "welcome". The output string should have exactly one space between each word.
# Input: s = " amazing coding skills "

# Output: "skills coding amazing"

def reverseWords(s):
    s = s.strip()       
    n = len(s)
    result = []
    i = n - 1

    while i >= 0:
        while i >= 0 and s[i] == ' ':
            i -= 1
        if i < 0:
            break
        j = i
        while i >= 0 and s[i] != ' ':
            i -= 1
        word = s[i + 1:j + 1]
        result.append(word)

    return ' '.join(result)
s = "welcome to the jungle"
print(reverseWords(s))  
    