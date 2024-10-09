import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input().strip())
ss = []
st = list(map(int, input().split()))
tt= [-1]*n
for i in range(n):
    while ss and st[ss[-1]]<st[i]:
        tt[ss.pop()] = st[i]
    ss.append(i)
print(' '.join(map(str, tt)))