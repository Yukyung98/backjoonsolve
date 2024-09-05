import sys
from collections import deque
input = sys.stdin.read
data = input().strip().splitlines()

M, N = map(int, data[0].split())

maps = [list(map(int, row.split())) for row in data[1:]]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()

for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            queue.append((i,j))
def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 상자 범위 안에 있고, 아직 익지 않은 토마토(0)인 경우
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 0:
                maps[nx][ny] = maps[x][y] + 1  # 이전 칸의 값에 1을 더해주어 날짜를 기록
                queue.append((nx, ny))
bfs()

max_days = 0
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:  # 아직 익지 않은 토마토가 있다면 -1 출력
            print(-1)
            sys.exit()
        max_days = max(max_days, maps[i][j])
print(max_days - 1)