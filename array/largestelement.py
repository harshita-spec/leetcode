# Second Largest Element

# Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.
# Examples:
# Input: nums = [8, 8, 7, 6, 5]
# Output: 7
# Explanation:
# The largest value in nums is 8, the second largest is 7
# Input: nums = [10, 10, 10, 10, 10]
# Output: -1
# Explanation:
# The only value in nums is 10, so there is no second largest value, thus -1 is returned

def num(arr,n):
    largest=arr[0]
    slargest=0
    for i in range(1,n):
        if arr[i]>largest:
            slargest=largest
            largest=arr[i]
        else:
            if arr[i]<largest and arr[i]>slargest:
                slargest=arr[i]
    return slargest
arr=[1,4,3,6,18,9]
n=len(arr)
result=num(arr,n)
print(result)
