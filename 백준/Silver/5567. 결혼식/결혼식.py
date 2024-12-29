from collections import deque
import copy
n = int(input())  # 동기의 수
m = int(input())  # 친구 관계 수
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def bfs(start):
    visitied = [False]*(n+1)
    queue = deque([(start,0)]) # (노드, 깊이)
    visitied[start]=True
    invited_count = 0
    while queue:
        current, depth = queue.popleft()
        if depth >= 2:
            continue
        for ne in graph[current]:
            if not visitied[ne]:
                visitied[ne] = True
                invited_count +=1
                queue.append((ne,depth+1))
    return invited_count
print(bfs(1))