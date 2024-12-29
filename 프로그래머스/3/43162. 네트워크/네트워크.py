from collections import deque
def bfs(startNode,visitedGraph,computers):
    queue = deque([startNode])
    
    while queue:
        x = queue.popleft()
        for node in range(len(computers[x])):
            if computers[x][node] == 1 and not visitedGraph[node]:
                visitedGraph[node] = 1
                queue.append(node)
def solution(n, computers):
    visited = [0]*n
    answer = 0
    for i in range(n):
        if visited[i] == 0:
            bfs(i,visited,computers)
            answer+=1
    return answer