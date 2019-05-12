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

'''
a = [int(x) for x in input().split(' ')]

n=a[0]
m=a[1]
k=a[2]


airway = list()
for i in range(k):
    a = [int(x) for x in input().split(' ')]
    airway.append(a)

'''



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



'''
n : 도시 개수
2 <= i <= n

k : 경로

dp[i] : 1번 도시부터 i번 도시까지의 최대 기내식 점수
dp[i] : max( dp[j] + k[j][i] )
(단, j는 1<=j<i에 해당하는 모든 j에 대해, k[j][i] 값이 있는 모든 j)
'''

print('dp', dp)
k = copy.deepcopy(dp)

for i in range(2,n+1):
    print()
    print('i', i)
    for j in range(1,i):
        print('i, j', (i,j))
        if k[j][i]:
            print('k[j][i] ', k[j][i])
            print('dp[j]', dp[j])


# q[i]를 i도시까지 최대 기내식 점수라 했을 때,
    # q[n]= max(q[i] + dp[i][n]), i(단, i는 n을 to로 갖는 fr도시)
q = list()
q.append(0)
q.append(0)


for e in range(2, n+1):
    
    max = 0
    max_idx = -1
    for i in range(0, n+1):
        if i == e-1 and dp[i][e]:
            # print('dp[i][e] :', dp[i][e][0])
            if max < dp[i][e][0]:
                max = dp[i][e][0]
                max_idx = i
    #     if max < dp[i][e][0]:
    #         max = dp[i][e][0]
    

    if max_idx == -1:
        q.append(max)
    else:
        q.append(q[max_idx]+max)
    






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
print(q[n])

# then = datetime.now()
# delta = then-now

# print(delta.total_seconds())

