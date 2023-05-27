n = int(input())

def facorial(n):
    if n==1 or n==0:
        return 1
    
    else:
        return facorial(n-1)*n

print(facorial(n))