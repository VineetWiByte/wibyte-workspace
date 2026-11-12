import turtle
t = turtle.Turtle()

def draw_line(x0, y0, x1, y1):
    t.penup()
    t.goto(x0, y0)
    t.pendown()
    t.goto(x1, y1)


def draw_rectangle(x0, y0, len, hgt, clr):
    t.fillcolor(clr)
    t.begin_fill()
    draw_line(x0, y0, x0+len, y0)
    draw_line(x0+len, y0, x0+len, y0+hgt)
    draw_line(x0+len, y0+hgt, x0, y0+hgt)
    draw_line(x0, y0+hgt, x0, y0)
    t.end_fill()


draw_line(0, 0, 100, 100)
draw_line(-100, 10, 100, -100)


x_val = -250


for jj in range(20):
    if jj < 5:
        draw_rectangle(x_val, 0, 20, 20, 'red')
    elif jj >=5 and jj < 10: 
        draw_rectangle(x_val, 0, 20, 20, 'blue')
    else: 
        draw_rectangle(x_val, 0, 20, 20, 'green')
        
    x_val = x_val + 20






turtle.mainloop()