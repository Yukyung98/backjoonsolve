from collections import deque

s,t = map(int,input().split())
def bfs(s,t):
    if s == t:
        return "0"
    queue = deque([(s,"")])
    visited = set()
    visited.add(s)

    while queue:
        current,path = queue.popleft()
        for op,nextValue in [('*',current*current),('+',current+current),('-',current-current),('/',current//current if current != 0 else None )]:
            if nextValue is None or nextValue < 1 or nextValue>10**9:
                continue
            newpath = path+op
            if nextValue == t:
                return newpath
            if nextValue not in visited:
                visited.add(nextValue)
                queue.append((nextValue,newpath))

    return "-1"
print(bfs(s,t))