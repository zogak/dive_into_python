'''
문자열 formatting에 대해 정리합니다.
'''
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