def solution(numbers, target):
    total = [0]
    cnt = 0 
    for i in numbers:
        tmp= [] 
        for k in total:
            tmp.append(k-i)
            tmp.append(k+i)
        total = tmp
    for i in total:
        if i == target:
            cnt+=1
    return cnt
    
    
    
    
    
    
    
    
    
    
    
    

    
