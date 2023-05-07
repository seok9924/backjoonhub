from collections import  deque
n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx=[0,0,1,-1]
dy=[-1,1,0,0]

time=0

x,y,size=0,0,2

for i in range(n):
    for j in range(n):
        if graph[i][j]==9:
            x=i
            y=j


def eat(x,y,size):
    distance=[[0]*n for _ in range(n)]
    visited=[[0]* n for _ in range(n)]
    q=deque()
    q.append((x,y))
    visited[x][y]=1
    temp=[]

    while q:
        curx,cury=q.popleft()

        for i in range(4):
            nx=curx+dx[i]
            ny=cury+dy[i]

            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                if graph[nx][ny]<=size:
                    q.append((nx,ny))
                    visited[nx][ny]=1
                    distance[nx][ny]=distance[curx][cury]+1
                if graph[nx][ny]<size and graph[nx][ny]!=0:
                    temp.append((nx,ny,distance[nx][ny]))
    return sorted(temp,key=lambda x:(-x[2],-x[0],-x[1]))


result=0

while True:
    shark=eat(x,y,size)
    if len(shark)==0:
        break

    nx,ny,dist=shark.pop()
    result+=dist
    graph[x][y],graph[nx][ny]=0,0
    x,y=nx,ny
    time+=1
    if time==size:
        size+=1
        time=0

print(result)