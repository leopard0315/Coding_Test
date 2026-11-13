# 3개의 정수번호를 다 더했을때, 0이 되면 삼총사
# # 방법1
# def solution(number):
#     answer = 0
#     for i in range(len(number)-2):
#         for j in range(i+1,len(number)-1):
#             for k in range(j+1,len(number)):
#                 if (number[i] + number[j] + number[k]) == 0:
#                     answer += 1
#     return answer

from itertools import combinations
def solution(number):
    new = [sum(i) for i in combinations(number,3)]
    return new.count(0)
