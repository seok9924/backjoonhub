from collections import defaultdict
d=defaultdict(int)
for i in range(65,91):
    d[i-55]=chr(i)
for i in range(0,10):
    d[i]=str(i)
n,m=map(int,input().split())
a=[]
while n>0:
    a.append(d[n%m])
    n//=m
print(''.join(reversed(a)))