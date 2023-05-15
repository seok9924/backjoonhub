n=int(input())
a=[]
i=2
while n!=1:
    if n%i==0:
        n//=i
        a.append(i)
        continue

    i+=1

for i in a:
    print(i)