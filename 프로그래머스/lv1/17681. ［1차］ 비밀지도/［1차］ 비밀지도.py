def solution(n, arr1, arr2):
    answer = []
    st = ''
    for i in range(n):
        a = len(str(bin(arr1[i])).replace('0b',''))
        b = len(str(bin(arr2[i])).replace('0b',''))
        if a < n:
            arr1[i] = str(bin(arr1[i])).replace('0b','0'*(n-a))  
        else: 
            arr1[i] = str(bin(arr1[i])).replace('0b','')  
        if b<n:
            arr2[i] = str(bin(arr2[i])).replace('0b','0'*(n-b))
        else : 
            arr2[i] = str(bin(arr2[i])).replace('0b','')
    for i in range(n):
        st = ''
        for j in range(n):
            if int(arr1[i][j])+int(arr2[i][j]) >=1 :
                st +="#"
            else :
                st +=" "
        answer.append(st)
    
    return answer