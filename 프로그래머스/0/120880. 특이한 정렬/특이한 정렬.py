# 1. 방법1
# 방법1과 방법2 구현 원리는 동일하지만 방법1을 압축하고 불필요한 부분을 날리면 방법2가 된다.
def solution(numlist, n):
    answer = [] # 정답을 담을 배열
    diff = [] # 거리 차이를 담을 배열 abs()사용해서 차이 구하기
    
    # 거리차이 담기
    for i in numlist:
        diff.append(abs(n-i))
    
    # 거리와 해당 정수열을 zip함수로 묶고 리스트로 변환
    arr = list(zip(numlist,diff))
    
    # key=lambda를 사용해서 거리차이가 작은 숫자 먼저 정렬, 값이 같다면, 숫자가 더 큰 숫자를이후에 오도록 내림차순 정렬 진행
    arr.sort(key=lambda x:(x[1],-x[0]))
    
    # 정렬된 arr에 대하여 numlist값만을 반환
    for j in arr:
        answer.append(j[0])
    return answer

# # 2. 방법2
# def solution(numlist, n):
#     return sorted(numlist, key=lambda x:(abs(n-x),-x))