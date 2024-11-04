from collections import deque
import sys
st = list(sys.stdin.readline().strip())
tt = list(sys.stdin.readline().strip())
m = len(tt)
stack = []
for i in st:
    stack.append(i)
    if stack[len(stack)-m:len(stack)] == tt: 
        for _ in range(m): 
            stack.pop() 
if stack:
    print(*stack, sep='')
else:
    print("FRULA")
