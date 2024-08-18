#다각형
import turtle as t
t.speed(0)
t.Turtle()

t.bgcolor("pink")
t.color("blue")
t.width(3)
a = int(t.numinput("다각형 그리기", "몇각형을 그릴 것인지 입력하세요 :"))

for i in range(a):
    t.forward(100)
    t.left(360/a)


t.mainloop()