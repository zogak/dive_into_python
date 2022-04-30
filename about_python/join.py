'''
join
리스트에 있는 value를 string으로 이어붙이는 방법
'''
#ex1
chars = ['a', 'b', 'c']
ex1 = "".join(chars)
print(ex1)

#ex2
nums = [1, 2, 3]
nums = map(str, nums)
ex2 = "-".join(nums)
print(ex2)

#ex3
k = ['old', 'ferry', 'donut']
ex3 = ' '.join(k)
print(ex3)