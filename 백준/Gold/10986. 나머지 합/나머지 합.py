import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N,M= map(int, input().split())  # A원소 갯수, B 원소 갯수
ss = list(map(int, input().split()))

r = [0] * M
prefixSum = 0
for i in range(N):
    prefixSum += ss[i]
    r[prefixSum % M] += 1

tt = r[0] 
for i in range(M):
    tt += r[i] * (r[i]-1) // 2
print(tt)
