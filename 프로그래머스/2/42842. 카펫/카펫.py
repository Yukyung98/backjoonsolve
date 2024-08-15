def solution(brown, yellow):
    total = brown + yellow
    
    # total의 약수 구하기
    for height in range(1, int(total**(0.5)) + 1):
        if total % height == 0:
            width = total // height
            
            # 가로는 세로보다 크거나 같아야 함
            if width >= height:
                # 갈색 타일의 수가 정확히 맞는지 확인
                if (width - 2) * (height - 2) == yellow:
                    return [width, height]
