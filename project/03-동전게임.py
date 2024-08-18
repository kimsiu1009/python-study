import random

lion = """
   \|\||
  -' ||||/
 /7   |||||/
/    |||||||/`-.____________
\-' |||||||||               `-._
 -|||||||||||               |` -`.
   ||||||               \   |   `\\
    |||||\  \______...---\_  \    \\
       |  \  \           | \  |    ``-.__--.
       |  |\  \         / / | |       ``---'
     _/  /_/  /      __/ / _| |
    (,__/(,__/      (,__/ (,__/

"""
monkey = """
          __
     w  c(..)o   (
      \__(-)    __)
          /\   (
         /(_)___)
         w /|
          | \\
         m  m
"""

menu = """
0. 앞
1. 뒤
"""

print("동전게임에 오신것을 환영합니다!")
go = True
while go:
    print(menu)

    choice = input("번호를 선택하세요 : ")
    isdigit = choice.isdigit()
    if isdigit:
        choice = int(choice)
    else:
        print("숫자를 입력해 주세요")
        quit()

    # 컴퓨터가 동전을 던진다

    computer = random.randint(0, 1)
    print()

    if choice == 1:
        print("당신의 선택은  '뒤' 입니다.")
    elif choice == 0:
        print("당신의 선택은  '앞' 입니다.")
    else:
        print("잘못된 선택입니다.")
        
    if computer:
        print("컴퓨터의 선택은 '뒤' 입니다.")
    else:
        print("컴퓨터의 선택은 '앞' 입니다.")

    if choice == computer:
        print(lion)
        print("축하합니다! 맞췄습니다!")
    else:
        print(monkey)
        print("예석합니다. 틀렸습니다. 다시 시도해 주세요.")

    stop = input("게임을 계속하시겠습니까? (y/n)")

    if stop == "y":
        pass
    else:
        go = False


