from collections import deque

def bfs(start, visited, computers, n):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        
        for i in range(n):
            # 연결되어 있고, 아직 방문하지 않은 컴퓨터 탐색
            if computers[node][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)

def solution(n, computers):
    visited = [False] * n
    count = 0
    
    for i in range(n):
        if not visited[i]:
            bfs(i, visited, computers, n)
            count += 1  # 새로운 네트워크 발견 시 카운트 증가
    
    return count
