'''
set
- intersection
- union
'''

setA = set([1, 2, 3])
setB = set([2, 3, 4])

print('setA : ', setA)
print('setB : ', setB)

intersection = setA&setB
union = setA|setB

print('intersection : ' ,intersection)
print(union)

intersection2 = setA.intersection(setB)
union2 = setA.union(setB)

print(intersection2)
print(union2)