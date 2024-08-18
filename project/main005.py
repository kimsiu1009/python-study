value = int(input('초를 입력하세요: '))

minutes = value // 60
seconds = value % 60

print(value,'초는 ', minutes,'분 ', seconds,'초 입니다.')
