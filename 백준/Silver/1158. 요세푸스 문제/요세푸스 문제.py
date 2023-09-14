import sys
from collections import deque
input = sys.stdin.readline
queue = deque()
queue1 = []
N,K = map(int, input().split())
for i in range(1,N+1):
    queue.append(i)
while queue :
    for i in range(K-1) :
        queue.append(queue.popleft())
    queue1.append(queue.popleft())
print(str(queue1).replace('[','<').replace(']','>'))