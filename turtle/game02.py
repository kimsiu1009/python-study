import turtle as t

t.setup(500, 800)
t.bgcolor("lightgreen")

t.ht()
t.up()

def turn_left():
    player.backward(10)
    
def turn_right():
    player.forward(10)

player = t.Turtle()
player.shape("square")
player.shapesize(1, 1)
player.color("white")
player.up()
player.speed(0)
player.goto(0, -270)

block = t.Turtle()
block.shape("square")
block.shapesize(4, 4)
block.up()
block.speed(0)
block.goto(700, -270)

t.onkeypress(turn_left, "Left")
t.onkeypress(turn_right, "Right")
t.listen()

t.mainloop()