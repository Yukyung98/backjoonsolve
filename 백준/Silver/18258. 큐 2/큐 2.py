from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
dep = deque([])
for _ in range(N):
    str = input().split()
    if str[0] == 'push' :
        dep.append((str[1]))
    elif str[0] == 'pop' :
        if len(dep) == 0:
            print(-1)
        else :
            print(dep.popleft())
    elif str[0] =='size':
        print(len(dep))
    elif str[0] == 'empty' :
        if len(dep) == 0 :
            print(1)
        else : 
            print(0)
    elif str[0] == 'front':
        if len(dep) == 0:
            print(-1)
        else:
            print(dep[0])
    elif str[0] == 'back':
        if len(dep) == 0:
            print(-1)
        else : 
            print(dep[-1])