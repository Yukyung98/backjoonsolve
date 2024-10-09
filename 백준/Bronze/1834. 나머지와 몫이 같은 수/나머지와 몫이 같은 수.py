import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input().strip())
sum = 0
for i in range(1,n):
    sum += n*i+i
print(sum)