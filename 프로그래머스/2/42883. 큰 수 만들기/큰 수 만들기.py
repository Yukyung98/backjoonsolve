import itertools
def solution(number, k):
    answer = ''
    stack = []
    for i in number:
        if not stack:
            stack.append(i)
            continue
        if k>0:
            while stack[-1]<i:
                stack.pop()
                k-=1
                if not stack or k<=0:
                    break
        stack.append(i)
    stack = stack[:-k] if k>0 else stack
    return ''.join(stack)