def solution(my_string, m, c):
    
    b=[]
    ss=""
    for i in range(0,len(my_string),m):
            b.append(my_string[i:i+m])
            
    for i in b:
        ss+=i[c-1]
    return ss