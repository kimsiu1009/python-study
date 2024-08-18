import random

num = 5
count = 1

player1_score = 0
player2_score = 0

player1 = input("player1의 이름을 입력하세요")
player2 = input("player2의 이름을 입력하세요")

print("점수 빨리내기게임에 오신것을 환영합니다" )

while num > 0:
    print("=" * 25, count,"=" * 25 )

    input(f"{player1}께서 키보드를 눌러주세요")
    player1_score += random.randint(-100,100)
    print(f"{player1}님의 점수는 {player1_score}입니다.\n")

    input(f"{player2}께서 키보드를 눌러주세요")
    player2_score += random.randint(-100,100)
    print(f"{player2}님의 점수는 {player2_score}입니다.\n")

    if player1_score > player2_score:
        print()
        print(f"{player1}님이 이겼습니다.:)")
        print() 
    elif player2_score > player1_score:
        print()
        print(f"{player2}님이 이겼습니다.:)")
        print()

    num -= 1
    count += 1

    if num == 0:
        print("게임이 종료되었습니다")
        print(f"{player1}님의 점수는{player1_score}이고, {player2}님의 점수는 {player2_score}입니다.")