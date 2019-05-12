from datetime import datetime, timedelta
import copy
now = datetime.now()


# 도시 개수
n = 3

# 여행하려는 도시 개수
m = 3

# 개설된 항로 개수
k = 5

# print('도시 개수 :', n)
# print('여행하려는 도시 개수 :', m)

# 항로 정보
airway = [    [1, 3, 2]
            , [1, 2, 5]
            , [2, 3, 3]
            , [1, 3, 4]
            , [3, 1, 100]
]



dp = list()
for e in range(n+1):
    dp.append([])

for e in dp:
    for e2 in range(n+1):
        e.append([])


# for e in dp:
#     print(e)
# print()

for e in airway:
    if e[0] < e[1]:
        tmp = dp[e[0]][e[1]]
        if tmp:
            s = max(tmp)
            if e[2] > s:
                tmp.clear()
                tmp.append(e[2])
        else:
            tmp.append(e[2])


for e in dp:
    print(e)
print()


# q[i]를 i도시까지 최대 기내식 점수라 했을 때,
# q[n]= max(q[i] + dp[i][n]), i(단, i는 n을 to로 갖는 fr도시)
q = list()
q.append(0)
q.append(0)

for e in range(2, n+1):
    print(e)
    max = 0
    max_idx = -1
    for i in range(0, n+1):
        if i < e and dp[i][e]:
            # print('dp[i][e] :', dp[i][e][0])
            if max < dp[i][e][0]:
                max = dp[i][e][0]
                max_idx = i
    #     if max < dp[i][e][0]:
    #         max = dp[i][e][0]
    print('max :', max)

    if max_idx == -1:
        print('a')
        q.append(max)
    else:
        print('b')
        q.append(q[max_idx]+max)

    print('q :', q)




# 여행도시 m
#
# m=2이면 그대로
#
# m=3, n최종 도시면
#
#
#
#
#
#



then = datetime.now()
delta = then-now

print(delta.total_seconds())

