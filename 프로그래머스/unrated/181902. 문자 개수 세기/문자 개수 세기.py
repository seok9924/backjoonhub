def solution(my_string):
    d={}
    
    
    for i in range(ord('A'),ord('Z')+1):
        d[chr(i)]=0
    for i in range(ord('a'),ord('z')+1):
        d[chr(i)]=0
        
    for i in my_string:
        d[i]+=1
        
    a= d.values()
    return list(a)

