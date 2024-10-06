import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
tt = dict()
N, M = map(int, input().split())  # 듣어보지 못한 사람, 보지도 못한 사람
for i in range(N):
    ss = input().strip()
    tt[ss] = 1
for j in range(M):
    name = input().strip()
    if name in tt.keys():
        tt[name] += 1 
    else:
        tt[name] = 1
du = [name for name,count in tt.items() if count>1]
print(len(du))
print('\n'.join(sorted(du)))