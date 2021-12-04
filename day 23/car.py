from turtle import Turtle
from random import choice, randint
COLORS = ["red", "green", "yellow", "orange", "blue", "purple"]


class Car(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(choice(COLORS))
        self.penup()
        self.speed = 5
        self.setx(x_pos)
        self.sety(y_pos)

    def move(self):
        self.setx(self.xcor() - self.speed)

    def change_speed(self, new_speed):
        self.speed = new_speed
