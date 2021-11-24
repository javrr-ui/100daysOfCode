from turtle import Turtle, Screen


def dashed_line(screen):
    for i in range(0, screen.window_height(), int(screen.window_height() / 10)):
        dashed_line = Turtle("square")
        dashed_line.color("white")
        dashed_line.shapesize(stretch_len=2, stretch_wid=0.20)
        dashed_line.penup()
        dashed_line.tilt(90)
        dashed_line.goto(0, int(screen.window_height() / 2) - (i * 1.20))


screen = Screen()
screen.setup(1000, 600)
screen.bgcolor("black")
screen.tracer(0)
dashed_line(screen)
screen.update()
screen.exitonclick()
