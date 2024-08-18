# 71 

my_variable = ()
print(my_variable, type(my_variable))

# 72

movie_rank = ("닥터 스트레인지", "스플릿", "럭키")

# 73

t1 = (1,)
print(type(t1))

# 74

t = (1, 2, 3)
t[0] = 'a'
#ERROR
#튜플 -> 값 변경 않됨

# 75

t = 1, 2, 3, 4
t = (1, 2, 3, 4)
#튜플은 가로를 생략할 수 있다

# 76

t = ('a', 'b', 'c')
#튜플 새로 정의
t = ('A', 'B', 'C')

# 77

interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(interest)

# 78

interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = tuple(interest) # 튜플 변화 함수
print(interest)

# 79

data = tuple(range(2, 100, 2))
print(data)

# 80 

temp = ('apple', 'banana', 'cake')

a, b, c = temp
print(a)
print(b)
print(c)

# 81

lst = {1, 2, 3, 4, 5, 6}
a, b, *c = lst
print(a)
print(b)
print(c)

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _, = scores
print(valid_score)

# 82

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, _, *valid_score = scores
print(valid_score)


# 83

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

_, *valid_score, _ = scores
print(valid_score)