from turtle import Turtle
MOVE_DISTANCE = 5


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def move_up(self):
        self.goto(0, self.ycor() + MOVE_DISTANCE)

    def reset_position(self):
        self.goto(0, -280)
