def solution(picture, k):
    answer = []
    for i in picture:
        arr = list(i)
        for j in range(len(arr)):
            arr[j] = arr[j] * k
        
        for _ in range(k):
            answer.append(''.join(arr))
            
    return answer