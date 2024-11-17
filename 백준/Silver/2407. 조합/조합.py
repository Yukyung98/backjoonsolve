n,m = map(int,input().split())
k = 1
y = 1
for i in range(n-m+1, n+1): 
    k *= i

for j in range(1, m+1):      
    y *= j
print(k//y)