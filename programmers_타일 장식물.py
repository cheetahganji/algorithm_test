# dp[N] : 타일의 개수 N이 주어질 때, N개의 타일로 구성된 직사각형의 둘레
# s[N] : N번째 타일 한 변의 길이
# dp[N] : dp[N-1] + s[N]*2

def solution(N):
    answer = 0

    # 초기화 : 타일의 한 변의 길이(0~2번째 타일까지)
    s = [0, 1, 1]
    dp = [0, 4]

    for i in range(2, N+1):
        dp.append(dp[i-1] + s[i]*2)
        s.append(s[i-1] + s[i])

    answer = dp[N]

    return answer
