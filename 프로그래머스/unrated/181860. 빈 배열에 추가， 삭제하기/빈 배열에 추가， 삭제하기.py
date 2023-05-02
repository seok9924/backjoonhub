def solution(arr, flag):
    a=[]
    for i,v in enumerate(arr):
        if flag[i]:
            for i in range(v*2):
                a.append(v)

        else:
            for i in range(v):
                a.pop()
    return a
                