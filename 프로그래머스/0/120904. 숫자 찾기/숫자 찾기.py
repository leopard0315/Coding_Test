def solution(num, k):
    answer = 0
    n = str(num)
    for i in range(len(n)):
        if int(n[i]) == k:
            answer = i+1
            break

    return answer if answer else -1