n,m=map(int,input().split())
d=dict()

for i in range(1,n+1):
    d[i]=i
for i in range(m):
    a,b=map(int,input().split())
    d[a],d[b]=d[b],d[a]

for i in d.values():
    print(i,end=" ")