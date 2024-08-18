num = 0
total = 0
while True:
    num += 1
    total += num
    print(f"{total}")
    if num >= 100000:
        break
# =================================================================================================


person = { 
    "firstName": "john",
    "lastName" : "Doe",
    "age": 23,
    "eyeColor" : "blue"
}

#딕셔너리에 추가하는 방법

# person["address"] = "busan"

#딕셔너리에 속성을 삭제하는 방법

del person["age"]

print(person)

#====================================================================================================
dic = {
   "firstName": "john",
   "lastName": "Doe",
   "age": 15,
   "height" : 155
}
# 딕셔너리에 새로운 속성을 추가할 경우

# dic["weight"] = 50

# print(dic)

#딕셔너리에 속성을 지우는 방법
del dic["height"] 

print(dic)

#======================================================================================================
def func():
    print("이것은 함수입니다")


func()
# func()
# func()
# func()
# func()
# func()

#함수를 정의하고, 실행(호출)하는 방법

def add(a, b):
    return a + b

def mul(a, b):
    return a * b


print(add(3, 5))
print(add(5, 10))
print(add(1, 2))

print(mul(2, 5))

