while True:
    x=input()
    if x=="0 W 0":
        break

    else:
        a,oper,b=x.split()
        if oper=="W":
            k=int(a)-int(b)
        else:
            k=int(a)+int(b)

        if k<-200:
            print("Not allowed")
        else:
            print(k)
