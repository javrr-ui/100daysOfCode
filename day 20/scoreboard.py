from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        self.scoreboard = Turtle()
        self.scoreboard.color("white")
        self.scoreboard.hideturtle()
        self.scoreboard.write("Score: 0", False, align="center")
