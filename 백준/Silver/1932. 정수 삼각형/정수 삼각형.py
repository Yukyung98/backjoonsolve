n = int(input())  # 삼각형의 크기 n 입력
triangle = [list(map(int, input().split())) for _ in range(n)]  # 삼각형 입력 받기
# dp 배열 초기화
dp = [[0] * n for _ in range(n)]

# 첫 번째 줄은 삼각형의 첫 번째 값으로 초기화
dp[0][0] = triangle[0][0]

# DP 배열 채우기
for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            # 첫 번째 열은 바로 위의 첫 번째 값만 선택
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j == i:
            # 마지막 열은 바로 위의 마지막 값만 선택
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:
            # 중간 값은 왼쪽과 오른쪽 중 더 큰 값을 선택
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

# 마지막 줄에서 최대값을 출력
print(max(dp[n-1]))
