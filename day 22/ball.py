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

        self.positive_x = True
        self.positive_y = True

    def move(self):
        # Code to make ball bounce when it reaches y-axis walls
        if self.ycor() <= self.upper_limit and self.positive_y:
            self.sety(self.ycor() + 10)
        else:
            self.positive_y = False
            self.sety(self.ycor() - 10)
            if self.ycor() <= self.lower_limit:
                self.positive_y = True

        if self.xcor() <= self.right_limit and self.positive_x:
            self.setx(self.xcor() + 10)
        else:
            self.positive_x = False
            self.setx(self.xcor() - 10)
            if self.xcor() <= self.left_limit:
                self.positive_x = True
