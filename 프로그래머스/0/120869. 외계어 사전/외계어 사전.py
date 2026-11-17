def solution(spell, dic):
#     ## 아이디어: spell을 오름차순한 배열과 dic배열 사이에 문자열을 배열로 변환하여 오름차순 정렬한 배열과 일치하는 배열 찾기

#     # 방법1
#     # spell 오름차순 정렬
#     spell.sort() 
    
#     # dic에서 한 원소씩 빼낸 후, 리스트로 변환해서 오름차순 정렬
#     # 해당 배열이 서로 일치한다면 1 반환하고, 아니라면 2 반환
#     for i in dic:
#         list_i = list(i)
#         list_i.sort()
#         if spell == list_i:
#             return 1
#     return 2

#   # 방법2
    # 문자열의 길이 먼저 동일한지 확인
    len_spell = len(spell)
    for i in dic:
        if len(i) == len_spell:
            n = 0
            for j in spell:
                if j in i:
                    n += 1
                else:
                    break
            if n == len_spell:
                return 1
    return 2
            
                
                
