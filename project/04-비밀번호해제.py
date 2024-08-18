lock = """
-------------------------
|     +     +     +     |
|                       |
|        Locked         |
|                       |
| 비빌번호를 입력하세요 |
|                       |
-------------------------
"""
unlock = """
-------------------------
|     +     +     +     |
|                       |
|        Welcome        |
|                       |
| 비빌번호가 해제됐어요 |
|                       |
-------------------------
"""
wrong = """
-------------------------
|     +     +     +     |
|                       |
|        locked!        |
|                       |
| 잘못된 비빌번호입니다 |
|                       |
-------------------------
"""


password = "131009"

go =True

while go:
    print(lock)
    pw = input("비빌번호를 입력하세요 : ")

    if pw == password:
        print(unlock)
        break
    else:
        print(wrong)












    
else:
    print(wrong)