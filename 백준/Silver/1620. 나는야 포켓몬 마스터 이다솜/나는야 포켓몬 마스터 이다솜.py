# 백준 1620번
# 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

# 입력
N,M = map(int,input().split())

# 포켓몬 도감 배열 생성 / 딕셔너리 생성
poket_list = []
poket_dict = {}

for i in range(N):
    name = input().strip()
    poket_list.append(name)
    poket_dict[name] = i+1

# 포켓몬 도감 순서를 통해 이름찾기 -> 리스트 사용
# 포켓몬 도감 이름을 통해 순서 찾기 -> 딕셔너리 사용
for i in range(M):
    n = input().strip()
    # 입력된 값이 순서(위치)라면 -> 이름 도출
    if (n.isdigit()):
        print(poket_list[int(n)-1])
    # 입력된 값이 이름이라면 -> 순서(위치 도출)
    else:
        print(poket_dict[n])