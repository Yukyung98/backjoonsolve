from collections import deque
import sys
N = int(sys.stdin.readline().strip())
N_n = list(map(int,sys.stdin.readline().split()))
func = list(map(int,sys.stdin.readline().split())) # +,-,x,%

maximum = -1e9
minimum = 1e9

def dfs(step,total,plus,minus,mult,div):
    global maximum,minimum
    if step == N:
        maximum = max(total,maximum)
        minimum = min(total,minimum)
        return
    if plus:
        dfs(step + 1, total + N_n[step], plus - 1, minus, mult, div)
    if minus:
        dfs(step + 1, total - N_n[step], plus, minus - 1, mult, div)
    if mult:
        dfs(step + 1, total * N_n[step], plus, minus, mult - 1, div)
    if div:
        dfs(step + 1, int(total / N_n[step]), plus, minus, mult, div - 1)


dfs(1, N_n[0], func[0], func[1], func[2], func[3])
print(maximum)
print(minimum)