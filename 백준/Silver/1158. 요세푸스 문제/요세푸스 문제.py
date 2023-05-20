n,k= map(int,input().split())

arr=[x for x in range(1,n+1)]
ans=[]
num=0
for i in range(n):
    num+=(k-1)
    if num>=len(arr):
        num%=len(arr)
    ans.append(str(arr[num]))
    arr.pop(num)
print("<",', '.join(ans),">",sep="")