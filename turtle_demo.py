import turtle
t = turtle.Turtle()


t.speed(0)

t.penup()
t.goto(-100, 100)

t.fillcolor('#FF69B4')
t.begin_fill()
t.pendown()
t.goto(100, 100)
t.goto(100, -100)
t.goto(-100, -100)
t.goto(-100, 100)
t.end_fill()

t.penup()
t.goto(0, 30)
t.setheading(90)
t.pendown()
t.circle(25)
t.circle(-25, 180)
turtle.mainloop()