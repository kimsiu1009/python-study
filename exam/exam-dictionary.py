# 84

temp = {}

# 85

temp = {
    "메로나" : 1000, 
    "폴라포" : 1200,
    "빵빠레" : 1800
}
# 메로나 = 키
# 1000 = value

# 86

temp = {
    "메로나" : 1000, 
    "폴라포" : 1200,
    "빵빠레" : 1800
}
temp['죠스바'] = 1200
temp['월드콘'] = 1500
print(temp)

# 87

ice = {'메로나': 1000,
 '폴로포': 1200,
 '빵빠레': 1800,
 '죠스바': 1200,
 '월드콘': 1500}
result = ice['메로나']
print(result)

# 88
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
ice['메로나'] = 1300
print(ice)
# 89
# 딕셔너리 삭제 방법

ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

del ice['메로나']
print(ice)

# 90

icecream = {
'폴라포': 1200, 
'빵빠레': 1800, 
'월드콘': 1500, 
'메로나': 1000}
icecream['누가바']

# 91

inventory = {
    "메로나" : [300, 20],
    "비비빅" : [400, 3],
    "죠스바" : [250, 100]
}

# 92

inventory = {
    "메로나" : [300, 20],
    "비비빅" : [400, 3],
    "죠스바" : [250, 100]
}

print(inventory["메로나"][0], "원")

# 93

inventory = {
    "메로나" : [300, 20],
    "비비빅" : [400, 3],
    "죠스바" : [250, 100]
}

print(inventory["메로나"][1], "개")

# 94

inventory = {"메로나": [300, 20],
 "비비빅": [400, 3],
 "죠스바": [250, 100]}

inventory['월드콘'] = [500, 7]
print(inventory)

# 95

icecream = {'탱크보이': 1200,
             '폴라포': 1200,
             '빵빠레': 1800,
             '월드콘': 1500,
             '메로나': 1000}

lst = list(icecream.keys())
print(lst)

# 96


icecream = {'탱크보이': 1200,
             '폴라포': 1200,
             '빵빠레': 1800,
             '월드콘': 1500,
             '메로나': 1000}
value = list(icecream.values())
print(value)

# 97

icecream = {'탱크보이': 1200,
             '폴라포': 1200,
             '빵빠레': 1800,
             '월드콘': 1500,
             '메로나': 1000}

print(sum(icecream.values()))

# 98

icecream = {'탱크보이': 1200,
             '폴라포': 1200,
             '빵빠레': 1800,
             '월드콘': 1500,
             '메로나': 1000}

new_product = {
    '팥빙수':2700, 
    '아맛나':1000
    }

icecream.update(new_product)
print(icecream)

# 99

keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

result = dict(zip(keys, vals))
print(result)

# 100

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
dic = dict(zip(date, close_price))
print(dic)