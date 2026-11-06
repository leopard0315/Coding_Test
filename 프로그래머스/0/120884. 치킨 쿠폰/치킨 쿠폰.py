def solution(chicken):
    coupon = 0 # 쿠폰의 수 체크
    ser_chi = 0 # 서비스치킨 수 체크
    
    while(1):
        chi = chicken // 10
        if chi == 0:
            coupon += chicken % 10 # 쿠폰의 수 더하기
            break
        ser_chi += chi # 서비스 치킨 개수 더하기
        coupon += chicken % 10 # 쿠폰의 수 더하기
        chicken = chi
    
    while(coupon >= 10):
        ser_coupon = coupon // 10
        ser_chi += ser_coupon
        ser_coupon_1 = coupon % 10
        coupon = ser_coupon+ ser_coupon_1
    print(coupon)
    print(ser_chi)
    return ser_chi