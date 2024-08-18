art_100 = """
    88    ,a8888a,       ,a8888a,     
  ,d88  ,8P"'  `"Y8,   ,8P"'  `"Y8,   
    88 ,8P        Y8, ,8P        Y8,  
    88 `8b        d8' `8b        d8'  
    88  `8ba,  ,ad8'   `8ba,  ,ad8'   
    88    "Y8888P"       "Y8888P" 
"""
name = '''
                                   88  
                                   88  
                                   88  
8b,dPPYba,  ,adPPYYba, 88       88 88  
88P'    "8a ""     `Y8 88       88 88  
88       d8 ,adPPPPP88 88       88 88  
88b,   ,a8" 88,    ,88 "8a,   ,a88 88  
88`YbbdP"'  `"8bbdP"Y8  `"YbbdP'Y8 88  
88                                     
88       
'''
print(art_100)
print(name)
print(" !! 100세 시대 - 나는 어떤 모습일까요?")
print()
age = int(input("나이를 입력하세요 : "))
restoflife = 100 - age
print("여기까지 달려왔어요")
print("*" * age, end = "")
print("_" * restoflife)
print()
print("보다 지혜롭고, 보다 풍부한 경험을 지닌 100세인 나 자신을 위해 한 걸음씩 내디더 보세요 ")
print()
print("지금부터")
print('=' * 70)
print(f"일년에 한번씩 새로운 취미에 도전한다면, {restoflife}개의 도전이 기다리고 있어요.")
print(f"한달의 한번씩 여행을 간다면, {restoflife * 12 }곳에서 추억을 쌓을수있어요")
print(f"일주일에 책 한권식 읽는다면, {restoflife * 52}권의 지혜를 얻게 되실 거예요")
print(f"하루에 1개씩 영어 단어를 외운다면, {restoflife * 365}개의 영어단어를 익히게 되요. ")
print(f"하루에 한번씩 엄마 아빠께 '사랑해요' 라고 말한다면, {restoflife * 365 * 2}번의 사랑을 표현할 수 있어요.")
print(f"일주일에 수영을 두번씩 하면, {restoflife * 52 * 2}번을 할수있어요.")
print(f"한달에 한번 쇠고기(2인분)를 먹는다면, {restoflife * 12 * 2}인분을 먹을 수 있어요.")