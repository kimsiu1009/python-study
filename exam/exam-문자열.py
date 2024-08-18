print("Hello Word")

print("Mary's cosmetics")

print('산씨가 소리질렀다. "도둑이야".')

print("C:\Windows")

print("안녕하세요.\n만나서\t\t반갑습니다.")
#이스케이프 코드

print("오늘은", "일요일")
#쉼표 = 스페이스 1

print("naver", "kakao", "samsung", sep = " ")
print("naver", "kakao", "samsung", sep = ";")
#(sep = ) = 공백을 사이에 너어줌(한 줄에서)

print("naver", "kakao", "samsung", sep = "/")

print("first", end = " ")
print("second")
            
#(end = ) = 줄을 이어붙일 때

print(5 / 3)


coffee = 5
price = 5000
print(f"총금액 : {coffee * price}원 ")

시가총액 = 298000000000000
현재가 = 50000
PER = 15.79

print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))
#type = 변수의 유형을 출력한다.

# 13

s = "hello"
t = "python"
print(s + "! " +  t )

# 14

print((2 + 3) * 3)

# 15

a = "132"
print(type(a))
# str(ing) = 문자열
# int = 정수
# float = 실수

# 16

# 문자열 -> 정수 : int()
# 정수 -> 문자열 : str()
# 문자열 -> 실수 : float()

num_str = "720"
num = int(num_str)
print(num, type(num))

# 17

num = 100
num_str = str(num)
print(num_str, type(num_str))

# 18

abc = "15.79"
abc = float(abc)
print(abc, type(abc))

# 19

year = "2024"
year = int(year)
print(year - 2)
print(year - 1)
print(year)

# 20

price = 48594
print(price * 36)

# 21

letter ='python'
print(letter[0], letter[2])

# 22

license_plate = "24가 2210"
print(license_plate[4:])

# 23

string = "홀짝홀짝홀짝"

print(string[::2])
print(string[1::2])

# 24

string = "PYTHON"
print(string[::-1])

# 25

phone_number = "010-1111-2222"

result = phone_number.replace("-", " ")
print(result)

# 26

phone_number = "010-1111-2222"

result = phone_number.replace("-", "")
print(result)

# 27

url = "http://sharebook.kr"

result = url.split(".")
print(result[1])

# 28

#error이 발생한다.

# 29

string = 'abcdfe2a354a32a'
rusult1 = string.replace("a", "A")
print(rusult1)

# 30

string = 'abcd'
a = string.replace('b', 'B')
print(a)

# 31

a = "3"
b = "4"
print(a + b)#"34"

# 32

print("Hi" * 3)

# 33

print("-" * 80)

# 34

t1 = 'python'
t2 = 'java'
print((t1 + " " + t2 + " ") * 4) 

# 35

name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13

print("이름 : %s 나이: %d" % (name1, age1))
print("이름 : %s 나이: %d" % (name2, age2))

# 36 

print("이름 : {0} 나이: {1}".format(name1, age1))
print("이름 : {0} 나이: {1}".format(name2, age2))

# 37

print(f" {name1} 나이 : {age1}")
print(f" {name2} 나이 : {age2}")

# 38

number = "5,969,782,550"
result = number.replace(",", "")
result = int(result)
print(result, type(result))

# 39

분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

# 40

data = "   삼성전자    "
print(data.strip())

# 41

ticker = "btc_krw"
print(ticker.upper())

# 42

ticker = "BTC_KRW"
print(ticker.lower())

# 43

a = 'hello'
result = "H" + a[1:]
print(result)

a = 'hello'
print(a.capitalize())

#44

file_name = "보고서.xlsx"
result = file_name.endswith("xlsx")
print(result)
#endswith()
#주어진 문자열 끝나는 지를 검사

# 45

#여러개 조건으로 검사할 때는 ()로 묶어 준다
file_name = "보고서.xlsx"
result = file_name.endswith(("xlsx", "xls"))# or 조건
print(result)

# 46

file_name = "2020_보고서.xlsx"
result = file_name.startswith("2020")
print(result)

#startswith() 는 어떤 문자가 주어진 문자로 시작하는지 검사한다

# 47

a = "hello world"
result = a.split(" ")
print(result)

#문자열을 split()함수로 나누면, 결과가 리스트가 된다

# 48___

ticker = "btc_krw"
result = ticker.split("_")
print(result[0])
print(result[1])

# 49

date = "2020-05-01"
result = date.split("_")
print(result)

# 50

data = "039490     "
result = data.rsplit
print(result)\

# split() : 왼쪽, 오른쪽 모두 공백 제거
# lsplit() : 왼쪽 공백 제거
# rsplit() : 오른쪽 공백 제거