def solution(citations):
    answer = 0
    
    max_cit = max(citations)

    if max_cit == 0:
        answer = 0
    else:
        for i in range(1, max_cit+1):
            
            if len([c for c in citations if c >= max_cit+1-i]) >= max_cit+1-i:
                answer = max_cit+1-i
                break

    return answer
