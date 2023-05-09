n= int(input())
a=list(map(int,input().split()))
a.sort()
k=[0]*n
k[0]=a[0]
for i in range(1,n):
    k[i]=k[i-1]+a[i]
print(sum(k))