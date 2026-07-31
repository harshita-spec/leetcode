# Selection Sort

# Selection Sort is a comparison-based sorting algorithm. It sorts by repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first unsorted element.

# Find the smallest element and swap it with the first element. This way we get the smallest element at its correct position.
# Then find the smallest among remaining elements (or second smallest) and swap it with the second element.
# We keep doing this until we get all elements moved to correct position.

def selection(arr):
    for i in range(len(arr)):
        mini=i
        for j in range(i,len(arr)):
            if arr[j]<arr[mini]:
                mini=j
        arr[i], arr[mini] = arr[mini], arr[i]
    return arr
arr=[13,46,24,52,20,9]
print(selection(arr))
