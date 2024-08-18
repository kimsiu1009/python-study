import random
prompt =  """
...1부터 3사이의 숫자를 입력하세요. 
"""

score = 0
game = True
while game:
    print(prompt)
    number = int(input())

    computer = random.randint(1,3)

    print(f"Computer: {computer}, User: {number}")

    if computer == number:
        print("맞았습니다")
        score += 1
    else:
        print("틀렸습니다.")

    y_n = input("\n게임을 게속하시겠습니까?(y/n) : ")
    if y_n == "n":
        game = False
        print(f"지금까지 획득한 점수는 {score}점 입니다.")
