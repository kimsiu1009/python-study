import turtle as t
import random

t.speed(0)
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def petal(size, angle):
    for j in range(2):
        t.circle(size, angle)
        t.left(180 - angle)

def draw_flower(petal_num, size, angle):

    t.color(random_color())
    t.begin_fill()
    for i in range(petal_num):
        petal(size, angle)
        t.left(360 / petal_num)
    t.end_fill()

    t.goto(3, -30)
    t.color(random_color())
    t.begin_fill()
    t.circle(30)
    t.end_fill()



t.hideturtle()
t.bgcolor("ivory")

t.bgcolor(random_color())

petal_num = random.randint(4, 10)
petal_size = random.randint(50, 120)
petal_angle = random.randint(90, 130)
draw_flower(petal_num, petal_size, petal_angle)

t.mainloop()