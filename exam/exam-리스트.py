# 51

movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)
# 52

movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

movie_rank.append("베트멘")
print(movie_rank)

# 53

movie_rank = ["닥터 스트레인지", "스플릿", "럭키", "베트멘"]

movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 54

movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']

del movie_rank[3]
print(movie_rank)
#리스트 요소 삭제 -> del

# 55

movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']

del movie_rank[2]
print(movie_rank)
del movie_rank[2]
print(movie_rank)

# 56

lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

langs = lang1 + lang2
print(langs)

# 57

nums = [1, 2, 3, 4, 5, 6, 7]
print("max", max(nums))# 최대값
print("min", min(nums))# 최소값

# 58

nums = [1, 2, 3, 4, 5]
result = sum(nums)
print(result)

# 리스트에 값의 합을 구할때 : sum() 함수

# 59

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]

lenght = len(cook)
print(lenght)

# 60

nums = [1, 2, 3, 4, 5]
average = sum(nums) / len(nums)
print(average)

# 61

price = ['20180728', 100, 130, 140, 150, 160, 170]

result = price[1:]
print(result)

# 62

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = nums[::2]
print(result)

# 63

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = nums[1::2]
print(nums)

# 64

nums = [1, 2, 3, 4, 5]
result = nums[::-1]
print(result)
# 리스트 순서를 바꾸기

# 65

interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

# 66

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
result = " ".join(interest)
print(result)

# 67

result = "/".join(interest)
print(result)

#68

result = "\n".join(interest)
print(result)

# 69

string = "삼성전자/LG전자/Naver"
result = string.split("/")
print(result)

# 70

data = [2, 4, 3, 1, 5, 10, 9]

data.sort()  #오름차 순으로 정렬
print(data)



