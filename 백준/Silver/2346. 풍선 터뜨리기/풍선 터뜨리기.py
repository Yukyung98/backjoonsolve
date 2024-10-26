from collections import deque
import sys

N = int(input())
deq = deque(enumerate(map(int, input().split())))
tmp = []
while deq:
    idx, now_turn = deq.popleft()
    tmp.append(idx+1)
    if now_turn > 0:
        deq.rotate(-(now_turn - 1))
    elif now_turn < 0:
        deq.rotate(-now_turn)
print(' '.join(map(str, tmp)))
