#순서 1. 단어 추가(중요)   2. 단어 해석

logo = """
 ■■■■■■   ■    ■■     ■        ■    ■   ■■■■■■■  ■
 ■■  ■■■■■■  ■■■■■■   ■        ■    ■   ■■■■■■■  ■
 ■    ■   ■  ■■  ■■   ■        ■    ■      ■     ■
 ■    ■   ■  ■    ■   ■        ■    ■     ■■  ■■■■
 ■■  ■■■■■■  ■    ■■■■■       ■■    ■■■■ ■■■■    ■
 ■■■■■■   ■  ■    ■   ■       ■■■   ■■■■■■■ ■■■  ■
          ■  ■    ■   ■      ■■■■■  ■  ■■■   ■■  ■
    ■■■■■■   ■■  ■■   ■     ■■  ■■■ ■     ■      ■
   ■■■  ■■■  ■■■■■■   ■    ■■    ■■ ■     ■      ■
   ■■     ■           ■             ■     ■       
   ■■    ■■           ■             ■     ■       
    ■■■■■■■           ■             ■     ■■■■■■■■
"""
menu = """
===================
1. 단어 찾기
2. 새로운 단어 등록
3. 등록된 단어 삭제 
4. 등록된 단어 보기
===================
""" 

def dic_list():
    keys = list(dic_eng.keys())
    
    for i in keys:
        print(i)

dic_eng = {                                                                      
    "apple": "사과",                                                         
    "peach": "복숭아", 
    "mango": "망고",
    "grape": "포도",
    "molar": "어금니",
    "ajective": "형용사",
    "beverage": "음료수",
    "approch": "접근하다",
    "discover": "발견하다"
}
print()

print()
print("*" * 50)
print("영어 단어 사전에 오신것을 환영합니다.")
print("*" * 50)

play = True
while play:

    print(menu)
    choice = input("메뉴를 선택하세요 예) 1, 2, 3, 4 : ")
    print()

    if choice == "1":
        do = True
        while do:
            # values = list(dic_eng.values())
            print("검색 가능한 단어는 다음과 같습니다.")
            print()

            print("-" * 50)
            dic_list()
            print("-" * 50)
            user_input = input("검색할 영어 단어를 입력하세요 : ")
            print()

            if user_input in dic_eng:
                print(f"검색하신 단어 {user_input}의 뜻은 {dic_eng[user_input]}입니다.")
                print()
            else:
                print("검색하신 단어는 등록되어 있지 않습니다.")
                print()

            ans = input("영어 단어 사전을 계속 찾아 보시겠습니까? (y/n)")
            if ans == "n":
                do = False

    elif choice == "2":
        new = input("새로운 단어를 입력하세요. 예) apple 사과 : ").split()
        dic_eng[new[0]] = new[1]
        print(dic_eng)
    
    elif choice == "3":
        print("-" * 50)
        dic_list()
        print("-" * 50)
        del_word = input("삭제할 단어를 입력하세요. : ")
        del dic_eng[del_word]
    
    elif choice == "4":
        print("=" * 5, "등록된 단어","=" * 5)
        dic_list()
        print("=" * 25)

    choice2 = input("\n사전을 게속 찾아 보시겠습니까? (y/n) : ")
    if choice2 == "n":
        play = False