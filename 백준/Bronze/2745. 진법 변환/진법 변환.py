from collections import defaultdict
d=defaultdict(int)
for i in range(65,91):
    d[chr(i)]=i-55
for i in range(1,10):
    d[str(i)]=i
n,m=input().split()
m=int(m)
total=0
square=0
for i in range(len(n)-1,-1,-1):
    total+=(m**square)*d[n[i]]
    square+=1
print(total)