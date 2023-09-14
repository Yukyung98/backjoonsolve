import sys
input = sys.stdin.readline
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))
dik = {}
for i in range(len(cards)) :
    dik[cards[i]] =0
for j in range(M):
    if check[j] not in dik :
        print(0, end =' ')
    else : 
        print(1, end = ' ') 