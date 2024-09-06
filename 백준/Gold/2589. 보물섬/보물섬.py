from collections import deque

N,M = map(int,input().split())
maps = [list(map(str,input().strip())) for _ in range(N)]

def bfs(start_x,start_y):
    queue = deque()
    queue.append((start_x,start_y))
    visited = [[-1]*M for _ in range(N)]
    visited[start_x][start_y] = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    max_distance = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]

            if 0<=nx<N and 0<=ny<M and maps[nx][ny] == "L"and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))
                max_distance = max(max_distance,visited[nx][ny])
    return max_distance
max_time = 0
for i in range(N):
    for j in range(M):
        if maps[i][j] == "L":
            max_time = max(max_time,bfs(i,j))

print(max_time)
        