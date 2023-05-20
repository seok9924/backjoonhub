from itertools import permutations
n,m= map(int,input().split())


x=[i for i in range(1,n+1)]
if m==1:
    for i in x:
        print(i)

else:
    for i in permutations(x,m):
        for j in i:
            print(j,end=" ")
        print()