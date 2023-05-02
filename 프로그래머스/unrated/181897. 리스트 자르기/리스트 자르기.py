def solution(n, slicer, x):
    a,b,c=slicer
    d=[]
    if n ==1:
        return x[:b+1]
    
    if n==2:
        return x[a:]
    
    if n==3:
        return x[a:b+1]
    
    if n==4:
        
        for i in range(a,b+1,c):
            d.append(x[i])
            
        return d