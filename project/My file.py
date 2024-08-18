name = input('이름을 입력하세요: ')
print()
print(f'환영합니다. {name} 님!')
print()
print("지금부터 OX게임을 시작하겠습니다!")

correct = 0

ans = input("남극에서는 감기가 걸릴까요?")
if ans == "O":
   print("틀렸습니다.")
   print()
elif ans == "X":
   print("정답입니다!")
   correct = correct + 1   

ans = input("코데인은 기침에 효과가 있을까요? ")
if ans == "O":
   print("정답입니다!")
   correct = correct + 1    
elif ans == "X":
   print("틀렸습니다.")
print()
print(f"{correct}개를 맞추었습니다!")
print("게임이 끝났습니다.감사합니다!")