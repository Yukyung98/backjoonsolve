  

# 입력 받기
N, M = map(int, input().split())
co=[]
def dfs(start):
    if len(co) == M:
        print(' '.join(map(str,co)))
    for i in range(start,N+1):
        if i not in co:
            co.append(i)
            dfs(i)
            co.pop()
dfs(1)