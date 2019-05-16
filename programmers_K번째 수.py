def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c[0], c[1], c[2]
        if len(array) >= j:
            if len(array[i-1:j]) >= k:
                a = array[i-1:j]
                a.sort()
                answer.append(a[k-1])
    return answer
