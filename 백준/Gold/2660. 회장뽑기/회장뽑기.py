from collections import deque

def bfs(start,numbers,graph):
    visited = [-1]*(numbers+1)
    visited[start] = 0
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i] == -1: # 아직 방문하지 않은 노드
                visited[i] = visited[node]+1
                queue.append(i)
    return max(visited[1:])


numbers = int(input())
graph = [[]for _ in range(numbers+1)]
while True:
    x,y = map(int, input().split())
    if x == -1 and y == -1:
        break
    else:
        graph[x].append(y)
        graph[y].append(x)
scores = []
for i in range(1,numbers+1):
    score = bfs(i,numbers,graph)
    scores.append(score)
min_score = min(scores)
candidates = [i+1 for i in range(numbers) if scores[i] == min_score]
print(min_score, len(candidates))
print(" ".join(map(str, candidates)))