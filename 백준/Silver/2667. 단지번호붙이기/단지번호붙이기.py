from collections import deque

def BFS(x1,y1):
    
    # 상 하 좌 우
    nx = [-1,1,0,0]
    ny = [0,0,-1,1]
    queue = deque()
    queue.append((x1,y1))
    maps[x1][y1] = 0
    cnt = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]

            if dx < 0  or dy <0 or dx>=n or dy>=n:
                continue
            if maps[dx][dy] == 0:
                continue
            if maps[dx][dy] == 1:
                maps[dx][dy] = 0
                queue.append((dx,dy))
                cnt +=1
    return cnt

n=int(input()) # 지도의 크기
maps = []
for _ in range(n):
    row = list(map(int, input().strip()))
    maps.append(row)
tt = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            tt.append(BFS(i,j))
tt.sort()
print(len(tt))
for i in tt:
    print(i,end="\n")