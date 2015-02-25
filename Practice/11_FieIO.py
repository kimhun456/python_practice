# file i/o 에 대하여 배우게 된다.

#open 함수를 이용하여 어떤 파일을 읽어올지 선택가능 하다.
f = open("www.txt",'w')

for i in range(10):
	data = "the data number is %d \n" %i
	f.write(data)
f.close()

f1 = open("www.txt","r")

while 1:
	line = f1.readline()
	if not line : break
	#print(line)

f1.close()

f = open("www.txt","r")
lines = f.readlines()

for l in lines:
	print(l)
f.close()

f = open("www.txt","r")
data = f.read()
print(data)
f.close()