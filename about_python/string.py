'''
문자열 다루는 법에 대해 정리합니다.
'''

# 문자열 slicing
sentence1 = "I made a snowman."
print(sentence1[2:6])
print(sentence1[9:-1])

# 마지막 문자를 없애고 싶은 경우
sentence2 = "This is my dog,"
sentence2 = sentence2[:-1]
print(sentence2)

# 문자열 formatting
def cookie(howMany):
    if howMany == 0:
        print("I have no cookie")
    elif howMany == 1:
        print("I have %d cookie" %howMany)
    elif howMany > 1:
        print("I have %d cookies" %howMany)

cookie(0)
cookie(1)
cookie(3)