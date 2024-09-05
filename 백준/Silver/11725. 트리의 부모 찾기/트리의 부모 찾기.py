from collections import deque
def BFS(start):
    queue = deque([start])
    visited[start]=start
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i]=v
                queue.append(i)
node = int(input())
graph = [[] for _ in range(node+1)]
visited = [0]*(node+1)
for _ in range(node-1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
BFS(1)
for i in visited[2:]:
    print(i)