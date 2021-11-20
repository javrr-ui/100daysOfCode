from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        self.scoreboard = Turtle()
        self.scoreboard.color("white")
        self.scoreboard.hideturtle()
        self.scoreboard.write(f"Score: {self.score}", False, align="center")

    def add_point(self):
        self.score += 1
