art = """
            S    S
        S       S
       S    S      S
        S    S   S
  *************************   **
   **                   **  ***
     **     Coffee    ** ****
       **           ** ***
         ***********
"""
menu = """
커피 자판기 메뉴

1.아메리카노    1800원
2.카페라떼      2700원
3.핫초코        2300원
"""
menu1 = """
빵 메뉴

1.소금빵        2500원
2.크루와상      2000원
"""

print(art)
print(menu)
print("=" * 50)
print()
coffee_price = 0
bread_price = 0
order = int(input("커피 종류를 선택하세요. 1(아메리카노), 2(카페라떼), 3(핫초코) : "))


if 1 <= order <= 3:

    if order == 1:
        coffee_price = 1800
    elif order == 2:
        coffee_price = 2700
    elif order == 3:
        coffee_price =2300
    
    
print()
cups = int(input("몇잔을 드릴까요?"))
print()
yes_no = input("빵도 드시겠습니까? : ")

if yes_no == "예" :
    print(menu1)
    print("=" * 50)
    bread_order = int(input("빵을 선택하세요. 1(소금빵), 2(크루와상) : "))

    if bread_order == 1:
        bread_price = 2500
    elif bread_order == 2:
        bread_price = 2000
else:
    pass

print()
sirup = input("시럽을 추가 하시겠습니까? 예) 예, 아니요 : ")
if sirup == "에":
    print("시럽을 추가했습니다.")
else:
    print("시럽은 추가하지 않았습니다")
print()
total_price = coffee_price * cups + bread_price
received = int(input(f"총 금액은 {total_price}원 입니다. 돈을 투입해주세요 : "))
print()
if received >= total_price:
    change = received - total_price
    print(f"{received}원을 받았습니다. 거스름돈은 {change}원입니다.")
    change_1000 = change // 1000
    remain_1000 = change % 1000
    change_500 = remain_1000 // 500
    remain_500 = remain_1000 % 500
    change_100 = remain_500 // 100

    print(f"(1000원 지폐 {change_1000}장, 500원 동전 {change_500}개, 100원 동전 {change_100}개)")
    print()
    print("맛있게 드세요~~~")
else:
    print("금액이 부족합니다. 주문이 취소 되었습니다")
    quit()