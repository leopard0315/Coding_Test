def solution(polynomial):
    coe = 0 # 일차항의 계수
    num = 0 # 상수
    poly = polynomial.replace(' ','')
    print(poly)
    poly_1 = poly.split('+')
    print(poly_1)
    
    # 일차항 계수와 상수항 구하기
    for i in poly_1:
        # 일차항의 계수 구하기
        if 'x' in i:
            # x인 경우
            if len(i) == 1:
                coe += 1
            # 2x이상인 경우
            else:
                coe += int(i[:len(i)-1])
        # 상수항 구하기
        else:
            num += int(i)
    
    # 계수가 0인 경우
    if coe == 0:
        if num == 0:
            return none
        else:
            return str(num)
    # 계수가 1인 경우
    elif coe == 1:
        if num == 0:
            return 'x'
        else:
            return 'x' + ' + ' + str(num)
    # 계수가 0,1이 아닌 경우
    else:
        if num == 0:
            return str(coe) + 'x'
        else:
            return str(coe) + 'x' + ' + ' + str(num)

    
    
    
    
    