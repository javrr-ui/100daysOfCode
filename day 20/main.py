import turtle
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

class Snake:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.snake_body = []

    def build_snake(self, size):
        x_coord = self.x_pos
        for i in range(size):
            snake_segment = Turtle("square")
            snake_segment.penup()
            snake_segment.setx(x_coord)
            snake_segment.color("white")
            x_coord -= 20
            self.snake_body.append(snake_segment)
        screen.update()

    def left(self):
        self.snake_body[0].setheading(180)

    def right(self):
        self.snake_body[0].setheading(0)

    def up(self):
        self.snake_body[0].setheading(90)

    def down(self):
        self.snake_body[0].setheading(270)

    def move(self):
        for segment in range(len(self.snake_body)-1, 0, -1):
            x = self.snake_body[segment - 1].xcor()
            y = self.snake_body[segment - 1].ycor()
            self.snake_body[segment].goto(x, y)
        self.snake_body[0].forward(20)


snake = Snake(0, 0)
snake.build_snake(3)
screen.onkey(snake.right, "d")
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
while True:
    screen.update()
    snake.move()
    time.sleep(0.1)


screen.exitonclick()
