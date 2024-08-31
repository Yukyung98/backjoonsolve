from collections import deque
def solution(elements):
    queue = deque(elements)
    li = set()
    cnt = len(elements)
    for i in range(1,cnt+1):
        for _ in range(cnt):
            tt = list(queue)[:i]
            li.add(sum(tt))
            queue.append(queue.popleft())
    return len(li)