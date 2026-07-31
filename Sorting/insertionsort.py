# Insertion Sort Algorithm

# Insertion sort is a simple sorting algorithm that works by iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list. It is like sorting playing cards in your hands. You split the cards into two groups: the sorted cards and the unsorted cards. Then, you pick a card from the unsorted group and put it in the right place in the sorted group.

# Start with the second element as the first element is assumed to be sorted.
# Compare the second element with the first if the second is smaller then swap them.
# Move to the third element, compare it with the first two, and put it in its correct position
# Repeat until the entire array is sorted.

def insertion(arr):
    for i in range(len(arr)):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
    return arr
arr=[23,4,56,76,2,51,15]
print(insertion(arr))