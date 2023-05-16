from collections import deque

def solution(priorities, location):
    a=[]
    for i in range(len(priorities)):
        a.append((priorities[i],i))

    q=deque(a)
    count=1
    while q:
        temp=max(q)
        prior,idx=q.popleft()

        if temp[0]==prior:
            if location==idx:
                return count
                continue

        if prior<temp[0]:
            q.append((prior,idx))
            continue

        count+=1

