'''
프로그래머스 : 가장 큰 
'''

def solution(numbers):
    answer = ''

    if max(numbers) == 0:
        answer = '0'
    else:
        max_len = len(str(max(numbers)))        # 가장 큰 길이

        # 자리수가 각각 다르므로 가장 큰 길이만큼 반복하여 길이비교
        # ex) 9 91 비교시, 9->99, 91->9191로 비교. 숫자로 비교하면 9191 > 99 이지만, 문자로 비교하면 '99' > '9191'이 더 크기 때문에 이를 이용할 수 있음
        sorted_numbers = sorted(numbers, key=lambda n:str(n)*max_len, reverse=True)     

        sorted_numbers = list(map(str, sorted_numbers))     # 각 숫자를 문자형으로 변경
        answer = ''.join(sorted_numbers)        # 문자이어붙이기

    return answer
