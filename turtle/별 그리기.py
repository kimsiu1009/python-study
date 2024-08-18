import turtle as t
import random

color = ("red", "orange", "blue", "green", "white","yellow","indigo", "pink")

t.bgcolor("black")
t.speed(0)

for x in range(30):
    t.up()
    t.goto(random.randint(-300 , 300), random.randint(-300, 300))
    t.down()

    #t.dot(5, random.choice(color))

    t.color(random.choice(color))
    t.begin_fill()
    star_size = random.randint(5, 15)
    for i in range(5):
            t.forward(star_size)
            t.left(72)
            t.forward(star_size)
            t.right(144)

    t.end_fill()
#북두칠성
origin = [(0, 0), (35, -70), (105, -20), (85, 40), (160, 70), (240, 70), (310, 60)]

for i in range(7):
    t.color(random.choice(color))
    t.color("gold")
    t.up()
    t.goto(origin[i][0], origin[i][1])
    t.down()
    t.begin_fill()
    for i in range(5):
        t.forward(10)
        t.left(72)
        t.forward(15)
        t.right(144)
    t.end_fill()
    
t.hideturtle()
t.mainloop()