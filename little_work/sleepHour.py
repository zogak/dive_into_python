'''
일어나는 시간과 자는 시간을 입력하면, 수면 시간이 몇 시간인지 계산해 주는 프로그램

[입력 예시]
* 시간을 24시간 단위로 입력
일어나는 시간? 7 30
자는 시간? 23 40
'''

def sleepingHour():
    wakeUpHour, wakeUpMinute = map(int, input('일어나는 시간? ').split())
    sleepHour, sleepMinute = map(int, input('자는 시간? ').split())

    wakeTotalMinute = wakeUpHour*60 + wakeUpMinute
    sleepTotalMinute = sleepHour*60 + sleepMinute

    if wakeTotalMinute > sleepTotalMinute:
        sleep = wakeTotalMinute - sleepTotalMinute

    elif wakeTotalMinute < sleepTotalMinute:
        sleep = 24*60 - (sleepTotalMinute - wakeTotalMinute)
    
    sleepHour = sleep // 60
    sleepMinute = sleep % 60

    return sleepHour, sleepMinute

sleepHour, sleepMinute = sleepingHour()
print('수면 시간은 %d시간 %d분' %(sleepHour,sleepMinute))



