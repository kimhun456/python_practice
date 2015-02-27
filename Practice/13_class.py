# class 를 배운다. 

class FourCal:
	def setData(self,first,second):
		self.first = first
		self.second = second
	def sumData(self):
		print(self.first + self.second)
	def subData(self):
		print(self.first - self.second)
	def mulData(self):
		print(self.first * self.second)
	def divData(self):
		print(self.first / self.second)

a = FourCal()
a.setData(10,3)
a.sumData()
a.subData()
a.mulData()
a.divData()


# __inii__ 를 이용해 생성자를 만들고 __del__을 이용하여 소멸자를 만들 수 있다. 
class HousePark:
	lastname = "박"
	def __init__(self,name):
		self.name = self.lastname + name
	def travel(self, place):
		print("%s는 %s로 여행을 떠난다." %(self.name, place))
	def __del__(self):
		print("%s 는 죽는다. " %self.name)
	def __add__(self,other):
		print("%s 랑 %s는 같이 결혼한다." % (self.name,other.name))

pey = HousePark("현재")
pey.travel("부산")


class HouseKim(HousePark):
	lastname = "김"

a = HouseKim("현재")
print(a.lastname)