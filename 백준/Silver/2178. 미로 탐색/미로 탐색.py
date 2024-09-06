from collections import deque

N,M = map(int,input().split())
maps = [list(map(int,input().strip())) for _ in range(N)]

def bfs(start_x,start_y,maps):
    queue = deque()
    queue.append((start_x,start_y))

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]

            if 0<=nx<N and 0<=ny<M and maps[nx][ny] == 1:
                maps[nx][ny] += maps[x][y]
                queue.append((nx,ny))
    return maps[N-1][M-1]

print(bfs(0,0,maps) )

        