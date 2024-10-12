from collections import deque
def solution(progresses, speeds):
    answer = []
    day = deque()
    for x,y in zip(progresses,speeds):
        if (100-x)%y == 0:
            day.append((100-x)//y)
        else:
            day.append((100-x)//y+1)
    tmp = []
    while day:
        inx = day.popleft()
        if len(tmp) == 0:
            tmp.append(inx)
        else:
            if inx > tmp[0]:
                print(inx,tmp[0])
                answer.append(len(tmp))
                tmp = []
                tmp.append(inx)
            else:
                tmp.append(inx)  
    answer.append(len(tmp))
    return answer