N,K = map(int, input().split())
coinlist = list()
for i in range(N) :
    coinlist.append(int(input()))
cout = 0
for i in reversed(range(N)) : 
    cout += K // coinlist[i]
    K = K%coinlist[i]
print(cout)
