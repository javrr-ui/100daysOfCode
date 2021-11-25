from turtle import Turtle, Screen


def dashed_line(screen):
    for i in range(0, screen.window_height(), int(screen.window_height() / 10)):
        line = Turtle("square")
        line.color("white")
        line.shapesize(stretch_len=2, stretch_wid=0.20)
        line.penup()
        line.tilt(90)
        line.goto(0, int(screen.window_height() / 2) - (i * 1.20))


class Paddle(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5)
        self.penup()
        self.tilt(90)
        self.goto(-450, 0)

    def up(self):
        if self.screen.window_height() / 2 > self.ycor()+50:
            self.sety(self.ycor()+5)

    def down(self):
        if (self.screen.window_height()*-1 / 2) < self.ycor() - 60:
            self.sety(self.ycor()-5)


screen = Screen()
screen.setup(1000, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
dashed_line(screen)
pad = Paddle()
while True:
    screen.onkeypress(pad.up, "w")
    screen.onkeypress(pad.down, "s")
    screen.update()
screen.update()
screen.exitonclick()
