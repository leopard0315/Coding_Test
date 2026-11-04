def solution(polynomial):
    coe = 0 # 일차항의 계수
    num = 0 # 상수
    poly = polynomial.replace(' ','')
    poly_1 = poly.split('+')
    
    # 일차항 계수와 상수항 구하기
    for i in poly_1:
        # 일차항의 계수 구하기
        if 'x' in i:
            # x인 경우
            if i == 'x':
                coe += 1
            # 2x이상인 경우
            else:
                coe += int(i[:-1])
        # 상수항 구하기
        else:
            num += int(i)

    # 출력하기
    # 계수가 0인 경우
    if coe == 0:
        return str(num)
    # 계수가 1인 경우
    coe_str=''
    if coe == 1:
        coe_str = 'x'
    else:
        coe_str = str(coe) + 'x'
    # 계수가 0,1이 아닌 경우
    if num == 0:
        return coe_str
    else:
         return coe_str +  ' + ' + str(num)
