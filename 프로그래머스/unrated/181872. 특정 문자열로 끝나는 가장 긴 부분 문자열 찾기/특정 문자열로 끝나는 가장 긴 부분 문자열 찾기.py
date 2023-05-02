def solution(myString, pat):
    lpat=len(pat)
    a=0
    for i in range(0,len(myString)-lpat+1):
        if pat in myString[i:i+lpat]:
            a=i+lpat
    return myString[0:a]