import turtle
import time
import random

t = turtle.Turtle()
t.shape('square')
t.color('black')

ts = t.screen
ts.bgcolor('khaki')

def down():
    if t.heading() != 90.0:
        t.setheading(-90.0)

def right():
    if t.heading() != 180.0:
        t.setheading(0.0)

def left(): 
    if t.heading() != 0.0: 
        t.setheading(180.0)

def up(): 
    if t.heading() != 270.0: 
        t.setheading(90.0)

ts.onkey(right, "Right")
ts.onkey(left, "Left")
ts.onkey(up, "Up")
ts.onkey(down, "Down")
ts.listen()



game_over = False

n_foods = 10
list_of_foods = []

for _ in range(n_foods):
    food = turtle.Turtle()
    food.penup()
    food.speed(0)
    food.shape('square')
    food.color('blue')
    food.goto(random.randint(-200, 200), random.randint(-200, 200))
    list_of_foods.append(food)

eaten = [False]*n_foods
segments = []


pen = turtle.Turtle()
pen.penup()
pen.goto(180, 180)
pen.color('white')
pen.ht()


report = turtle.Turtle()
report.penup()
report.goto(0, 0)
pen.color('white')
pen.ht()



steps = 0


while not game_over:
    steps += 1

    pen.write(len(segments), align = 'center', font = ('Courier', 24, 'normal'))

    for kk in range(n_foods):
        if not eaten[kk]:
            if t.distance(list_of_foods[kk]) < 20: 
                eaten[kk] = True
                list_of_foods[kk].color('green')
                segments.append(list_of_foods[kk])
                pen.clear()

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0: 
        x = t.xcor()
        y = t.ycor()
        segments[0].st()
        segments[0].goto(x, y)
    
    if len(segments) == n_foods: 
        if abs(t.xcor()) < 20 and abs(t.ycor()) < 20:
            game_over = True
            time.sleep(1)
            t.clear()
            t.ht()
            for kk in segments:
                kk.ht()
            report.write('Steps ' + str(steps), align = 'center', font = ('Courier', 24, 'normal'))






    t.forward(20)
    time.sleep(0.1)



turtle.mainloop()