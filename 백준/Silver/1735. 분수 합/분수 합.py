def gcd(a,b):
    if b!=1 and a%b==0:
        return b
    if b==1:
        return b
    else:
        return gcd(b,a%b)


bunso=[]
for i in range(2):
    a,b=map(int,input().split())
    bunso.append((b,a))
bunso.sort()
so=gcd(bunso[1][0],bunso[0][0])
k=bunso[1][0]*bunso[0][0]//so
ak=k//bunso[1][0]*bunso[1][1]+k//bunso[0][0]*bunso[0][1]
ko=0
if ak>k:
    ko=gcd(ak,k)
else:
    ko=gcd(k,ak)
print(ak//ko,k//ko)