## 접근
# 1. 지금까지 나온적이 없는 수이면 배열 맨 뒤에 추가 - in 함수를 써서 false이면 배열 맨 뒤에 추가
# 2. 완성될 배열의 길이가 k보다 작으면 부족한 값만큼 -1로 채우기 - [-1] * (k-len(answer))
def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
        
        if len(answer) == k:
            break
    if len(answer) < k:
        answer.extend([-1] * (k-len(answer)))
    
    return answer