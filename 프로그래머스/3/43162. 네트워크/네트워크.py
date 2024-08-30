from collections import deque

def bfs(start, computers, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        for i in range(len(computers)):
            if not visited[i] and computers[node][i] == 1:
                visited[i] = True
                queue.append(i)

def solution(n, computers):
    visited = [False] * n
    network_count = 0
    
    for i in range(n):
        if not visited[i]:
            bfs(i, computers, visited)
            network_count += 1
            
    return network_count
