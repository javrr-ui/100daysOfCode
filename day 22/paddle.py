from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, screen, x_pos, y_pos):
        super().__init__()
        self.screen = screen
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5)
        self.penup()
        self.tilt(90)
        self.goto(x_pos, y_pos)
        self.speed = 0
        self.x_pos = x_pos
        self.y_pos = y_pos

    def up(self):
        if self.screen.window_height() / 2 > self.ycor() + 55:
            self.sety(self.ycor() + self.speed)

    def down(self):
        if (self.screen.window_height() * -1 / 2) < self.ycor() - 60:
            self.sety(self.ycor() - self.speed)

    def set_speed(self, speed):
        self.speed = speed
