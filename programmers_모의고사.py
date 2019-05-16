'''
프로그래머스 : 모의고사
'''

def solution(answers):
    answer = []

    pbp = list()        # pattern by person
    pbp.append([1, 2, 3, 4, 5])
    pbp.append([2, 1, 2, 3, 2, 4, 2, 5])
    pbp.append([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])

    score = list()
    for i in range(len(pbp)):
        score.append(0)

    for idx, ans in enumerate(answers):
        for i, p in enumerate(pbp):
            if p[idx%len(p)] == ans:
                score[i] += 1

    answer = [n for n, s in enumerate(score, start=1) if s == max(score)]

    return answer
