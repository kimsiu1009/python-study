import turtle as t

t.speed(0)

def green_color():
    t.color("greenyellow")

def red_color():
    t.color("red")

def pink_color():
    t.color("pink")

def white_color():
    t.color("white")

def penup():
    t.up()

def pendown():
    t.down()

def begin_fill():
    t.begin_fill()
    
def end_fill():
    t.end_fill()

def draw_ondrag(x, y):
    t.ondrag(None)
    t.goto(x, y)
    t.ondrag(draw_ondrag)

t.bgcolor("lightblue")

t.pensize(3)

t.onscreenclick(draw_ondrag)

t.onkeypress(green_color, "g")
t.onkeypress(red_color, "r")
t.onkeypress(pink_color, "p")
t.onkeypress(white_color, "w")
t.onkeypress(penup, "Up")
t.onkeypress(pendown, "Down")
t.onkeypress(begin_fill, "Left")
t.onkeypress(end_fill, "Right")




t.listen()

t.mainloop()