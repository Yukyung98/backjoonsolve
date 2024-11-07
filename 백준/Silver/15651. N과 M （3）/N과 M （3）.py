  

# 입력 받기
N, M = map(int, input().split())
co=[]
def dfs(start):
    if len(co) == M:
        print(' '.join(map(str,co)))
        return
    for i in range(1,N+1):
        co.append(i)
        dfs(i)
        co.pop()
        
dfs(1)