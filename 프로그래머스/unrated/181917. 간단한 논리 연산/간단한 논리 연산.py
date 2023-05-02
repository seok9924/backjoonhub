def solution(x1, x2, x3, x4):
    if x1 or x2:
        a=True
    else:
        a=False
        
    if x3 or x4 :
        b= True
    else:
        b=False
    
    if a and b:
        return True
    else:
        return False