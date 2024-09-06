import sys
from collections import deque

input = sys.stdin.read
data = input().strip().split()

r, c = int(data[0]), int(data[1])
maps = [list(data[i + 2]) for i in range(r)]

visited = set()
ans = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] not in visited:
            visited.add(maps[nx][ny])
            dfs(nx, ny, cnt + 1)
            visited.remove(maps[nx][ny])

visited.add(maps[0][0])
dfs(0, 0, 1)
print(ans)
