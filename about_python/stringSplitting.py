'''
문자열을 split하는 여러 예시와 방법입니다.

- split 뒤에 적어둔 문자를 기준으로 string이 split 됩니다.
- split 된 string들은 list에 저장됩니다.
'''

# 01. 이메일 주소에서 아이디만을 가져오고 싶은 경우
email = "coffee@gmail.com"
myID = email.split('@')[0]

print("myID : ", myID)

# 02. 년, 월, 일이 '-'로 연결된 날짜에서 각각을 따로 가져오고 싶은 경우
date = "2021-11-13"
YMD = date.split('-')
y, m, d = int(YMD[0]), int(YMD[1]), int(YMD[2])

print(y,'년',m,'월',d,'일')

# 03. 문장을 어절 단위로 분리하고 싶은 경우
sentence = "오늘은 날씨가 참 좋다"
words = sentence.split()

for word in words:
    print(word)

# 04. 공백을 기준으로 입력받은 수를 list에 저장하고 싶은 경우
n = list(map(int, input().split()))

print(n)
