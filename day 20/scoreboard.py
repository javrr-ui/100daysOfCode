from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        self.scoreboard = Turtle()
        self.scoreboard.color("white")
        self.scoreboard.hideturtle()
        self.scoreboard.goto(0, 260)
        self.update_score()

    def add_point(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.scoreboard.clear()
        self.scoreboard.write(f"Score: {self.score}", False, align="center", font=('Arial', 20, 'normal'))
