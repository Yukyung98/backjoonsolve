from collections import deque

def BFS(x1, y1, check, temp_maps):
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x1, y1))
    temp_maps[x1][y1] = 0  # Mark as visited
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if temp_maps[nx][ny] > check:
                temp_maps[nx][ny] = 0  # Mark as visited
                queue.append((nx, ny))
    return 1

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

max_safe_areas = 0

for k in range(101):  # Check all possible heights from 0 to 100
    temp_maps = [row[:] for row in maps]  # Create a copy of maps
    count = 0
    for i in range(N):
        for j in range(N):
            if temp_maps[i][j] > k:  # Cell is above the water level
                count += BFS(i, j, k, temp_maps)
    max_safe_areas = max(max_safe_areas, count)

print(max_safe_areas)
