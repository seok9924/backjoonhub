from collections import defaultdict
def solution(clothes):
    d=defaultdict(int)
    for c in clothes:
        wear,wear_type=c[0],c[1]
        d[wear_type]+=1
    total=0
    for v in d.values():
        total=total+v+total*v
    return total