import random

card = """
    @@@@@@@@@@@@@@@@
    @@    ***     @@
    @@   *   **   @@
    @@      *     @@
    @@     *      @@
    @@     *      @@
    @@            @@
    @@     *      @@
    @@@@@@@@@@@@@@@@
"""

print(card)
print("카드 뒷면에 1 ~ 30 사이에 숫자가 있습니다. 어떤 숫자가 숨겨져 있을까요? ")

game = True
while game:
    card_num = random.randint(1, 30)
    user_guess = 0
    count = 0

    while card_num != user_guess:
        print()
        user_guess = int(input("카드 뒷면의 수를 추측해 보세요~!"))
        count += 1 #count = count + 1
        if card_num > user_guess:
            print("더 큰 수 입니다.")
        elif card_num < user_guess:
            print("더 작은 수 입니다.")
    print()
    print("*" * 50)
    print(f"정답입니다~! {count}번 만에 맟추셨습니다. 감사합니다!")
    
    print("*" * 50)

    go = input("\n게임을 계속하시겠습니까? (y/n)")

    if go != "y":
        print("\n숫자 게임이 종료되었습니다.")
        game = False
