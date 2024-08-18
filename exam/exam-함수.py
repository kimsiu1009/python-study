# 201

# def print_coin():
#     print("beat coin")

# # 202

# def print_coin():
#     print("beat coin")
# # print_coin() # 함수 호출

# # 203

# def print_coin():
#     print("beat coin")

# for i in range(100):
#     print_coin()

# 204

# def print_coin():
#      print("beat coin")
     
# def print_coins():
#     for i in range(100):
#         print_coin()
# print_coins()

# 205

# def hello():
#  print("Hi")
# hello() 

# # 206

# def message() :
#  print("A")
#  print("B")
# message()
# print("C")
# message()

# # 207

# print("A")
# def message() :
#  print("B")
#  print("C")
#  message()

# 208

# print("A")
# def message1() :
#  print("B")
#  print("C")
# def message2() :
#  print("D")
# message1()
# print("E")
# message2()

# 209

# def message1():
#     print("A")
# def message2():
#     print("B")
#     message1()

# # 210

# def message1():
#     print("A")
# def message2():
#     print("B")
# def message3():
#     for i in range (3) :
#         message2()
#         print("C")
#     message1()
# message3()

# 211

# def 함수(문자열) :
#  print(문자열)

# 함수("안녕")
# 함수("Hi")
# 함수의 매개 변수 

# def 함수이름(매개변수)

# def add(num1, num2):
#     print(num1 + num2)

# def sub(num1, num2):
#     print(num1 - num2)

# def div(num1, num2):
#     print(num1 / num2)

# def mul(num1, num2):
#     print(num1  *  num2)

# add(5, 10)
# sub(5, 10)
# div(10, 5)
# mul(5, 10)

# 212

# def 함수(a, b) :
#  print(a + b)
# 함수(3, 4)
# 함수(7, 8)

# def 함수(문자열) :
#  print(문자열)
# 함수()

# 214

# def 함수(a, b) :
#  print(a + b)
# 함수("안녕", 3)

# 215

# def print_with_smile(a):
#     print(a + ":D") 
# print_with_smile("a")

# 217

# def print_upper_price(price):
#     print(price * 1.3)
# print_upper_price(10000)


# 218

# def print_sum(a, b):
#     print(a + b)
# a = 3
# b = 4
# print_sum(a, b)

# 219
# def print_arithmetic_operation(a, b):
#     print(f"{a} + {b} = {a + b}")
#     print(f"{a} - {b} = {a - b}")
#     print(f"{a} * {b} = {a * b}")
#     print(f"{a} / {b} = {a / b}")

# print_arithmetic_operation(3, 4)

# 220

# def print_max(a, b, c):
#     max_val = 0
#     if a > max_val:
#         max_val = a        
#     if b > max_val:
#         max_val = b        
#     if c > max_val:
#         max_val = c
#     print(max_val)        
# print_max(3, 9, 2)

# 221

# def print_reverse(a):
#     print(a[::-1])
# print_reverse("python")

# 222

# def print_score(list):
#     average = sum(list) / len(list)
#     print(average)
# print_score([1, 2, 3])

 # 223
# def print_keys(list):
#     for i in list:
#         if i % 2 == 0:
#             print(i)

# print_keys([1, 3, 2, 10, 12, 11, 15])

# 224

# def print_keys (dictionary):
#     for key in dictionary:
#         print(key)
# print_keys ({"이름":"김말똥", "나이":30, "성별":0})

# # 225

# my_dict = {"10/26" : [100, 130, 100, 100],
#  "10/27" : [10, 12, 10, 11]}

# def print_value_by_key(dic, date):
#     print(dic[date])

# print_value_by_key(my_dict, "10/26")

# 226

# def print_5xn(string):
#     lines = int(len(string))
#     for i in range(lines + 1):
#         print(string[i * 5: i * 5 + 5])
# print_5xn("아이엠어보이유알어걸")

# 227

# def print_5xn(string, num):
#     lines = int(len(string / num))
#     for i in range(lines + 1):
#         print(string[i * 5: i * 5 + 5])
# print_5xn("아이엠어보이유알어걸, 3")
# print_5xn("아이엠어보이유알어걸, 2")

# 228

# def calc_monthly_salary(annual_pay):
#     monthly_pay = int(annual_pay / 12)
#     return monthly_pay
# monthly_pay = calc_monthly_salary(12000000)
# print(monthly_pay)

# 229

# def my_print (a, b) :
#  print("왼쪽:", a)
#  print("오른쪽:", b)
# my_print(a=100, b=200)

# 230

# def my_print (a, b) :
#  print("왼쪽:", a)
#  print("오른쪽:", b)
# my_print(b=100, a=200)

# 231

# def n_plus_1 (n) :
#     result = n + 1
#     n_plus_1(3)
#     print (result)

# 232

# def make_url(string):
#     return "www." + string + ".com"
# url = make_url("naver")
# print(url)

# 233

# def make_list(string):
#     return list(string)
# list = make_list("python")
# print(list)

# # 234

# def pickup_even(list):
#     result = []
#     for i in list:
#         if i % 2== 0:
#             result.append(i)
#         return result
# result1 = pickup_even([3, 4, 5, 6, 7, 8])
# print(result1)

# 235

# def convert_int(string):
#     string = string.replace(",", "")
#     num = int(string)
#     return num

# result = convert_int("1,234,567")
# print(result)

# # 236

# def 함수(num) :
#  return num + 4
# a = 함수(10)
# b = 함수(a)
# c = 함수(b)
# print(c)

# # 237

# def 함수(num) :
#  return num + 4
# c = 함수(함수(함수(10)))
# print(c)

# 238

# def 함수1(num) :
#  return num + 4
# def 함수2(num) :
#  return num * 10
# a = 함수1(10)
# c = 함수2(a)
# print(c)

# def 함수1(num) :
#  return num + 4
# def 함수2(num) :
#  return num * 10
# a = 함수1(10)
# c = 함수2(a)
# print(c)

# 239

# def 함수1(num) :
#  return num + 4
# def 함수2(num) :
#  num = num + 2
#  return 함수1(num)
# c = 함수2(10)
# print(c)

# 240

# def 함수0(num) :
#  return num * 2
# def 함수1(num) :
#  return 함수0(num + 2)
# def 함수2(num) :
#  num = num + 10
#  return 함수1(num)
# c = 함수2(2)
# print(c)