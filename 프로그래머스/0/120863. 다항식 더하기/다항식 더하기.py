def solution(polynomial):
    coe = 0 # 일차항의 계수
    num = 0 # 상수
    poly = polynomial.replace(' ','')
    poly_1 = poly.split('+')
    
    # 일차항 계수와 상수항 구하기
    for i in poly_1:
        if i.isdigit(): # 상수항
            num += int(i)
        else: # 일차항 계수
            coe = coe + 1 if i == 'x' else coe + int(i[:-1])

    # 출력하기
    # 계수가 0인 경우
    if coe == 0:
        return str(num)
    # 계수가 1인 경우
    elif coe == 1:
        return 'x' + ' + ' + str(num) if num != 0 else 'x'
    # 계수가 0,1이 아닌 경우
    else:
        return str(coe) + 'x + ' + str(num) if num !=0 else str(coe) + 'x'
