# 백준 1157번
# 단어 공부

from collections import Counter

# 입력
Word = list(map(str,input()))

# 아스키코드 사용 
# 대문자 = 소문자 - 32
# a 아스키코드 번호 97 A : 65

# 소문자 -> 대문자로 전부 변경
for i in range(len(Word)):
    # 소문자라면 대문자로 변경
    if (ord(Word[i]) >= 97 and ord(Word[i]) <= 122):
        k = ord(Word[i]) - 32
        Word[i] = chr(k)

# 출력
# 문자열의 길이가 1 이상일때
counter = Counter(Word)
if(len(counter) == 1):
    result = counter.most_common(1)
    print(result[0][0])
# 문자열의 길이가 2 이상일때
else:
    result = counter.most_common(2)
    # 가장 많이 사용된 알파벳이 1개가 아닌 경우
    if(result[0][1] == result[1][1]):
        print("?")
    else:
        print(result[0][0])