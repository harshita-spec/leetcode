def cow(arr,cows):
    arr=sorted(arr)
    low=0
    n=len(arr)
    high=arr[n-1]-arr[0]
    while low<=high:
        mid=(low+high)//2
        if (cwp(arr,mid,cows)==True):
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans
def cwp(arr,dist,cows):
    cntcow=1
    last=arr[0]
    for i in range(1,len(arr)):
        if (arr[i]-last) >=dist:
            cntcow+=1
            last=arr[i]
        if cntcow>=cows:
            return True
    return False
arr=[0,3,4,7,10,9]
cows=4
result=cow(arr,cows)
print(result)