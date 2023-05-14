n,m= map(int,input().split())
d=dict()
for i in range(1,n+1):
    d[i]=0
for i in range(m):
    s,e,ball=map(int,input().split())

    for i in range(s,e+1):
        d[i]=ball

for i in d.values():
    print(i, end=" ")
