import sys
from collections import deque
sys.setrecursionlimit(10**6)  # 재귀 깊이 설정
input = sys.stdin.readline

# 입력 받기
N, M, R = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}

# 간선 입력 받기
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 각 노드의 인접 리스트를 오름차순으로 정렬
for key in graph:
    graph[key].sort()

visited = [0] * (N+1)  # 방문 체크 배열
cnt = 1
def bfs(v):
    global cnt
    queue = deque([R])
    visited[v] = cnt  # 현재 노드 방문 처리
    while queue:
        node = queue.popleft()
        for x in graph[node]:
            if visited[x] == 0:
                cnt+=1
                visited[x] = cnt
                queue.append(x)
    
# DFS 실행
bfs(R)
for i in range(1,len(visited)):
    print(visited[i])
