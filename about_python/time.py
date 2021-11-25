'''
time module 사용하기
'''

import time, datetime
from datetime import timezone

'''
unix time이란?
1970년 1월 1일 00:00:00 이후로 경과한 시간을 초로 환산하여 정수로 나타낸 것
'''
currentUnix = int(time.time())
print('현재 unix 시간 ', currentUnix)

# datetime 형식으로 바꾸는 방법
print(type(currentUnix)) #int
currentUnixDatetimeFormat = datetime.datetime.fromtimestamp(currentUnix)
print(type(currentUnixDatetimeFormat)) #datetime

# human time으로 바꾸는 방법
humanTime1 = currentUnixDatetimeFormat.strftime('%Y-%m-%d %H:%M:%S')
humanTime2 = currentUnixDatetimeFormat.strftime('%Y-%m-%d')
humanTime3 = currentUnixDatetimeFormat.strftime('%H:%M:%S')
print('humanTime')
print(humanTime1)
print(humanTime2)
print(humanTime3)

# unix time UTC
currentUnixUTC = currentUnixDatetimeFormat.replace(tzinfo = timezone.utc).timestamp()
print('현재 unix UTC 시간 ', int(currentUnixUTC))
print(datetime.datetime.fromtimestamp(currentUnixUTC).strftime('%Y-%m-%d %H:%M:%S'))

