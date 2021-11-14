import turtle
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = []


def build_snake():
    x_coord = 0
    for i in range(3):
        snake_segment = Turtle("square")
        snake_segment.penup()
        snake_segment.setx(x_coord)
        snake_segment.color("white")
        x_coord -= 20
        snake.append(snake_segment)
    screen.update()


snake()
screen.exitonclick()
