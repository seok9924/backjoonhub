def solution(ineq, eq, n, m):
    
    bonm=0
    if ineq==">":
        
        if eq=="=":
            if n>=m:
                bonm=1
            else: 
                bonm=0
            
            
        else:
            if n>m:
                bonm=1
            else: 
                bonm=0
            
            
        
        
    else:
        if eq=="=":
            if n<=m:
                bonm=1
            else: 
                bonm=0
            
            
        else:
            if n<m:
                bonm=1
            else: 
                bonm=0
    return bonm