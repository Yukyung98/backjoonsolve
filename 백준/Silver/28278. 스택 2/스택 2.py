import sys
input = sys.stdin.readline
n = int(input())
stack = []
for i in range(n) :
    k = input().rstrip()
    if len(k) > 2 :
        stack.append(int(k[2:]))
    elif k == '2' :
        if stack :
            print(stack.pop())
        else :
            print("-1")
    elif k == '3' :
        print(len(stack))
    elif k == '4' :
        if len(stack) == 0:
            print("1")
        else :
            print("0")
    else :
        if stack :
            print(stack[-1])
        else :
            print("-1")