# Quick Sort

# QuickSort is a sorting algorithm based on the Divide and Conquer that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array. .

# There are mainly three steps in the algorithm:

# Choose a Pivot: Select an element from the array as the pivot. The choice of pivot can vary (e.g., first element, last element, random element, or median).
# Partition the Array: Re arrange the array around the pivot. After partitioning, all elements smaller than the pivot will be on its left, and all elements greater than the pivot will be on its right.
# Recursively Call: Recursively apply the same process to the two partitioned sub-arrays.
# Base Case: The recursion stops when there is only one element left in the sub-array, as a single element is already sorted.

def quick(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while i<j:
        while i<=high and arr[i]<=pivot:
            i+=1
        while j>=low and arr[j]>pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j
def quicksort(arr,low,high):
    if(low<high):
        p=quick(arr,low,high)
        quicksort(arr,low,p-1)
        quicksort(arr,p+1,high)
arr=[4,6,2,5,7,9,1,3]
n=len(arr)
quicksort(arr,0,n-1)
print(arr)