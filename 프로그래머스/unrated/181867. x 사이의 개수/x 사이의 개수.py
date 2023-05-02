def solution(myString):
    a=myString.split('x')
    b=[]
    for i in a:
       b.append(len(i)) 
    return b