def factorial(n):
    if n ==1 or n==0:
        return 1

    else:
        return factorial(n-1)*n

n,m=map(int,input().split())
ans=factorial(n)//factorial(n-m)//factorial(m)
print(ans)