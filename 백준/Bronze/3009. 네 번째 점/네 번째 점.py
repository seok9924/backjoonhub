from collections import defaultdict
d1=defaultdict(int)
d2=defaultdict(int)
for i in range(3):
    x,y=map(int,input().split())
    d1[x]+=1
    d2[y]+=1

a=[]
for i,v in d1.items():
    if v==1:
        a.append(i)
for i,v in d2.items():
    if v==1:
        a.append(i)

for i in a:
    print(i,end=" ")