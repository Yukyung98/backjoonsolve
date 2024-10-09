import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
A,B = map(str,input().split())
print(int(str(int(B[::-1])+int(A[::-1]))[::-1]))
