# Swap Two Numbers

# Given two numbers a and b, the task is to swap them.

# Examples:

# Input: a = 2, b = 3
# Output: a = 3, b = 2

# Input: a = 20, b = 0
# Output: a = 0, b = 20

# Input: a = 10, b = 10
# Output: a = 10, b = 10

def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b

def swap2(a,b):
    a,b=b,a
    print("a=",a,"b=",b)
a=10
b=20
print(swap(a,b)) 
swap2(a,b)