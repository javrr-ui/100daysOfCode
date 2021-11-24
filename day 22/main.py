from turtle import Turtle, Screen


def dashed_line(screen):
    for i in range(0, screen.window_height(), int(screen.window_height() / 10)):
        line = Turtle("square")
        line.color("white")
        line.shapesize(stretch_len=2, stretch_wid=0.20)
        line.penup()
        line.tilt(90)
        line.goto(0, int(screen.window_height() / 2) - (i * 1.20))


screen = Screen()
screen.setup(1000, 600)
screen.bgcolor("black")
screen.tracer(0)
dashed_line(screen)
screen.update()
screen.exitonclick()
