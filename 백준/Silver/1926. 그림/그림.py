from collections import deque

# 이동 방향 설정 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x1,y1):
    queue = deque()
    queue.append((x1,y1))
    maps[x1][y1] = 0
    cnt = 1
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            if 0<= nx < N and 0<= ny < M and maps[nx][ny] == 1:
                maps[nx][ny] = 0
                queue.append((nx,ny))
                cnt+=1
    return cnt

# 입력 처리
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]  # 입력 처리
tt = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            tt.append(bfs(i,j))
# BFS 실행 및 결과 출력
if len(tt) == 0:
    print(0)
    print(0)
else:
    print(len(tt))
    print(max(tt))
