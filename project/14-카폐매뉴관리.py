juice = """
           * O ||  O 0
        O   *  || @  *  0
          O ~~~~~~~~~
            \\O  * O/
             \\ @  /
             |@   |
             |   O|
             ~~~~~~
"""

print(juice)
print("-- 주스 카폐 관리자 보드 --")
print()
flavor = ["사과", "당근", "망고"]

user_input = 0
while user_input != "5":

    print("""
====== 관리자 모드 ======
    1. 메뉴 출력
    2. 신메뉴 추가하기
    3. 메뉴 삭제하기
    4.메뉴 이름 바꾸기
    5.관리자 모드 종료하기
=========================
""")

    user_input = input("원하는 기능을 선택하세요. : ")
    if user_input == "1":
        for i in flavor:
            print(f"{i} 주스")
    elif user_input == "2":
        new_flavor = input("메뉴 이름을 입력해주세요. : ")
        flavor.append(new_flavor)
    elif user_input == "3":
        remove_flavor = input("삭제할 메뉴를 선택하세요. : ")
        flavor.remove(remove_flavor)
    elif user_input == "4":
        for i in range(len(flavor)):
            print(f"{i}. {flavor[i]}")

        index = int(input("몇 번째 메뉴를 변경하시겠습니까? : "))
        new_name = input("변경할 이름을 임력하세요 : ")

        print(f"{flavor[index]} 메뉴를 {new_name}으로 변경했습니다.")
        flavor[index] = new_name
        
print("관리자 모드를 종료합니다.")

