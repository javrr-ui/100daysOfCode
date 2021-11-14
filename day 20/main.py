from turtle import Turtle, Screen

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")


def snake():
    x_coord = 0
    for i in range(3):
        snake_segment = Turtle("square")
        snake_segment.penup()
        snake_segment.setx(x_coord)
        snake_segment.color("white")
        x_coord -= 20


screen.exitonclick()
