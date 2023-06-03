import math

def prime_num(n):
    b=[]
    for i in range(2,n+1):
        flag=True
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                flag=False
                break
        if flag:
            b.append(i)
    return b

n=int(input())

x=prime_num(n)


left,right=0,0
value=0
count=0
while left<=right and right<(len(x)):

    if value==n:
        count+=1
        value-=x[left]
        left+=1
    if left==right:
       value=x[left]
       right+=1

    elif left<right:
        if value<n:
            value = x[right] + value
            right+=1
        else:
            value-=x[left]
            left+=1
    else:
        break
if n in x:
    count+=1
print(count)
