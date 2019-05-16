def solution(triangle):
    answer = 0
    dp = [triangle[0]]

    for i in range(1, len(triangle)):

        t = list()
        for idx, j in enumerate(triangle[i]):
            m = 0
            if idx == 0:
                m = dp[i-1][idx] + j
            elif idx == len(triangle[i])-1:
                m = dp[i-1][idx-1] + j
            else:
                m = max(dp[i-1][idx] + j, dp[i-1][idx-1] + j)
            t.append(m)
        dp.append(t)

    answer = max(dp[len(dp)-1])
    return answer
