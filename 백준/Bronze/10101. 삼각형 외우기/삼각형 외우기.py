e="Equilateral"
iso="Isosceles"
sc="Scalene"
err="Error"

a=int(input())
b=int(input())
c=int(input())

d=[a,b,c]

if sum(d)!=180:
    print(err)
elif a==b and b==c and a==c:
    print(e)
elif a!=b and b!=c and a!=c:
    print(sc)
else:
    print(iso)