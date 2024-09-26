import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
    
N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 1
for _ in range(M):
    u, v  = map(int,input().split())
    if 1 <= u <= N and 1 <= v <= N:  
        graph[u].append(v)
        graph[v].append(u)
def bfs(startNode):
    global cnt
    queue= deque([R])
    visited[startNode] = cnt
    cnt +=1
    while queue:
        node = queue.popleft()
        graph[node].sort()
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = cnt
                cnt+=1
                queue.append(i)  
# 시작 정점이 범위 안에 있는지 확인
if 1 <= R <= N:
    bfs(R)
for i in range(1,N+1):
    print(visited[i])
