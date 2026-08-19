def solution(participant, completion):
    answer = ""
    participant.sort()
    completion.sort()
    # participant랑 completion이랑 같은 경우랑 안 같은 경우 2가지
    # 1) 중간에 다른 경우
    for i in range(len(completion)):
        if participant[i] != completion[i]: # 중간에 다른경우
            return participant[i]
    return participant[len(completion)]

            
    