def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)) :
        if signs[i] == True:
            answer += int(absolutes[i])
        if signs[i] == False:
            answer -=int(absolutes[i])
    return answer