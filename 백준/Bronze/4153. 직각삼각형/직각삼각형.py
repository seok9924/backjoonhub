while True:
    a,b,c=map(int,input().split())
    if a==0 :
        break
    else:
        triangle=max(a,b,c)**2
        total=a**2+b**2+c**2
        if triangle*2==total:
            print('right')
        else:
            print('wrong')