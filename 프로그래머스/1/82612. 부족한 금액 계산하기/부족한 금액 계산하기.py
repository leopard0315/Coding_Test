# 이용료 price -> n번 이용시 price * n
# # 방법1
# def solution(price, money, count):
#     cost = 0
#     for i in range(1,count+1):
#         cost += i * price
    
#     # 금액이 부족하다면 비용 - 가지고 있는 돈, 금액이 부족하지 않다면 0 반환
#     return cost - money if money - cost < 0 else 0
# 방법2
def solution(price, money, count):
    return max(0,price * count * (count + 1)//2 - money)
        