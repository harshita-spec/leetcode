# Merge Sort

# Merge sort is a popular sorting algorithm known for its efficiency and stability. It follows the Divide and Conquer approach. It works by recursively dividing the input array into two halves, recursively sorting the two halves and finally merging them back together to obtain the sorted array.

# arr_
# Here's a step-by-step explanation of how merge sort works:

# Divide: Divide the list or array recursively into two halves until it can no more be divided.
# Conquer: Each subarray is sorted individually using the merge sort algorithm.
# Merge: The sorted subarrays are merged back together in sorted order. The process continues until all elements from both subarrays have been merged.
# Let's sort the array or list [38, 27, 43, 10] using Merge Sort

# Let's look at the working of above example: 

# Divide: 
# [38, 27, 43, 10]  is divided into  [38, 27] and  [43, 10]  . 
# [38, 27]  is divided into  [38]  and  [27]  . 
# [43, 10]  is divided into  [43]  and  [10]  . 
# Conquer: 
# [38]  is already sorted. 
# [27]  is already sorted. 
# [43]  is already sorted. 
# [10]  is already sorted. 
# Merge: 
# Merge  [38]  and  [27]  to get  [27, 38]  . 
# Merge  [43]  and  [10]  to get  [10,43]  . 
# Merge  [27, 38]  and  [10,43]  to get the final sorted list  [10, 27, 38, 43] 
# Therefore, the sorted list is  [10, 27, 38, 43]  

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
