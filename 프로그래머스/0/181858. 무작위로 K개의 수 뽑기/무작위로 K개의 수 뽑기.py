## 접근
# 1. 지금까지 나온적이 없는 수이면 배열 맨 뒤에 추가 - in 함수를 써서 false이면 배열 맨 뒤에 추가
# 2. 완성될 배열의 길이가 k보다 작으면 부족한 값만큼 -1로 채우기 - [-1] * (k-len(answer))
def solution(arr, k):
    answer = []
    for i in arr:
        # arr의 요소가 answer 배열에 존재하지않으면 추가한다.
        if i not in answer:
            answer.append(i)
        
        # answer 배열의 길이가 k라면 반복문 중단
        if len(answer) == k:
            break
    
    # answer의 길이가 k보다 작다면 부족한 원소만큼 -1 추가 
    if len(answer) < k:
        answer.extend([-1] * (k-len(answer)))
    
    # 정답을 반환한다.
    return answer