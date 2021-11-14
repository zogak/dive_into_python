'''
time module 사용하기
'''
import time, datetime

'''
unix time이란?
1970년 1월 1일 00:00:00 이후로 경과한 시간을 초로 환산하여 정수로 나타낸 것
'''
unixUTC = int(time.time())
print(unixUTC)