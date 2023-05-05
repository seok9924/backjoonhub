from itertools import combinations

n,m =map(int,input().split())
data=list(map(int,input().split()))

a=list(combinations(data,3))
b=[]
for i in a:
    if sum(i)<=m:
        b.append(sum(i))
print(max(set(b)))