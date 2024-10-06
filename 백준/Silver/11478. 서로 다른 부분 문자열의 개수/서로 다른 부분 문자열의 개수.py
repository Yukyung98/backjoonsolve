import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
A= input().strip()
tt = set()  
for i in range(len(A)):
    for j in range(i + 1, len(A) + 1):
        tt.add(A[i:j])  
print(len(tt))