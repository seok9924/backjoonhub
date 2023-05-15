while True:
    n=int(input())
    if n==-1:
        break
    a=[]
    for i in range(1,n):

        if n%i==0:
            a.append(i)

    if sum(a)==n:
        print(f"{n} = ",end='')
        for ao in range(len(a)-1):
            print(a[ao],"+",end=' ')
        print(a[-1],end="")
    else:
        print(f"{n} is NOT perfect.",end="")
    print()