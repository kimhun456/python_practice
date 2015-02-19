#list.py 

a = [1,2,3]

print(a)
print(a[0])

print(a[0]+a[1])

a= [1,2,3,['a','b','c']]

print(a)

print(a[3])
print(a[-1][0])

a = [1,2,3, ["life" , "out" , [ 1,2,3 ]]]

print(a[3][2][1])

a = [1,2,3,4,5]

b = a[:2]

print(b)

c = a[3:]

print(c)

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]

print(a[:4])
print(a[3][:3])