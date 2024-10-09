import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
A,B = map(int,input().split())
tt = [0]
for i in range(1,B+1):
    for j in range(i):
        tt.append(i)
print(sum(tt[A:B+1]))