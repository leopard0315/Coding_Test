def solution(emergency):
    answer = []
    e = sorted(emergency,reverse=True)
    
    for i in emergency:
        answer.append(e.index(i)+1)
        
    return answer
        