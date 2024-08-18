# # 101

# # true/False : bool(eam)

# # 102

# print(3 == 5)

# # 103

# print(3 < 5)

# # 104

# x = 4
# print(1 < x < 5)

# # 105

# print ((3 == 3) and (4 != 3))

# # 106

# # print(3 => 4)

# # 107

# if 4 < 3:
#  print("Hello World")

# 108

# if 4 < 3:
#  print("Hello World.")
# else:
#  print("Hi, there.")

# # 109

# if True :
#  print ("1")
#  print ("2")
# else :
#  print("3")
# print("4")

# 110

# if True :
#     if False:
#         print("1")
#         print("2")
#     else:
#         print("3")
# else :
#     print("4")
# print("5")

# 111

# if 5 < 9:
#   print("안녕하세요" * 2)

# 112

# user = int(input(": "))
# print(user + 10)

# 113

# user = int(input('입력 : '))
# if user % 2 == 0:
#   print("짝수")
# else:
#   print("홀수")
# (%) = 어떤수를 나누었을때 {나머지를 구하는 연산자.}

# 114

# paul = int(input(": "))
# paul += 20
# if paul > 255:
#   print(255)
# else:
#   print(paul)

# 115

# num = int(input("입력 : "))
# num -= 20
# if num > 255:
#   print(255)
# elif num < 0:
#   print(0)
# else:
#   print(num)

# 116

# time = input("입력 : ")
# if time[-2 :] == "00":
#   print("정각")
# else:
#   print("정각 아님")


# # 117

# fruit = ["사과", "포도", "홍시"]

# user = input("과일 : ")
# if user in fruit:
#   print("정답")
# else:
#   print("오답")

# # 118

# it_company_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

# user = input("회사명 : ")

# if user in it_company_list:
#   print("입사 희망")
# else:
#   print("입사희망 아님")

# sports = ["축구", "테니스", "씨름", "유도"]
# sports1 = input("좋아하는 스포츠 : ")

# if sports1 in sports:
#   print("좋아하는 스포츠입니다.")
# else:
#   print("좋아하는 스포츠가 아닙니다.")

# 119

# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# user = input("제가 좋아하는 계절은 : ")

# if user in fruit:
#   print("정답")
# else:
#   print("오답")
# in : 리스트, 튜플. 딕셔너리에 어떤 값이 있으면 True를 없으면 False를 반환한다

# a = [1, 2, 3, 4]
# if 1 in a:
#   print("있음")

# if 5 in a:
#   print("없음")

# 120

# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# user = input("좋아하는 과일은 : ")
# if user in fruit.values():
#   print("정답")
# else:
#   print("오답")

# 121
# user = input("문자 하나를 입력하세요 : ")

# if user.islower():
#   print(user.upper())
# else:
#   print(user.lower())

# 122
# user = int(input("점수를 입력하세요 : "))
# if 81 <= user <= 100:
#   print("A")
# elif 61 <= user <= 80:
#   print("B")
# elif 41 <= user <= 60:
#   print("C")
# elif 21 <= user <= 40:
#   print("D")
# elif 0 <= user <= 20:
#   print("E")

# 123

# 환율 = {
#   "달러" : 1167,
#   "엔" : 1.096,
#   "유로" : 1268,
#   "위안" : 171
# }
# print(환율)
# user = input("입력 : ")
# num, currency = user.split()# split = 공백 기준으로 문자열을 리스트로 생성해서 변환
# print(float(num) * 환율[currency], "원")
# a, b = [1, 2] : 언팩킹

# 124
# nums = input("세계의 값을 입력하세요. : ")

# nums = nums.split()
# print(max(nums))

# 125
# user = input("휴대전화 번호 입력 : ")

# user = user.split("-")

# if user == "011":
#  com = "SKT"

# elif user == "011":
#  com = "KT"

# elif user == "011":
#  com = "LGU"

# elif user == "011":
#  com = "알수없음"

# 126

# 우편번호 = input("우편번호 : ")
# 우편번호 = 우편번호[:3]

# if 우편번호 in ["010", "011", "012"]:
#     print("강복구")
# elif 우편번호 in ["013", "014", "015"]:
#     print("도붕구")
# elif 우편번호 in ["016","017", "018", "019"]:
#     print("노원구")
# else:
#    print("없음")

# 127

# 주민번호 = input("주민등록번호 : ")
# 주민번호 = 주민번호.split("-")[1]

# if 주민번호[0] == "1" or 주민번호[0] =="3":
#     print("남자")
# elif 주민번호[0] == "2" or 주민번호[0] =="4":
#     print("여자")
# else:
#     print("잘못된 주민번호")

# 128

# user = input("입력 : ")
# user2 = user.split("-")[1]
# user3 = int(user2[1:3])
# if 0 <= user3 and user3 <= 8:
#     print("서울")
# else:
#     print("서울 아님")

# 129

# num = input("주민등록번호 입력 : ")
# num2 = int(num[0]) * 2 + \
#         int(num[1]) * 3 + \
#         int(num[2]) * 4 + \
#         int(num[3]) * 5 + \
#         int(num[4]) * 6 + \
#         int(num[5]) * 7 + \
#         int(num[7]) * 8 + \
#         int(num[8]) * 9 + \
#         int(num[9]) * 2 + \
#         int(num[10]) *3 + \
#         int(num[11]) * 4 + \
#         int(num[12]) * 5
# num3 = 11 - (num2 % 11)
# num4 = str(num3) 
# if num[-1] == num4[-1]:
#     print("유요한 주민등록번호")
# else:
#     print("유요하지 않은 주민등록번호")

# 130

# import requests

# btc = requests.get("https://api.bithumb.com/public/ticker/").json()
# ['data']
 
# 변동쪽 = float(btc['max_price']) - float(btc['min_price'])

# 131

# fruits = ["사과", "귤", "수박"]
# for fruit in fruits:
#     print(fruit)

# 132
# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#     print("#####")

# 133
# for 변수 in ["A", "B", "C"]:
#  print(변수)

# 134

# 변수 = "A"
# print("출력:", 변수)
# 변수 = "B"
# print("출력:", 변수)
# 변수 = "C"
# print("출력:", 변수)

# 135

# for 변수 in ["A", "B", "C"]:
#  b = 변수.lower()
#  print("변환:", b)

# 136

# 변수 = 10
# print(변수)
# 변수 = 20
# print(변수)
# 변수 = 30
# print(변수)

# list = [10, 20, 30]

# for 변수 in list:
#     print(변수)

# 137

# list = [10, 20, 30]

# for 변수 in list:
#     print(변수)

# 138

# for 변수 in list:
#     print(변수)
#     print("-------")

# 139


# for 변수 in list:
#     print(변수)
#     print("++++")

# 140


# list = [10, 20, 30]
# for 변수 in [1, 2, 3, 4]:
#     print("--------")

# 141

# for i in [100, 200, 300]:
#     print(i + 10)

# 142

# 리스트 = ["김밥", "라면", "튀김"]
# for i in 리스트:
#     print(f"오늘의 메뉴 : {i}")

# # 143

# 리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
# for i in 리스트:
#     print(len(i))

# # 144

# 리스트 = ['dog', 'cat', 'parrot']

# for i in 리스트:
#     print("시우")

# # 146

# 리스트 = [1, 2, 3]

# for i in 리스트:
#     print(f"3 x {i}")

# # 147

# 리스트 = [1, 2, 3]

# for i in 리스트:
#     print(f"3 x {i} = {i * 3}")

# 148

# 리스트 = ["가", "나", "다", "라"]

# for i in 리스트[1:]:
#     print(i)

# # 149
# 리스트 = ["가", "나", "다", "라"]

# for i in 리스트[::2]:
#     print(i)

# # 150

# 리스트 = ["가", "나", "다", "라"]

# for i in 리스트[::-1]:
#     print(i)

# # 151

# 리스트 = [3, -20, -3, 44]

# for i in 리스트:
#     if i < 0:
#         print(i)

# # 152

# 리스트 = [3, 100, 23, 44]

# for i in 리스트:
#     if i % 3 == 0:
#         print(i)

# 153

# 리스트 = [13, 21, 12, 14, 30, 18]

# for i in 리스트:
#     if i % 3 == 0 and i < 20:
#         print(i)

# 154

# 리스트 = ["I", "study", "python", "language", "!"]

# for i in 리스트:
#     if len(i) >= 3:
#         print(i)

# 155

# 리스트 = ["A", "b", "c", "D"]

# for i in 리스트:
#     if i.isupper():
#         print(i)

# # 156
    
# 리스트 = ["A", "b", "c", "D"]

# for i in 리스트:
#     if i.islower():
#         print(i)

# # 157

# 리스트 = ['dog', 'cat', 'parrot']

# for i in 리스트:
#     print(i.capitalize())

# # 158

# 리스트 = ['hello.py', 'ex01.py', 'intro.hwp']

# for i in 리스트:
#     split = i.split(".")
#     print(split[0])

# 160

# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

# for i in 리스트:
#     split = i.split(".")
#     if split[1] == 'h' or split[1] == 'c':
#         print(i)

# 161

# for i in range(100):
#     print(i)

# 162

# for i in range(2002, 2051, 4):
#     print(i)

# 163

# for i in range(3, 31, 3):
#     print(i)

# 164
#  
# for i in range(100):
#     print(99 -i)

# for i in range(99, -1, -1):
#     print(i)

# 165

# for i in range(10):
#     print(i / 10)

# 166

# for i in range(1, 10): 
#     print(f"3 x {1} = {3 * i} ")

# 167

# for i in range(1, 10, 2): 
#     print(f"3 x {1} = {3 * i} ")

# 168

# total = 0

# for i in range(1, 11):
#     total = total + i
#     print(total)

# 169
# total = 0

# for i in range(1, 11, 2):
#     total = total + i
#     print(total)

# 170

# total = 0

# for i in range(1, 11):
#     total = total * i
# print(total)

# 171

# price_list = [32100, 32150, 32000, 32500]

# for i in range(len(price_list)):
#     print(price_list[i])

# 172

# price_list = [32100, 32150, 32000, 32500]

# for i in range(len(price_list)):
#     print(i, price_list[i])

# 173

# price_list = [32100, 32150, 32000, 32500]

# for i in range((price_list)):
#     print((len(price_list - 1)) - i, price_list[i])

# # 174

# price_list = [32100, 32150, 32000, 32500]

# for i in range(1, len(price_list)):
#     print(90 + 10* i,price_list)

# 175

# my_list = ["가", "나", "다", "라"]

# # print(my_list(0), my_list[1])
# # print(my_list(1), my_list[2])
# # print(my_list(2), my_list[3])

# for i in range(0, len(my_list)-1):
#     print(my_list[i], my_list[i + 1])

# 176
# my_list = ["가", "나", "다", "라", "마"]

# # print(my_list(0), my_list[1], my_list[2])
# # print(my_list(1), my_list[2], my_list[3])
# # print(my_list(2), my_list[3], my_list[4])

# for i in range(1, len(my_list)-1):
#     print(my_list[i-1], my_list[i], my_list[i + 1])

# 177

# my_list = ["가", "나", "다", "라"]
# print(my_list[3], my_list[2] )
# print(my_list[2], my_list[1] )
# print(my_list[1], my_list[0] )

# for i in range(len(my_list) - 1, 0, -1):
#     print(my_list(i), my_list[i-1])