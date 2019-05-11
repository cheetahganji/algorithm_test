'''
정의
    dp[n] : n자리 숫자에 대한 암호의 해석 수
    참고(n자리 숫자에 대해, n-1자리 숫자의 끝자리가 한 자리인 경우의 수는 dp[n-2])

암호해석 실패 조건(다음 중 하나라도 만족하는 경우)
    0으로 시작하거나, [00, 30, ..., 80, 90] 중 하나라도 포함
'''

cyper_text = input()

# 초기화
dp = list()
dp.append(1)    # 계산 편의상 1
dp.append(1)    # 한 자리 숫자의 경우의 수

# 암호해석 실패 조건(다음 중 하나라도 만족하는 경우)
# 0으로 시작하거나, [00, 30, ..., 80, 90] 중 하나라도 포함
not_contain = [str(x*10) for x in range(3, 10)]
not_contain.insert(0, '00')

flag = True

if cyper_text[0:1] == '0':
    flag = False

for nc in not_contain:
    if nc in cyper_text:
        flag = False
        break

if not flag:
    print('0')
else:
    for i in range(2, len(cyper_text)+1):
        a = cyper_text[i-2] + cyper_text[i-1]

        if int(cyper_text[i-1]) == 0:
            dp.append(dp[i-2])
        elif int(a) in range(10, 27):
            dp.append(dp[i-1] + dp[i-2])
        else:
            dp.append(dp[i-1])

    print(dp[len(cyper_text)]%1000000)
