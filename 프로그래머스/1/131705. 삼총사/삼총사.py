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

# 방법2
from itertools import combinations,permutations,product
def solution(number):
    
    # 조합 : nCr -> combinations
    new = [sum(i) for i in combinations(number,3)]
    return new.count(0)
    
    # 알아두어야할 라이브러리 및 함수
    # from itertools import permutations, combinations, productr
    # 순열 : nPr -> permutations
    # new1 = list(permutations(number,3))
    # print(new1)
    
    # 중복순열 : product
    # new2 = list(product(number,number,number))
    # print(new2)
    
