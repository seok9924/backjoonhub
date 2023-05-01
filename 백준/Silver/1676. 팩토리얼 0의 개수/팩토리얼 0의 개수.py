n=int(input())
count=0
for i in range(1,n+1):
    a=i
    while a%5==0:
#         print(a)
        count+=1
        a//=5
print(count)
            