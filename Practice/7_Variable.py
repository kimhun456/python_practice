# Variable.py

'''

파이썬에서 모든 변수는 객체라고 할 수 있다.  

예를 들어서 a = 3 이라고 하면 

a는 reference 3은 object라고 할수 있고 a 는 3이라는 object를 가르치는것이다. 



'''

a = 3
b = 3 
print(a is b)

# 변수를 만드는 여러가지 방법 

a,b = 'python', 'key'

print("asdf %s %s " %(a,b))

(a,b) = ("what","is")

print("%s %s " %(a,b))

[a,b] = ["aaaaaa","bbbbbb"]

print("%s %s" %(a,b))

a = b = "wasdf"

print(a)
print(b)

a = [1,2,3]

b = [1,2,3]

c = a[:]

a[1]=5
c[2]=0

print("%s %s %s " %(a,b,c))

from copy import copy
b= copy(a)

print(b)
print(b is a)
