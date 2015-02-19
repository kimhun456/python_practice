# dictionary 는 키와 값으로 이루어진 자료형이다. 

user = {"name":"HyunJae", "phone_number":"010-4011-7501" ,"age":25}

print(user)

print(user["name"])

print(user["phone_number"])

user["address"] = "Seoul YonhSan-Gu " 

print(user['address'])

print(user)

# del 명령을 이용하여 name 키값을 삭제한다. 
del user['name']

print(user)

#dictionary.keys() 를 이용하여 dict_keys객체를 생성한다. 키만을 가지고 있는 객체이다. 
user.keys()
print(user.keys())

for k in user.keys():
	print(k)

print(list(user.keys()))

# dictionary.values() 를 이용하여 dict_values 객체를 생성한다. 밸류를 가지고 있는 객체이다. 

print (user.values())

#dictionary.items()를 이용하여 dict_items 객체를 생성한다. 이것은 키와 밸류를 모두 가지고 있는 객체이다. 
print (user.items())

print(user.get("address"))

# get(a,b) 만약 a라는 키가 없다면  b라는 값이 리턴되게 된다. 
print(user.get("name","hyujae"))

# in 명령어를 사용하여 해당 딕셔너리에 키값이 있는지 확인한다. 
print("name" in user)
print("address" in user)