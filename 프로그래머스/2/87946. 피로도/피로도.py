def dfs(k,dungeons,visited,count):
    max_count = count
    for i in range(len(dungeons)):
        min_required, consumption = dungeons[i]
        if not visited[i] and k >= min_required:
            visited[i] = True
            max_count = max(max_count, dfs(k - consumption, dungeons, visited, count + 1))
            visited[i] = False
    return max_count

            
def solution(k, dungeons):
    answer = -1
    visited = [False]*len(dungeons)
    count = 0
    dfs(k,dungeons,visited,count)
    
    return dfs(k,dungeons,visited,count)