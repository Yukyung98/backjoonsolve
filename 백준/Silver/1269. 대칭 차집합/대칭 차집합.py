import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
tt = dict()
A,B= map(int, input().split())  # A원소 갯수, B 원소 갯수

a = set(map(int, input().split()))

b = set(map(int, input().split()))

dd = len(a - b) + len(b - a)

print(dd)