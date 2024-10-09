import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N,M = map(int,input().split())
miro = []
for i in range(N):
    miro.append(input().strip())
cnt  = 0
for i in miro:
    if 'X' not in i:
        cnt +=1
cnt2 = 0
for i in range(M):
    xt = 0
    for j in range(N):
        if miro[j][i] == ".":
            xt+=1
    if xt == N:
        cnt2 +=1

print(max(cnt,cnt2))