import turtle as t
import random

size = 50
color = ["red", "pink", "lightblue", "greenyellow", "black"]
t.bgcolor("ivory")
t.speed(0)


def draw_dot(x, y):
    t.up()
    t.goto(x, y)
    t.dot(size)

def draw_square(x, y):
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(random.randint(0, 360))
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(360/4)
    t.end_fill()

def draw_triangle(x, y):
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(random.randint(0, 360))
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(360/3)
    t.end_fill()

def size_up():
    global size
    size += 10 

def size_down():
    global size
    if  size > 10: 
        size -= 10 

def rand_color():
    t.color(random.choice(color))


t.onscreenclick(draw_dot, 1)
t.onscreenclick(draw_square, 3)
t.onscreenclick(draw_triangle, 2)

t.onkeypress(size_up, "Up")
t.onkeypress(size_down, "Down")
t.onkeypress(rand_color, "space")

t.listen()

t.mainloop()