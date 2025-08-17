# Largest Element

# Given an array of integers nums, return the value of the largest element in the array
# Examples:
# Input: nums = [3, 3, 6, 1]
# Output: 6
# Explanation: The largest element in array is 6
# Input: nums = [3, 3, 0, 99, -40]
# Output: 99
# Explanation: The largest element in array is 99

def array(a):
    largest=a[0]
    for i in range(1,len(a)):
        if largest<a[i]:
            largest=a[i]
    return largest
