from collections import deque
def bfs(start,target,graph,N):
    queue = deque([(start,0)]) # 현재노드, 누적 거리
    visited = [-1]*(N+1)
    visited[start]=0
    while queue:
        node, dist = queue.popleft()

        if node == target:
            return dist
         
        for next_node, weight in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = dist+weight
                queue.append((next_node,dist+weight))
    return -1


N,M = map(int, input().split())
graph = [[ ] for _ in range(N+1)]
for _ in range(N-1):
    node1, node2 , distance = map(int, input().split())
    graph[node1].append((node2, distance))
    graph[node2].append((node1, distance))
for _ in range(M):
    node1,node2 = map(int, input().split())
    result = bfs(node1, node2, graph, N)
    print(result)
