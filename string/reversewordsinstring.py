# Reverse every word in a string

# Given an input string, containing upper-case and lower-case letters, digits, and spaces( ' ' ). A word is defined as a sequence of non-space characters. The words in s are separated by at least one space.

# Return a string with the words in reverse order, concatenated by a single space.
# Examples:
# Input: s = "welcome to the jungle"

# Output: "jungle the to welcome"

# Explanation: The words in the input string are "welcome", "to", "the", and "jungle". Reversing the order of these words gives "jungle", "the", "to", and "welcome". The output string should have exactly one space between each word.
# Input: s = " amazing coding skills "

# Output: "skills coding amazing"

# Explanation: The input string has leading and trailing spaces, as well as multiple spaces between the words "amazing", "coding", and "skills". After trimming the leading and trailing spaces and reducing the multiple spaces between words to a single space, the words are "amazing", "coding", and "skills". Reversing the order of these words gives "skills", "coding", and "amazing". The output string should not have any leading or trailing spaces and should have exactly one space between each word.
# Input: s = "openAI is innovative"
# innovative is openAI

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
s = "  the sky   is blue  "
print(reverseWords(s))  