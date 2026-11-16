# '': 공백(0), # : 벽(1)
# 지도 n * n
def solution(n, arr1, arr2):
    ans = [] # 정답 배열 선언
    for i in range(n):
        # or 연산 진행해서 값 합치기
        Num = arr1[i] | arr2[i]

        # 합친값이 앞에 '0'이 부족한 경우, 부족한 '0' 채우기
        b_Num = bin(Num)[2:]
        if len(b_Num) != n:
            str_num = '0' * (n-len(b_Num))  + str(b_Num)
        else:
            str_num = str(b_Num)
            
        # 해당 문자열을 1:'#', 0:' '으로 변환하기
        s = ''
        for c in str_num:
            if c == '1':
                s += '#'
            else:
                s += ' '
                
        # 정답 배열에 추가하기
        ans.append(s)
        
    # 정답 배열 반환
    return ans
    