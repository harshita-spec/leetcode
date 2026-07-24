def reverse(arr,l,n):
    l=l
    r=n
    if l>=r:
        return 
    arr[l],arr[r]=arr[r],arr[l]
    reverse(arr,l+1,r-1)
    return arr
arr=[1,2,3,4,5]
l=0
n=len(arr)
print(reverse(arr,l,n-1))
