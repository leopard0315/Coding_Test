# c,d = divmod(a, b)
# c : a // b
# d : a % b
def solution(chicken):
    coupon = chicken # 쿠폰의 수 체크
    ser_chi = 0 # 서비스치킨 수 체크
    
    # # 1. 시켜먹은 치킨의수 -> 서비스 받은 치킨의 수만 체크
    # while(1):+
    #     chi = chicken // 10
    #     if chi == 0:
    #         coupon += chicken % 10 # 쿠폰의 수 더하기
    #         break
    #     ser_chi += chi # 서비스 치킨 개수 더하기
    #     coupon += chicken % 10 # 쿠폰의 수 더하기
    #     chicken = chi
    
    # 2. 쿠폰을 사용해서 서비스 받은 치킨의 수만을 체크
    while(coupon >= 10):
        ser_coupon = coupon // 10
        ser_chi += ser_coupon
        ser_coupon_1 = coupon % 10
        coupon = ser_coupon+ ser_coupon_1

    return ser_chi