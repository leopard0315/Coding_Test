def solution(A, B):
    answer = 0
    for i in range(len(A)):
        if (A[len(A)-i:] + A[0:len(A)-i]) == B:
            return answer
        answer += 1
            
    return -1