'''
list에 대해 정리합니다.
'''

a = [1, 2, 3]
b = ['apple', 'orange', 'grape']
c = [1, 1, 2, 3, 4, 5, 5, 5]
d = []

# list의 element에 접근하는 법
print(a[0], a[1], a[2])

# list의 element의 index를 알고싶은 경우
print(a.index(1))           #0
print(b.index('grape'))     #2

# list에 특정 element가 존재하는지 확인
print(1 in a)               #True
print('strawberry' in b)    #False

# list에 특정 element가 몇 개 존재하는지 확인
print(c.count(1))       #2
print(c.count(5))       #3

# list가 비었는지 여부
if not d :
    print('not d')
else:
    print('d:',d)