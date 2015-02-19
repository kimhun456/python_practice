# sets.py
'''
set의 특징은 1. 중복을 허락하지 않는다. 2. 순서가 없다. (unorderd)
'''

s1 = set([1,2,3])

print(s1)

s2 = set("Hello")

print(s2)

l1 = list(s1)

print(l1)
print(l1[0])

s1 = set([1,2,3,4,5])
s2 = set([2,3,4,6,7])

#합집합
print(s1|s2)

#차집합
print(s1-s2)

#교집합
print(s1&s2)

# set에 추가및 삭제 법 add = 한개만 추가 , update = 2개이상 추

s1.add(6)

print(s1)

s1.update([10,11,12])

print(s1)

s1.remove(12)

print(s1)