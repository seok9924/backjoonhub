n= int(input())
a=list(map(int,input().split()))
find=int(input())
count=0
for i in a:
    if find==i:
       count+=1

print(count)