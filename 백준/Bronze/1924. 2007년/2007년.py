day = 0 
arrList = [31,28,31,30,31,30,31,31,30,31,30,31]
weekList = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
M,D = map(int, input().split())
for i in range(M-1):
    day = day + arrList[i]
day = (day + D) % 7
print(weekList[day])