n=int(input())
nlist=list(map(int,input().split()))
m=int(input())
mlist=list(map(int,input().split()))

d=dict()
for i in nlist:
    d[i]=0
for j in mlist:
    if j in d:
        print(1,end=' ')
    else:
        print(0,end=' ')