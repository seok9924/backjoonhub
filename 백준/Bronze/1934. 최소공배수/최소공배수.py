def gcd(a,b):
    if b!=1 and a%b==0:
        return b
    if b==1:
        return b
    else:
        return gcd(b,a%b)


n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if a<b:
        a,b=b,a
    so=gcd(a,b)
    print(a*b//so)