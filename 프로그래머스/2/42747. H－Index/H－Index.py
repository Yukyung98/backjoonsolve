def solution(citations):
    answer = 0
    citations.sort()
    Hindx = len(citations)
    while True:
        if Hindx == 0:
            break
        cnt = 0
        rcnt = 0
        for i in citations:
            if i>=Hindx:
                cnt +=1
            else:
                rcnt+=1
        if Hindx <=cnt:
            answer  = Hindx
            break
        else:
            Hindx-=1
    return answer