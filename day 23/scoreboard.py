from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.goto(-250, 260)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align="center", font=('Arial', 18, 'normal'))

    def level_up(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align="center", font=('Arial', 25, 'normal'))
