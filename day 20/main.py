import turtle
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


class Snake:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.snake_body = []

    def build_snake(self, size):
        x_coord = self.x_pos
        for i in range(size):
            snake_segment = Turtle("square")
            snake_segment.penup()
            snake_segment.setx(x_coord)
            snake_segment.color("white")
            x_coord -= 20
            self.snake_body.append(snake_segment)
        screen.update()


build_snake()
while True:
    screen.update()
    for segment in snake:
        segment.forward(20)
    time.sleep(0.1)

screen.exitonclick()
