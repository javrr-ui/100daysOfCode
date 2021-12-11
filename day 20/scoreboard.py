from turtle import Turtle
from file_reader import FileReader


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(FileReader.get_high_score())
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def add_point(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}   High score: {self.high_score}", False, align="center", font=('Arial', 20, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            FileReader.set_high_score(str(self.high_score))

        self.score = 0
        self.update_score()
