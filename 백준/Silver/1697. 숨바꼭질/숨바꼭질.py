import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def bfs(N, K):
    visited = [-1]*100001
    queue = deque([N])
    visited[N] = 0
    while queue:
        current = queue.popleft()
        if current == K:  
            return visited[current]
        for next in (current-1,current+1,current*2):
            if 0<=next<=100000 and visited[next] == -1:
                visited[next] = visited[current] + 1
                queue.append(next)
        
N,K = map(int,input().split())
print(bfs(N,K))
