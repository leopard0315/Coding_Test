# def solution(array):
#     # 방법1. counter함수 사용X
#     # 빈 딕셔너리 생성
#     mode = {}
#     # 각 원소의 count값을 적용해서 배열안에 몇번있는지 확인하고 이를 딕셔너리로 표현
#     for i in range(len(array)):
#         mode[array[i]] = array.count(array[i])
    
#     # 딕셔너리 아이템을 기준으로 최빈값이 가장 앞에 오도록 내림차순 정렬
#     mode1 = list(sorted(mode.items(),key=lambda x:-x[1]))

#     # 만약 최빈값이 2개이상일 경우, -1 반환
#     if len(mode1) >=2:
#         if mode1[0][1] == mode1[1][1]:
#             return -1
        
#     # 아니라면 최빈값 반환
#     return mode1[0][0]

# 방법2. Counter 함수 이용
from collections import Counter

def solution(array):
    a = Counter(array).most_common(2) # 가장 빈출값 2개 뽑기
    if len(a) == 1: # 배열의길이가 1인 경우 1개 반환
        return a[0][0]
    if a[0][1] == a[1][1]: # 최빈값이 여러개인경우 -1 반환
        return -1
    return a[0][0] # 아니라면 최빈값 반환하기
