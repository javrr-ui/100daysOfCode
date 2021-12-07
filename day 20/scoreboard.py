from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def add_point(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=('Arial', 20, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, align="center", font=('Arial', 25, 'normal'))
