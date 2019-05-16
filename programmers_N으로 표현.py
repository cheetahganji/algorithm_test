'''
프로그래머스 N
'''

def cal_four_arith_multi(ls, ls_N):
    rst = list()
    for j in ls_N:
        for i in ls:
            rst.append(i+j)
            rst.append(i-j)
            rst.append(i*j)
            if j!=0:
                div = int(i/j)
                if div > 0:
                    rst.append(div)

    if 0 in rst:
        rst.remove(0)

    return rst

def solution(N, number):
    answer = 0
    min_cnt = 8     # 8회 초과는 찾지 않는다.
    
    s = list()
    s.append([])   
    s.append([N])      # 숫자 n을 한 번 써서 만들 수 있는 수 집합

    if number == N:   # 숫자 n과 목표 숫자가 같은 경우
        answer = 1

    l = len(s)

    if answer == 0:
        for _ in range(min_cnt-1):
            if s[l-1]:
                ret = cal_four_arith_multi(s[l-1], [N])
                
                for i in range(1, int(l/2)+1):      # 다섯번 사용해서 나타낼 수 있는 숫자는 두번 사용한 것과 세번 사용한 것의 사칙연산으로도 계산될 수 있으므로 이런 연산도 추가함
                    ret.extend(cal_four_arith_multi(s[i], s[l-i]))

                ret.append( int(str(N)*l) )        # 5, 55, 555 같은 숫자들
                s.append( list(set(ret)) )         # 중복 제거

            l = len(s)

            if number in s[l-1]:        # 최종 내역에서만 찾는다.
                answer = l-1
                break

        if answer == 0:
            answer = -1

    return answer
