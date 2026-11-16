# '': 공백(0), # : 벽(1)
# 지도 n * n
# 
def solution(n, arr1, arr2):
    ans = []
    for i in range(n):
        # or 연산 진행해서 값 구하기
        Num = arr1[i] | arr2[i]

        # 앞에 '0'이 부족한 경우, 0 채우기
        if len(bin(Num)[2:]) != n:
            str_num = '0' * (n-len(bin(Num)[2:]))  + str(bin(Num)[2:])
        else:
            str_num = str(bin(Num)[2:])
    
        print(str_num)
        
        s = ''
        for c in str_num:
            if c == '1':
                s += '#'
            else:
                s += ' '
        print(s)
        ans.append(s)
    return ans
        
#         num = bin(arr1[i])
#         num2 = bin(arr2[i])
#         len_num = len(num)
#         len_num2 = len(num2)
        
#         # 길이가 n자리인경우 / 길이가 n자리 미만인경우
#         if len_num == (n+2):
#             str_num = str(num[2:])
#         else:
#             # n = 5, len()
#             str_num = '0' * (n+2-len_num) + str(num[2:])
        
#         if len_num2 == (n+2):
#             str_num2 = str(num2[2:])
#         else:
#             # n = 5, len()
#             str_num2 = '0' * (n+2-len_num2) + str(num2[2:])
            
#         arr1_1.append(str_num)
#         arr2_1.append(str_num2)
            
#     print(arr1_1)
#     print(arr2_1)
    