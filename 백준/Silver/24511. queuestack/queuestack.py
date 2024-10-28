from collections import deque
import sys

N = int(input())
queorstack = list(map(int,input().strip().split()))
nu = deque(map(int,input().strip().split()))
tt = [[q,n] for q, n in zip(queorstack, nu)]
M = int(input())
insert = deque(map(int,input().strip().split()))
kk = deque()
for x,y in tt:
    if x == 0:
        kk.append(y)
for i in insert:
    kk.appendleft(i)
    print(kk.pop(),end=" ")
