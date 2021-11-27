from turtle import Turtle


class Ball(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.screen = screen

        self.upper_limit = self.screen.window_height() / 2 - 20  # -20 pixel gap
        self.lower_limit = (self.screen.window_height() / 2 * -1) + 20  # +20 pixel gap
        self.left_limit = self.screen.window_width() / 2 * -1 + 10  # +10 pixel gap
        self.right_limit = self.screen.window_width() / 2 - 30  # 30 pixel gap

    positive_x = True
    positive_y = True

    def move(self):
        self.goto(self.xcor()+10, self.ycor()+10)
