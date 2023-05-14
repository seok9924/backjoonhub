n,m=map(int,input().split())
alist=[x for x in range(1,n+1)]
for i in range(m):
    s,e,m=map(int,input().split())
    s-=1
    m-=1
    tmp=alist[m:e]
    tmp2=alist[s:m]
    alist[s:e]=tmp+tmp2

for i in alist:
    print(i, end=" ")