def solution(myStr):
    change=myStr.replace('b','c')
    change=change.replace('a','c')
    x=change.split('c')
    d=[]
    for i in x:
        if len(i)==0:
            continue
        else:
            d.append(i)
    if len(d)==0:
        return ["EMPTY"]
    else:
        return d
