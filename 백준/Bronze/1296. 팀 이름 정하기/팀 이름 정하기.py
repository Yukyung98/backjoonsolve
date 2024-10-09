import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
word = input().strip()
N = int(input().strip())
Team = {}
score = 0
socre_n = []
for i in range(N):
    name = input().strip()
    L = word.count("L") + name.count("L")
    O = word.count("O") + name.count("O")
    V = word.count("V") + name.count("V")
    E = word.count("E") + name.count("E")
    score = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    Team[name] = score
    socre_n.append(score)
    score = 0
max_n = max(socre_n)
names = []
for x,y in Team.items():
    if y == max_n:
        names.append(x)
names.sort()
print(names[0])