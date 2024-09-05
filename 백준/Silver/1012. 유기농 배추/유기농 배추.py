from collections import deque

def BFS(x1,y1):
    
    # 상 하 좌 우
    nx = [-1,1,0,0]
    ny = [0,0,-1,1]
    queue = deque()
    queue.append((x1,y1))
    maps[x1][y1] = 0
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]

            if dx < 0  or dy <0 or dx>=M or dy>=N:
                continue
            if maps[dx][dy] == 0:
                continue
            if maps[dx][dy] == 1:
                maps[dx][dy] = 0
                queue.append((dx,dy))
    return 1

T = int(input()) #테스트 케이스
tt = []
for _ in range(T):
    M,N,K = map(int,input().split())
    maps = [[0] * N for _ in range(M)]
    for _ in range(K):
        x,y = map(int,input().split()) # 지렁이 위치
        maps[x][y] = 1
    cnt = 0
    for i in range(M):
        for k in range(N):
            if maps[i][k] == 1:
                cnt += BFS(i,k)
    tt.append(cnt)
for i in tt:
    print(i,end="\n")
