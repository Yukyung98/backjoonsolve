def solution(answers):
    answer = []
    one = [1,2,3,4,5]*len(answers)
    two = [2,1,2,3,2,4,2,5]*len(answers)
    three = [3,3,1,1,2,2,4,4,5,5]*len(answers)
    one_cnt = 0
    two_cnt = 0
    three_cnt = 0
    for i in range(0,len(answers)):
        if answers[i]==one[i] :
            one_cnt += 1
        if answers[i]==two[i] :
            two_cnt += 1
        if answers[i]==three[i] :
            three_cnt +=1
    k = max(one_cnt,two_cnt,three_cnt)
    if k == one_cnt:
        answer.append(1)
    if k== two_cnt:
        answer.append(2)
    if k == three_cnt:
        answer.append(3)
    return answer