def dfs(k,cnt,dungeons):
    max_cnt = cnt  
    for x in range(n):
        if k >= dungeons[x][0] and not visited[x]:
            visited[x] = True
            max_cnt = max(max_cnt, dfs(k - dungeons[x][1], cnt + 1, dungeons))
            visited[x] = False
    return max_cnt  
def solution(k, dungeons):
    answer = -1
    global n,visited
    n = len(dungeons)
    visited = [0]*n
    return dfs(k,0,dungeons)

