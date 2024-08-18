import turtle as t

t.speed(0)

def petal():
    for j in range(2):
        t.circle(150, 110)
        t.left(70)

def draw_flower(x, y):
    t.up()
    t.goto(x, y)
    t.down()
    t.color("pink")
    t.begin_fill()
    for i in range(5):
        petal()
        t.left(360 / 5)
    t.end_fill()

    t.goto(x + 3, y - 30)
    t.color("hotpink")
    t.begin_fill()
    t.circle(30)
    t.end_fill()



t.hideturtle()
t.bgcolor("ivory")

draw_flower(0, 0)
draw_flower(-200, 200)
draw_flower(200, -200)

t.mainloop()