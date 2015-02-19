# string.py

print("Hello world")

#여러줄짜리 기호를 포함시키기 위해서는 """ 를 사용하면 \n 이 들어간다고 볼수있다. 

"""

파이썬에서 문자열 만드는 방법 4가지 

1. 'Hello world'
2. 'Python is fun'
3.  '''Life is too short, you need python  '''

"""

s = """ what i can say is that there are so many Things to learn the Computer Science
and it makes me something exciting feeling"""

a = " what's you gonna do " 

b = 'hey whay are you doing '

c = '''asfsafasfasdf"sfasfa"sfasfasf"asfs safd s'dfas fsa '''

head = "what i wanna "
tail = "is the party!!!"

a = "Life is too short, you need Python"

print(a)

#index 기법
a[1] 
#문자열의 마지막을 가르키게 하고 싶을 경우에는 -1 을 쓴다.  ex ) 
a[-1]

#slicing 기법 마지막 인덱스는 처리하지 않는다 마지막인덱스는 3이었는데 그럼에도 LIFE가 나온것은 마지막을 무시하고 처리한다는것 
# [a:b] 라는 것은 a<= x < b 라는 것이다.
a[0:4]
print(a[0:4])

# 숫자를 입력하지 않으면 처음 혹은 끝 까지 처리를 한다는 의미를 갖는 것이다. 
print (a[:5])
print (a[5:])

b = "20150220rainy"

print (b[:4])
print(b[4:8])
print(b[8:])

# pithon 을 python 으로 바꾸고 싶을 경우 슬라이싱을 이용한다 직접 접근하면 에러가 발생하게 된다!!

a = "Pithon"

b = a[:1] + 'y' + a[2:]

print(b)

# 문자 포매팅을 사용한다. %d ,%f ,%s 등이 있다. 

print ("what we gonna do %d" % 3)
print ("what we gonna do %s" % "is what we can do")

number = 3 

print("1 + 2 is %d " % number)

number = 4

day = "saturday"


# %s는 % 뒤의 값을 자동으로 문자열로 치환해준다.
print (" today is %s and next day is September on %d "  %(day,number))

print (" today is %s and next day is September on %s " % (day,number))

num = 12.1234567

#오른쪽 정렬은 양수 
print("%10.4f" %num)
#왼쪽 정렬은 음수로 사용한다. 
print("%-10.4f" %num)

a = 'hi'

print (a.upper())

a = "HI"

print (a.lower())

a= "hobby"

print (a.count('b'))

a= 'Pyhton is best thing'

print(a.find('best'))

print (a.index('i'))


a = ","

print(a.join("abcd"))

a= " hi "

print (a.rstrip())
print (a.strip())

# replace 를 이용하여 교체할수있다.
a = "Life is too short "

print( a.replace("Life" , "Leg")  )

# split 함수를 이용하여 문자열을 나눠줄수있다. 아무것도 입력하지 않으면 공백을 이용하여 split한다.

print (a.split())


