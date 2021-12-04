from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align="center", font=('Arial', 18, 'normal'))
