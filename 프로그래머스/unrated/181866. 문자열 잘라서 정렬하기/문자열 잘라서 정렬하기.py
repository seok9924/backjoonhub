def solution(myString):
    a=myString.strip().split('x')
    while "" in a:
        a.remove("")
    return sorted(a)