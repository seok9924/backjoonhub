import heapq


heap=[]

n=int(input())
numbers=[int(input()) for _ in range(n) ]

for i in numbers:
    if i==0 and heap:
        print(heapq.heappop(heap))
    elif i==0 and not heap:
        print(0)

    else:
        heapq.heappush(heap,i)