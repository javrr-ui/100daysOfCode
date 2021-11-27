from turtle import Turtle


class Ball(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.screen = screen

    def move(self):
        self.goto(self.xcor()+10, self.ycor()+10)
