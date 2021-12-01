from turtle import Turtle
from random import Random
COLORS = ["red", "green", "yellow", "orange", "blue", "purple"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
