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