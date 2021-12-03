from turtle import Turtle
from random import choice, randint
COLORS = ["red", "green", "yellow", "orange", "blue", "purple"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(choice(COLORS))
        self.penup()
        self.speed = randint(3, 7)
        self.setx(300)

    def move(self):
        self.setx(self.xcor() - self.speed)
