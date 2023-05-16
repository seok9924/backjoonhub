n,k =map(int,input().split())
nk=list(map(int,input().split()))
nk=sorted(nk,key=lambda x:-x)
coi=[]
for i in range(k):
    coi.append(nk[i])
print(coi[-1])