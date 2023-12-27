x,y = map(int,input().split())
cnt = 0
for i in range(1,x+1):
    if x % i == 0:
        cnt+=1
        if cnt == y :
            print(i)
            break
if cnt != y:
    print(0)