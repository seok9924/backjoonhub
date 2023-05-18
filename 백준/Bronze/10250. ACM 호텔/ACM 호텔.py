t=int(input())
for i in range(t):
    h,w,n=map(int,input().split())
    first=n%h
    next=n//h+1
    if n%h==0:
        next=n//h
        first=h
    print(f'{first*100+next}')
