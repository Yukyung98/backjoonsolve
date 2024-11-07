from collections import deque

def dfs2(visited, r, c):
    global check
    global count_temp

    if r < 0 or r >= 5 or c < 0 or c >= 5:
        return

    if visited[r][c] == 0:  
        visited[r][c] = 1  
        count_temp += 1  
    else:
        return

    if count_temp == 7:  
        check = True  
        return

    dr = [-1, 1, 0, 0]  
    dc = [0, 0, -1, 1]  

    for i in range(4):
        dfs2(visited, r + dr[i], c + dc[i])


def dfs(depth, start, count):
    global result
    global check
    global count_temp

    if count >= 4:  
        return  

    if depth == 7:  
        
        visited = [[1] * 5 for _ in range(5)]
        for i in arr:  
            visited[i[0]][i[1]] = 0

        dfs2(visited, arr[0][0], arr[0][1])  
        if check:
            result += 1  
            check = False
        count_temp = 0
        return

    for i in range(start, 25):
        r = i // 5  
        c = i % 5  
        arr.append((r, c))  
        dfs(depth + 1, i + 1, count + (students[r][c] == 'Y')) 
        arr.pop()  


students = [list(input()) for _ in range(5)]
arr = []
result = 0
check = False  
count_temp = 0  
dfs(0, 0, 0)
print(result)