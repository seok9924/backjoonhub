n,m=map(int,input().split())
nlist=[]
mlist=[]
d=dict()
for i in range(n):
    d[input()]=0
count=0
for i in range(m):
    if input() in d:
        count+=1

print(count)
