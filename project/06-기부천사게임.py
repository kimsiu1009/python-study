import random

art1 = """
A        A       B       B      C       C
 A       A      B       B      C       C
  A   1   A    B   2  B      C   3   C
   A      A   B      B     C       C
    A     A   B     B    C      C
     A     A  B    B   C     C
      A    A B    B C    C
       A    AB   BC    C
"""

art2 = """
##############   %%%%%%%%%%%%%%   @@@@@@@@@@@@@@
##          ##   %%          %%   @@          @@
##   Door   ##   %%   Door   %%   @@   Door   @@
##    1     ##   %%    2     %%   @@    3     @@
##          ##   %%          %%   @@          @@
##############   %%%%%%%%%%%%%%   @@@@@@@@@@@@@@
"""
art4 = """
       .--------.             .--------.               .--------.
  ____/_____|___ \___    ____/_____|___ \___      ____/_____|___ \___  
 O    _  1  |   _   ,*  O    _  2  |   _   ,*    O    _  3  |   _   ,*
  '--(_)-------(_)--'    '--(_)-------(_)--'      '--(_)-------(_)--'
"""
art3 = """
*********************************************
**        빵빠바방~~~ 축하합니다 !!          **
*********************************************
"""

print("\n기부천사 게임에 오신것을 환영합니다 ")
print("한 레벨을 통과할 때 마다, 기부 금액이 2배가 됩니다. ")
print("레벨 통과 실패 하면, 최초 기부 금액만 기부하게 됩니다.")
print("=" * 60)
print()
amount = int(input("기부 금액을 입력하세요 : "))
print(f"총 {amount}원을 기부하셨습니다.")
print()
print("지금부터 더 많은 금액을 기부하는 기부천사가 되어 보세요.")
print(art1)
print()
choice1 = int(input("세 갈래 길 중에서 하나를 선택하세요. (1, 2, 3) : "))
winning_num = random.randint(1, 3)

if choice1 == 1:
    amount = amount * 2  # amount *= 2
    print(art3) 
    print(f"기부 금액이 {amount}원으로 늘어났습니다!\n")

    go = input("계속 도전하시겠어요? (y/n) : ").lower()
    if go == 'y':
        print(art2)
        choice2 = int(input("세개의 문 중 하나를 선택하세요. (1, 2, 3) : "))
        winning_num = random.randint(1, 3)
        if choice2 == 1:
            amount *= 2
            print(art3)
            print(f"기부금액이 {amount}원으로 늘어났습니다!\n")

           
            go = input("계속 도전하시겠어요? (y/n) : ").lower()
            if go == 'y':
                print(art4)
                choice3 = int(input("세개의 자동차 중 하나를 선택하세요. (1, 2, 3) : "))
                winning_num = random.randint(1, 3)
                if choice3 == winning_num:
                    amount *= 2
                    print(art3)
                    print(f"기부금액이 {amount}원으로 늘어났습니다!\n")
                else:
                    print("\n저런! 애석하게 되었습니다\n")
            else:
                pass
        else:
            print("\n저런! 애석하게 되었습니다\n")
    else:
        pass
else:
    print("\n저런! 애석하게 되었습니다\n")

print("=" * 50)
print(f"당신의 총 기부금액은 {amount}원 입니다.\n")

print("당신은 착한 기부 천사에요!!!!   안녕~")
print("=" * 50)