from collections import deque

def bfs(start):
    queue = deque([start])
    visited[start]=True
    cnt = 0
    while queue:
        x = queue.popleft()
        cnt+=1
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    print(cnt-1)

n=int(input()) # 컴퓨터 개수
v=int(input()) # 연결선 개수
graph = [[] for _ in range(n+1)]
for _ in range(v):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in graph:
    i.sort()
visited = [False]*(n+1)
bfs(1)