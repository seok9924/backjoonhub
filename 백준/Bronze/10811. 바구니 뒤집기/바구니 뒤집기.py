n,m=map(int, input().split())

alist=[x for x in range(1,n+1)]
for i in range(m):
    s,e=map(int,input().split())
    temp=alist[s-1:e]
    temp.reverse()
    alist[s-1:e]=temp
for i in alist:
    print(i, end= " ")