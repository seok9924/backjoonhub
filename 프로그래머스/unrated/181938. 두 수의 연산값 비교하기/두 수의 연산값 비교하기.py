def solution(a, b):
    oper=str(a)+str(b)
    back= 2*a*b
    if int(oper)>=back:
        return int(oper)
    else:
        return back