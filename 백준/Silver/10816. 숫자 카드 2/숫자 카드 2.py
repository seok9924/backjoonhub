from collections import defaultdict
n= int(input())
nlist=list(map(int,input().split()))

m=int(input())
mlist=list(map(int,input().split()))

sangdict=defaultdict(int)

for nl in nlist:
    sangdict[nl]+=1

for ml in mlist:
    if ml in sangdict:
        print(sangdict[ml],end=' ')

    else:
        print(0, end=' ')

