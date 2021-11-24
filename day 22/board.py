from turtle import Turtle, Screen


class Board:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(1000, 600)
        self.screen.bgcolor("black")
        self.screen.exitonclick()
