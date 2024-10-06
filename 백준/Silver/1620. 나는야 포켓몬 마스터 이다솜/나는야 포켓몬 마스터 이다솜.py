import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, K = map(int, input().split())  
dd = dict()
re_dd = dict()


for i in range(N):
    name = input().strip()
    dd[i + 1] = name
    re_dd[name] = i + 1  

for j in range(K):
    s = input().strip()
    
    if s.isdigit():  
        print(dd[int(s)])
    else:  
        print(re_dd[s])
