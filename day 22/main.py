from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball


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
screen.listen()
dashed_line(screen)
l_paddle = Paddle(screen, x_pos=-450, y_pos=0)
l_paddle.set_speed(20)
r_paddle = Paddle(screen, x_pos=450, y_pos=0)
r_paddle.set_speed(20)
while True:
    screen.onkeypress(l_paddle.up, "w")
    screen.onkeypress(l_paddle.down, "s")
    screen.update()
screen.update()
screen.exitonclick()
