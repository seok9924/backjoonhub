from collections import defaultdict
def solution(participant, completion):
    
    
    d=defaultdict(int)
    for p in participant:
        d[p]+=1
        
    for c in completion:
        d[c]-=1
    
    for i,v in d.items():
        if v==1:
            return i