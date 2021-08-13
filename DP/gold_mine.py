# 테스트 케이스 입력
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = list(map(int,input().split()))
    data_list = list(map(int,input().split()))
    # data_list를 행렬로 변환하기 위해 2차원의 dp초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(data_list[index:index+m])
        index += m
    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0: left_up = 0
            else: left_up = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1: left_down = 0
            else: left_down = dp[i+1][j-1]
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            # 점화식 진행
            dp[i][j] = dp[i][j] + max(left, left_down, left_up)
    print(dp)
    result = 0
    # m-1 열에서 최대 값을 구한다
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)