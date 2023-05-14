from collections import defaultdict

d=defaultdict(int)
a=set()
s=input().lower()


for i in s:
    a.add(i)
    d[i]+=1

maxvalue=max(d.values())
count=0
idx=0
for i in a:
    if d[i]==maxvalue:
       count+=1
       idx=i


if count==1:
    print(idx.upper())
else:
    print("?")