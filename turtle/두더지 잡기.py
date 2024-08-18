import turtle as t
import random
 
 
#원의 좌표 리스트
circle_list = [(-150, 0), (150,0), (0, 0)]#, (-150, 150),
            #    (150, 150), (0, 150), (-150, -150), (0,-150), (150,-150)]
 
score = 0
timer = 61
 
# 터틀을 클릭할 때 점수가 올라가도록 설정하기
def catch(x, y):
    global score
    score += 1
    t.ht()
    pen.clear()
    pen.write(f"점수 : {score}", False, "center", ("Arial", 15))
 
t.onclick(catch)
 
     
# 터틀이 올라갈 위치를 표여주는 원 그리기
def draw_circle():
    t.goto(-150,0)
    t.dot(100, "pink")
    t.goto(150,0)
    t.dot(100, "pink")
    t.goto(0,0)
    t.dot(100, "pink")
    # t.goto(-150,150)
    # t.dot(100, "pink")
    # t.goto(150,150)
    # t.dot(100, "pink")
    # t.goto(0,150)
    # t.dot(100, "pink")
    # t.goto(-150,-150)
    # t.dot(100, "pink")
    # t.goto(0,-150)
    # t.dot(100, "pink")
    # t.goto(150,-150)
    # t.dot(100, "pink")
     
 
# 터틀을 랜덤하게 이동하도록 설정
def turtle_move():
    global timer
    t.goto(random.choice(circle_list))
    t.st()
    for i in range(1, 30):
        t.shapesize(i/30)
    for i in range(30, 1, -1):
        t.shapesize(i/30)
    t.ht()
 
    
    t.ontimer(turtle_move, 1000)
 
 
# 그래픽창 설
t.setup(600, 600)
t.title("터틀 잡기 게임")
t.bgcolor('light blue')
t.shape("turtle")
t.speed(0)
t.penup()
               
 
# 점수 기록 하는 터틀 생성
pen = t.Turtle()
pen.penup()
pen.goto(0,260)
pen.color("white")
pen.ht()
pen.write(f"점수 : {score}", False, "center", ("Arial", 15))
 
 
# 실행하기
draw_circle()
turtle_move()
 
t.done()