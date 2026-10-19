# 목표: 배열안의 2가 모두 포함된 가장 작은 연속된 부분배열 반환 
# -> 그러면 양쪽끝이 2여야 최소가 된다.
def solution(arr):
    s = -1 # start 변수
    e = -1 # end 변수
    
    # 만약 arr에 2가 2번이상있는 경우
    for i in range(len(arr)):
        if arr[i] == 2: # 2인지 확인
            if s == -1: # 2가 처음 등장할시 s랑 e 동일한 인덱스 값 저장
                s = i
            e = i # 2가 등장했을때의 끝순서 저장
    
    # 만약 arr에 2가 없는 경우 [-1] 반환, 2가 있다면 arr[start:end+1] 값 반환하기
    if s == -1:
        return [-1]
    return arr[s:e+1]