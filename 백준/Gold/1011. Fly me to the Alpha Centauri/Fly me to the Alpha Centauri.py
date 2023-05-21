t=int(input())

for i in range(t):
    x,y=map(int,input().split())
    distance=y-x
    count=0
    k=1
    while distance>0:
        distance-=k
        count+=1
        if distance>0:
            distance-=k
            count+=1
        else:
            break
        k+=1
    print(count)