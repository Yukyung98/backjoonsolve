from collections import deque
def bfs(start,computers,N,visited):
    queue = deque()
    queue.append(start)
    
    while queue:
        node = queue.popleft()
        visited[node] = 1
        for i in range(N):
            if computers[node][i] == 1 and visited[i] != 1 :
                visited[i] = 1
                queue.append(i)
            
def solution(n, computers):
    visited =[0]*n
    answer = 0
    for i in range(n):
        if visited[i] == 0:  # 아직 방문하지 않은 노드에 대해 BFS 호출
            bfs(i, computers, n, visited)
            answer += 1
    return answer
