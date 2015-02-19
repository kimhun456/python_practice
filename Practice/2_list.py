#list.py 


#list의 기본형 [] 속의 값이 리스트로 여겨진다. 
a = [1,2,3]

print(a)
#a리스트의 0번쨰 부분을 출력한다. 
print(a[0])
#a 리스트의 0번쨰와 1번째를 더한다. 
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


# 3번쨰부터 끝까지를 출력한다. 
c = a[3:]

print(c)

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]

print(a[:4])
print(a[3][:3])

a = [1,2,3]
b = [4,5,6]


역시 곱하기가 가능하다.
print (a*3)

a = [1,2,3]


print (a)


a[1:2] = ["a","b","c"]

print (a)

a[1:3] =[]

print(a)
del(a[1])
print(a)

a = [1,2,3]
a.append(4)
print(a)

# 리스트에 추가하는 함수
a.append([5,6])
print(a)

a = [1,3,7,2,4]
a.sort()
print(a)

a =  ["asf", "abdd",  "abc "]
print(a)

#리스트를 정렬시킨다. 문자열도 abc 순서에 따라 정렬 한다. 
a.sort()
print(a)

a = [1,3,4,5]

#list를 반전시킨다. ( 정렬 후 반전 시키는 것이 아닌 그대로를 반전시키는 것 )
a.reverse()

print(a)

# x 의 index를 반환한다. 
print(a.index(4))

a = [1,2,3,4,5]

# 1번쨰 위치에 주어진 요소를 대입한다. 
a.insert(1,"asfd")

print(a)


# 리스트에 2가 있다면 삭제하고 없다면 에러를 출력한다. 
a.remove(2)

print(a)

a= [1,2,3,4,5]

#3번쨰에 있는 요소를 돌려주고 삭제한다. 
a.pop(3)

print(a)

print(a.count(1))

a= [1,2,3,4]

b= ["a","b","c"]

#a의 리스트에 b의 리스를 더한다. 
a.extend(b)

print(a)