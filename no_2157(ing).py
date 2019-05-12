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
airway = [[1, 3, 2]
    , [1, 2, 5]
    , [2, 3, 3]
    , [1, 3, 4]
    , [3, 1, 100]
]


a = [int(x) for x in input().split(' ')]

n=a[0]
m=a[1]
k=a[2]


airway = list()
for i in range(k):
    a = [int(x) for x in input().split(' ')]
    airway.append(a)



dp = list()
for e in range(n + 1):
    dp.append([])

for e in dp:
    for e2 in range(n + 1):
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

# for e in dp:
#     print(e)
# print()

'''
n : 도시 개수
2 <= i <= n

k : 경로

dp[i] : 1번 도시부터 i번 도시까지의 최대 기내식 점수
dp[i] : max( dp[j] + k[j][i] )
(단, j는 1<=j<i에 해당하는 모든 j에 대해, k[j][i] 값이 있는 모든 j)
'''

p = list()

p.append(0)
p.append(0)


# print('dp ', dp)
k = copy.deepcopy(dp)

# print('k ', k)

for i in range(2, n + 1):
    # print()
    # print('i', i)

    tmp = list()
    for j in range(1, i):
        # print('i, j', (i, j))
        if k[j][i]:
            # print('p :', p)
            # print('k[j][i] ', k[j][i])
            # print('p[j]', p[j])
            # print('p[j] + k[j][i]', p[j] + k[j][i])
            tmp.append(p[j] + k[j][i][0])
        else:
            tmp.append(p[j])
    p.append(max(tmp))

print(p[n])
