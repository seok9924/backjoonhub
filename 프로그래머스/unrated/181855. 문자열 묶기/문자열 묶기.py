def solution(strArr):  
    d={}
    for i in range(31):
        d[i]=0
        
    for i in strArr:
        c=len(i)
        d[c]+=1
    return max(d.values())