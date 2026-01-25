# Largest Element

# Given an array of integers nums, return the value of the largest element in the array
# Examples:
# Input: nums = [3, 3, 6, 1]
# Output: 6
# Explanation: The largest element in array is 6
# Input: nums = [3, 3, 100, 99, -40]
# Output: 99
# Explanation: The largest element in array is 99

def array(a):
    largest=0
    for i in range(len(a)):
        if largest<a[i]:
            largest=a[i]
    return largest
a=[3, 3, 1000, 99, -40]
print(array(a))