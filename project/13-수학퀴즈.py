import random
import time

logo = """
    88     ad888888b,     ad888888b,  
  ,d88    d8"     "88    d8"     "88  
    88         ,d8P"          aad8"   
    88       a8P"             ""Y8,   
    88    d8"            Y8,     a88  
    88    88888888888     "Y888888P'  
"""
menu = """
======================
1. +
2. -
======================
"""

print(logo)
print("수학 퀴즈 게임에 오신것을 환영합니다.")
print(menu)

print()

choice = input(" +, - 중에 하나를 선택해주세요. : ")

score = 0
count = 0
play = True

start_time = time.time()

while play:
    count += 1
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    num3 = random.randint(1, 9)
    if choice == "+":
        answer = num1 * (num2 + num3)
    elif choice == "-":
        answer = num1 * (num2 - num3)
        

    user_input = int(input(f"{num1} x ({num2} {choice} {num3}) = "))

    if answer == user_input:
        score += 1
        print(f"정답입니다. 현재 점수는 {score}입니다.")
    else:
        print(f"아쉽습니다. 정답은 {answer}입니다.")

    if count == 10:
        play = False

end_time = time.time()

print()
print("수학 퀴즈 게임이 종료되었습니다.")
print(f"총 {count}회 도전하여, {score}점을 획득하였습니다.")
print(f"문제를 푸는데 걸린 총 시간은{round(end_time - start_time)}초 입니다.")
