def next_pos(m, n, pos):
    next = []

    for p in pos:
        if p[0] < m:
            next.append([p[0] + 1, p[1]])
        if p[1] < n:
            next.append([p[0], p[1]+1])

    return next


def solution(m, n, puddles):
    answer = 0

    dp = list()
    dp.append([[1,1]])
    print(dp)

    shortest_cnt = m+n-2

    for i in range(1, shortest_cnt+1):
        t = next_pos(m, n, dp[i-1])
        if not t:   # 갈 수 있는 경로가 없으면
            return 0
        else:
            if [m, n] in t:
                return t.count([m, n])
            else:
                dp.append([x for x in t if x not in puddles])

    return answer
