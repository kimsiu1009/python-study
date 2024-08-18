print("\n1인떡볶이 집에 오신 것을 환영합니다.")
menu = """
--------------------------------------------------------
떡볶이

1. 떡볶이(1인분): 2000원        
2. 매콤떡볶이(1인분): 2300원    
3. 치즈 떡볶이(1인분): 2700원 
----------------------------------------------------------   
"""
menu1 = """
----------------------------------------------------------
음료

음료(사이다,콜라): 1000원
----------------------------------------------------------
"""
menu2 = """
----------------------------------------------------------
김말이

김말이(1개): 500원
----------------------------------------------------------
"""
print(menu)
order1 = input("드실 떡볶이를 고르세요. : ")

current = 0 
order1_price = 0

if order1 == "떡볶이":
    order1_price = 2000
elif order1 == "매콤떡볶이":
    order1_price = 2300
elif order1 =="치즈 떡볶이":
    order1_price = 2700

order2 = int(input("몇인분 드시겠습니까? 예) 1 2 3 : "))

order2_price = 0

if order2 == 1:
    order2_price = 1
if order2 == 2:
    order2_price = 2
if order2 == 3:
    order2_price = 3

current += order1_price * order2_price
print(f"현재 금액은 {current}원입니다.")

print()
print(menu1)
print()
order3_price = 0
beverage = input("음료수를 드시겠어요? (y/n) : ")
if beverage == "y":
    order3 = input("드실 음료를 고르세요. : ")

    if order3 == "사이다":
        order3_price = 1000
    elif order3 == "콜라":
        order3_price = 1000


else:
    pass


current += order3_price    #current = current + order3_price
print(f"현재 금액은 {current}원입니다.")

print(menu2)
print()
order4 = input("김말이는 드시겠습니까? (y/n) : ")

order4_price = 0
order5_price = 0

if order4 == "y":
    order4_price = 500
    order5 = int(input("몇인분을 드시겠습니까? 예) 1 2 3 : "))

    order5_price = 0

    if order5 == 1:
        order5_price = 1
    elif order5 == 2:
        order5_price = 2
    elif order5 == 3:
        order5_price = 3
    
    current += order4_price * order5_price
    print(f"현재 금액은 {current}원입니다.")

elif order4 == "n":
    pass


# total = (order1_price * order2_price) + order3_price + (order4_price * order5_price)

while True:
    received = int(input(f"총 금액은 {current}원 입니다. 돈을 입력하세요 : "))
    print()
    if received >= current:
        change = received - current
        print(f"{received}원을 받았습니다. 거스름돈은 {change}원입니다.")
        change_1000 = change // 1000
        remain_1000 = change % 1000
        change_500 = remain_1000 // 500
        remain_500 = remain_1000 % 500
        change_100 = remain_500 // 100

        print(f"(1000원 지폐 {change_1000}장, 500원 동전 {change_500}개, 100원 동전 {change_100}개)")
        print()
        print("맛있게 드세요~~~")
        break
    else:
        print(" 주문하신 금액보다 입력한 금액이 부족합니다.") 
        go = input(" 주문을 취소 하시겠습니까?(y/n) : ")
        if go == "y":
            print("주문이 취소 되었습니다. 또 이용해 주세요.")
            break # while False