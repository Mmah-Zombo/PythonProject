import turtle

s = turtle.Turtle()
turtle.getcanvas()
turtle.speed(20)
turtle.bgcolor('black')
for i in range(13):
    for c in ('red', 'blue', 'yellow'):
        turtle.left(10)
        turtle.color(c)
        turtle.circle(100)
turtle.hideturtle()
turtle.mainloop()
