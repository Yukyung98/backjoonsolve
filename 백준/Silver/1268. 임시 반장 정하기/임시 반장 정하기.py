import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N = int(input().strip())
matrix = [list(map(int,input().split())) for _ in range(N)]
students = [[0] * N for _ in range(N)]


for i in range(N):
    for j in range(5):
        for k in range(N):
            if matrix[i][j] == matrix[k][j]:
                students[i][k] =1
cnt = []
for i in students:  
    cnt.append(i.count(1))
print(cnt.index(max(cnt))+1)
