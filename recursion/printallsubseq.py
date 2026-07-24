def seq(arr,ind,ans,n):
    if ind >= n:
        print(ans)
        return
    ans.append(arr[ind])
    seq(arr,ind+1,ans,n)
    ans.remove(arr[ind])
    seq(arr,ind+1,ans,n)
arr=[3 ,2 ,1]
n=len(arr)
ans=[]
seq(arr,0,ans,n)