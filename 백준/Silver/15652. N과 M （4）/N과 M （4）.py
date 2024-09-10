

# 입력 받기
N, M = map(int, input().split())
visited = [False]*(N+1)
co=[]
def dfs(start):
    if len(co) == M:
        print(' '.join(map(str,co)))
        return
    for i in range(start,N+1):
        co.append(i)
        dfs(i)
        co.pop()
dfs(1)