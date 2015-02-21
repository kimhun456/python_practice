# 함수에 관하여 배우게 된다. 
def sum(a,b):
	return a+b

a = 3
b = 2
print(sum(a,b))

def hi():
	return "hi"

print(hi())

def printSum(a,b):
	print("%s 와 %s 의 합은 %s 입니다." % (a,b,a+b))

printSum(123,123)


# 함수를 사용할 때 입력변수의 숫자를 알수 없다면 *변수명을 사용하여 입력하면 여러개의 입력을 자동으로 받을수 있다. 
def sum_many(*args):
	sum = 0 
	for i in args:
		sum += i
	return sum

print (sum_many(1,2,3,4,5,6))

def sum_mul(choice, *args):
	if choice =="sum":
		result = 0
		for i in args:
			result += i
		print(result)
	elif choice =="mul":
		result = 1 
		for i in args:
			result *= i
		print(result)

sum_mul("mul",1,2,3,3,4,5)


def say_mysel(name,age, sex =1) :

	print("이름은 %s 나이는 %s 성별은 " %(name,age))
	if sex==1 :
		print("남자입니다.")
	else:
		print("여자입니다.")

say_mysel("guswo",123)



