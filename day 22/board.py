from turtle import Turtle, Screen


class Board:
    def dashed_line(self):

        for i in range(0, self.screen.window_height(), int(self.screen.window_height()/6)):
            dashed_line = Turtle("square")
            dashed_line.color("white")
            dashed_line.shapesize(stretch_len=3)
            dashed_line.penup()
            dashed_line.tilt(90)
            dashed_line.goto(0, int(self.screen.window_height()/2)-(i*1.20))
