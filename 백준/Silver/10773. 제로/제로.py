n=int(input())
s=[]
for i in range(n):
    m=int(input())
    if m==0 and not s:
        s.append(m)
    elif m==0 and s:
        s.pop()
    else:
        s.append(m)

if len(s)==0:
    print(0)
else:
    print(sum(s))