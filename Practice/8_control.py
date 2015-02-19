# if 문을 사용한다. 

money =1 

if money :
	print("taxi")
else :
	print("walk")


a =10
if a :
	print("true")
	print("what we can do")
	print("yes we can")
else :
	print("false")

money = 2000

if(money > 3000) or a :
	print("money is much than 2000")
else:
	print("money is less than 2000")

if 1 in [1,2,3] :
	print("1 is in the List")
else:
	print("1 is not in the List")

if 1 not in [1,2,3]:
	print("1 is not in the List")
else:
	print("1 is in the List")

if 'a' in ('a','b','c'):
	print("a is in the tutle")
else:
	print("a is not in the tutle")

pocket = ['paper','handphone']

watch = 1

if 'money' in pocket :
	print("money is in pocket")
else :
	if watch : 
		print("watch is true")
	else :
		print("watch is not dlelelelel")




treehit = 0 

while treehit <10 :
	treehit +=1 
	print("tree is cutted %d" %treehit)

	if(treehit==10):
		print("tree is endndndnd")

'''
coffee = 10
while 1:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break
'''

test_list = ['1','2','3']

for i in test_list :
	print(i)
marks = [90, 25, 67, 45, 80]

number = 0

for mark in marks :
	number = number +1 
	if mark >=60 :
		print("%d 학생은 합격입니다. " %number)
	else :
		print("%d 학생은 불합격입니다. " %number)






