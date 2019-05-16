from itertools import permutations

def is_prime_num(num):

    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True    
    
    return False



def solution(numbers):
    answer = 0
    
    n = list(numbers)
    a = list(permutations(n, len(numbers)))
    
    for i in range(1, len(numbers)):
        a.extend(list(permutations(n,i)))
    a = list(set(a))
    # print(a)
    
    done = list()
    for i in a:
        num = int(''.join(i))
        # print(num)
        if is_prime_num(num) and num not in done:
            answer += 1
            done.append(num)
        
    return answer
