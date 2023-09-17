import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N,M,R = map(int,input().split()) # 정점,간선,시작
graph =[[]for _ in range(N+1)]
visite = [0]*(N+1) # 방문 확인
cnt =1

for _ in range(M) :
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
def dfs(v):
    global cnt
    visite[v] = cnt
    graph[v].sort()
    for g in graph[v]:
        if visite[g] == 0:
            cnt +=1
            dfs(g)
dfs(R)
for i in range(1,N+1):
    print(visite[i])