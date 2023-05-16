n=int(input())
a=[]
for i in range(n):
    x,y=input().split()
    a.append((int(x),y,i))
a=sorted(a,key=lambda x:(x[0],x[2]))
for i in a:
    print(i[0],i[1])