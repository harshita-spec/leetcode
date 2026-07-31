# Bubble Sort

# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not efficient for large data sets as its average and worst-case time complexity are quite high.

# Sorts the array using multiple passes. After the first pass, the maximum goes to end (its correct position). Same way, after second pass, the second largest goes to second last position and so on.
# In every pass, process only those that have already not moved to correct position. After k passes, the largest k must have been moved to the last k positions.
# In a pass, we consider remaining elements and compare all adjacent and swap if larger element is before a smaller element. If we keep doing this, we get the largest (among the remaining elements) at its correct position.

def bubble(arr):
    for i in range(len(arr)-1,-1,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[13,24,45,23,5,89,9]
print(bubble(arr))

def bubblee(arr):
    for i in range(len(arr)-1,-1,-1):
        didswap=0
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                didswap=0
        if didswap==1:
            break
    return arr
arr=[13,24,45,23,5,89,9]
print(bubblee(arr))