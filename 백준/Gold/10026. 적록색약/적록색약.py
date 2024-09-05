from collections import deque

def BFS(x1,y1,maps,word):
    
    # 상 하 좌 우
    nx = [-1,1,0,0]
    ny = [0,0,-1,1]
    queue = deque()
    queue.append((x1,y1))
    maps[x1][y1] = "S"
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]

            if dx < 0  or dy <0 or dx>=T or dy>=T:
                continue
            if maps[dx][dy] == word:
                maps[dx][dy] = "S"
                queue.append((dx,dy))
    return 1

T = int(input()) 
maps1 = [] # 일반인
copys = [] # 적록색약
for _ in range(T):
    row = list(map(str, input().strip()))
    maps1.append(row)
    copys.append([ch if ch != 'G' else 'R' for ch in row])

cnt1 = 0
cnt2 = 0
for i in range(T):
    for k in range(T):
        # 일반인용 탐색
        if maps1[i][k] == "R" or maps1[i][k] == "G" or maps1[i][k] == "B":
            cnt1 += BFS(i, k, maps1, maps1[i][k])

        # 적록색약용 탐색
        if copys[i][k] == "R" or copys[i][k] == "B":
            cnt2 += BFS(i, k, copys, copys[i][k])

print(cnt1,cnt2)