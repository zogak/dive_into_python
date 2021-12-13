'''
dictionary 에 대해 정리합니다.
'''
# 새로운 딕셔너리 생성
info = dict()

# 딕셔너리에 key value 생성
info['Mon'] = 3
info['Tue'] = 4
info['Wed'] = 1
info['Thur'] = 7
info['Fri'] = 2
info['Sat'] = 5

# key로 value 찾기
print(info['Mon'])
print(info.get('Mon'))

try:
    res = info['Sun']
    print(res)
except Exception as e:
    print(e)

print(info.get('Sun'))

# (key, value) tuple 값 얻기
print(info.items())