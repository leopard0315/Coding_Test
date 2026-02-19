# 백준 14489번
# 치킨 두마리(...)

# 입력
A,B = map(int,input().split())
C = int(input())

# 잔고 계산
account = A + B
price = C * 2
if(account >= price):
    account = account - price

# 출력
print(account)