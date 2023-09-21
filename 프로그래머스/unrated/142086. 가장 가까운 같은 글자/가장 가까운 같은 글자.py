def solution(s):
    answer = []
    word = {}
    for i in range(len(s)) :
        if s[i] not in word:
            word[s[i]] = i
            answer.append(-1)
        else :
            answer.append(i-word[s[i]])
            word[s[i]] = i
    return answer