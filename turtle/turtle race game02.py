import turtle as t
import time
import winsound
import random

t.ht()

t.bgcolor("lavender")
t.up()
t.speed(0)
t.goto(0, 200)
t.write("turtle race", False, "center",("", 35))

t.goto(-400, 170)
t.down()
t.color("lightpink")
t.begin_fill()

for i in range(2):
    t.forward(800)
    t.right(90)
    t.forward(400)
    t.right(90)

t.end_fill()

t.color("black")
t.up()
t.goto(330, 200)
t.down()
t.goto(330, -250)

start_ycor = [150, 90, 30, -30, -90, -150, -210]
# start_ycor = [150, 90]
color_list = ["hotpink", "white", "red", "green", "yellow", "purple", "blue"]

for i in range(6):
# for i in range(2):
    t.up()
    t.goto(-400, start_ycor[i] - 30 )
    t.color("white")
    t.down()
    t.goto(400, start_ycor[i] - 30)

turtles = []

for i in range(7):
# for i in range(2):
    new_turtle = t.Turtle()
    new_turtle.color(color_list[i])
    new_turtle.up()
    new_turtle.shape("turtle")
    new_turtle.goto(-370, start_ycor[i])
    new_turtle.write(i,)
    new_turtle.goto(-350, start_ycor[i])
    turtles.append(new_turtle)

# user_choice = int(t.textinput("turtle race", "몇번 거북이가 이길까요?"))
t.up()
# t.goto(0, -200)
# t.color("black")
# t.write(f"{user_choice}번 turtle을 응원하셨습니다.", False, "center", ("", 30))
# t.hideturtle()

winsound.Beep(523, 300)
time.sleep(0.3)

game_over = False

while not game_over:
    for i in turtles:
        ran_speed = random.randint(1, 10)
        i.forward(ran_speed)
        if i.xcor() > 350:
            game_over = True

min_xcor = 9999
winner = 0
for i in range(len(turtles)):
    if turtles[i].xcor() < min_xcor:
        min_xcor = turtles[i].xcor()
        winner = i

t.goto(0, 0)
t.write(f" {winner}번이 꼴등했습니다", False, "center", ("", 30))
# if user_choice == winner:
#     t.write(" turtle이 1등했습니다", False, "center", ("", 30))
# else:
#     t.write(f"{winner}번 turtle이 1등을 했네요...", False, "center", ("", 30))
    



t.mainloop()