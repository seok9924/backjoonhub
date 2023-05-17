import math
def is_prime(x):
    if x==0 or x==1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True


n=1
while n!=0:
    n=int(input())
    count=0
    for i in range(n+1,2*n+1):
        if is_prime(i):
            count+=1
    if n!=0:
        print(count)
